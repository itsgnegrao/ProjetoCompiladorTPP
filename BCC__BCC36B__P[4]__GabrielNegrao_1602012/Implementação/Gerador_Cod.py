# -----------------------------------------------------------------------------
# UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - UTFPR-CM
# Gabriel Negrão Silva - 1602012 - 30/11/2017
# Compiladores - Ciência Da Computação
# Gerador_Cod.py
# -----------------------------------------------------------------------------

from llvmlite import ir
from llvmlite import binding as llvm
from ctypes import CFUNCTYPE, c_int32
from Analisador_Semantico import Analisador_Semantico
import sys

class Gerador_Cod:
    def __init__(self, code):
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()

        self.ee = self.create_execution_engine()

        As = Analisador_Semantico(code,False)
        self.arvoreSintatica = As.arvoreSintatica
        self.tabSimbolos = As.tabSimbolos

        self.module = ir.Module(code)
        self.module.triple = llvm.Target.from_triple("x86_64-pc-linux-gnu")

        self.escopo = "global"
        self.escreva = None
        self.leia = None
        self.builder = None

        self._codegen__programa(self.arvoreSintatica)


    def _codegen__programa(self, node):
        self._codegen_listaDeclaracoes(node.child[0])

    def _codegen_listaDeclaracoes(self, node):
        if len(node.child)==1:
            self._codegen_declaracao(node.child[0])
        else:
            self._codegen_listaDeclaracoes(node.child[0])
            self._codegen_declaracao(node.child[1])

    def _codegen_declaracao(self,node):
        if(node.child[0].type == "declaracao_variaveis"):
            self._codegen_declaracaoVar(node.child[0])
        else:
            self._codegen_declaracaoFuncao(node.child[0])

    def _codegen_declaracaoFuncao(self, node):
        if(node.child[0].type == "cabecalho"):
            str_args = self.tabSimbolos[node.child[0].value][2]
            self.escopo = node.child[0].value
            return_type = ir.VoidType()
            args_type = ()
            if(str_args != "void"):
                for a in str_args:
                    args_type = args_type + (self._codegen_tipo(a),)

            tipo_func = ir.FunctionType(return_type,args_type)
            self.func = ir.Function(self.module,tipo_func,node.child[0].value)
            self.tabSimbolos[node.child[1].value].append(self.func)
            bb = func.append_basic_block('entrada')
            self.builder = ir.IRBuilder(bb)
            self._codegen_listaParametros(node.child[1].child[0])
            self._codegen_corpo(node.child[0].child[1])
            self.escopo = "global"

        else:
            str_args = self.tabSimbolos[node.child[1].value][2]
            self.escopo = node.child[1].value
            return_type = self._codegen_tipo(node.child[0])
            args_type = ()
            if(str_args != "void"):
                for a in str_args:
                    args_type = args_type + (self._codegen_tipo(a),)

            tipo_func = ir.FunctionType(return_type,args_type)
            self.func = ir.Function(self.module,tipo_func,node.child[1].value)
            self.tabSimbolos[node.child[1].value].append(self.func)
            bb = self.func.append_basic_block('entrada')
            self.builder = ir.IRBuilder(bb)
            self._codegen_listaParametros(node.child[1].child[0])
            self._codegen_corpo(node.child[1].child[1])
            self.escopo = "global"

    def _codegen_listaParametros(self,node):
        listaParams = []

        if (len(node.child) == 1):
            self._codegen_parametro(node.child[0])

        else:
            self._codegen_listaParametros(node.child[0])
            self._codegen_parametro(node.child[1])

    def _codegen_parametro(self, node):
        if(node != None):
            tipo = self._codegen_tipo(node.child[0])

            var = self.builder.alloca(tipo, name = node.value)
            self.tabSimbolos[self.escopo+"-"+node.value].append(var)

    def _codegen_corpo(self,node):
        if (len(node.child)==1):
            return
        else:
            self._codegen_corpo(node.child[0])
            self._codegen_acao(node.child[1])

    def _codegen_acao(self,node):
        if (node.child[0].type=="expressao"):
            return self._codegen_expressao(node.child[0])
        elif (node.child[0].type=="declaracao_variaveis"):
            return self._codegen_declaracaoVar(node.child[0])
        elif (node.child[0].type=="se"):
            return self._codegen_se(node.child[0])
        elif (node.child[0].type=="repita"):
            return self._codegen_repita(node.child[0])
        elif (node.child[0].type=="leia"):
            return self._codegen_leia(node.child[0])
        elif (node.child[0].type=="escreva"):
            return self._codegen_escreva(node.child[0])
        elif (node.child[0].type=="retorna"):
            return self._codegen_retorna(node.child[0])


    def _codegen_se(self,node):
        condicao = self._codegen_expressaoLogica(node.child[0])

        se_entao = self.func.append_basic_block('se-então')
        if (len(node.child)== 3):
            senao = self.func.append_basic_block('senão')
        fim = self.func.append_basic_block('fim')

        if (len(node.child)==3):
            self.builder.cbranch(condicao, se_entao, se_entao)
        else:
            self.builder.cbranch(condicao, se_entao, fim)

        self.builder.position_at_start(se_entao)
        self._codegen_corpo(node.child[1])

        self.builder.branch(fim)
        if (len(node.child)==3):
            self.builder.position_at_start(senao)
            self._codegen_corpo(node.child[2])
            self.builder.branch(fim)

        self.builder.position_at_start(fim)

    def _codegen_repita(self, node):
        repita = self.func.append_basic_block('repita')
        fim_repita = self.func.append_basic_block('fim_repita')

        self.builder.branch(repita)
        self.builder.position_at_start(repita)
        self._codegen_corpo(node.child[0])

        condicao = self._codegen_expressaoLogica(node.child[1])

        self.builder.cbranch(condicao, fim_repita, repita)
        self.builder.position_at_start(fim_repita)



    def _codegen_expressaoLogica(self,node):
        exp1 = self._codegen_expressao(node.child[0])
        exp2 = self._codegen_expAditiva(node.child[0].child[2])

        if node.child[0].child[1].value   == "=":
            res = self.builder.icmp_signed("==", exp1, exp2)
        else:
            res = self.builder.icmp_signed(node.child[0].child[1].value, exp1, exp2)

        return res

    def _codegen_declaracaoVar(self,node):
        tipo = self._codegen_tipo(node.child[0])
        if (self.escopo == "global"):
            for ret in self._codegen_listaVars(node.child[1]):
                var = ir.GlobalVariable(self.module, tipo, name = ret)
                self.tabSimbolos[self.escopo+"-"+ret].append(var)
        else:
            for ret in self._codegen_listaVars(node.child[1]):
                var = self.builder.alloca(tipo, name = ret)
                self.tabSimbolos[self.escopo+"-"+ret].append(var)

    def _codegen_listaVars(self, node):
        retArgs=[]

        if (len(node.child) == 1):
            if (len(node.child[0].child) == 1):
                retArgs.append(node.child[0].value+self.indice(node.child[0].child[0]))
            else:
                retArgs.append(node.child[0].value)

            return retArgs
        else:
            retArgs=self._codegen_listaVars(node.child[0])

            if(len(node.child[1].child))==1:
                retArgs.append(node.child[1].value)+self.indice(node.child[1].child[0])
            else:
                retArgs.append(node.child[1].value)

            return retArgs

    def _codegen_retorna(self, node):
        res = self._codegen_expressao(node.child[0])
        self.builder.ret(res)


    def _codegen_expressao(self, node):
        res = None
        if (node.type == "operador_relacional"):
            print("entrei")
            res = node.value
        elif (node.child[0].type) == "expressao_simples":
            res = self._codegen_expressaoSimples(node.child[0])
        else:
            res = self._codegen_atribuicao(node.child[0])

        return res

    def _codegen_expressaoSimples(self,node):
        res = None
        if len(node.child)==1:
            res = self._codegen_expAditiva(node.child[0])
        else:
            print("HAHAHAHAAHAH")
#            tipoExp1 = self.expSimples(node.child[0])
#           self.opRelacional(node.child[1])
#            tipoExp2 = self.expAditiva(node.child[2])

        return res

    def _codegen_atribuicao(self,node):
        if(node.child[0].type == "var"):
            var = None
            try:
                var = self.tabSimbolos[self.escopo+"-"+node.child[0].value][6]
                tipo = self._codegen_tipo(self.tabSimbolos[self.escopo+"-"+node.child[0].value][4])
            except:
                if var == None:
                    try:
                        var = self.tabSimbolos["global-"+node.child[0].value][6]
                        tipo = self._codegen_tipo(self.tabSimbolos["global-"+node.child[0].value][4])
                    except:
                        pass

            res = self._codegen_expressao(node.child[1])
            if res != None:
                self.builder.store(res, var)
#        else:
#            print("SLAAAAAA")
#            print(node)
#            res = self._codegen_expAditiva(node)
#            print(res)
#            print("SLAAAAAA2")




    def _codegen_expAditiva(self,node):
        res = None
        if len(node.child)==1:
            res = self._codegen_expMultiplicativa(node.child[0])
        else:
            Exp1 = self._codegen_expAditiva(node.child[0])
            Exp2 = self._codegen_expMultiplicativa(node.child[2])

            if(node.child[1].value == "+"):
                res = self.builder.fadd(Exp1, Exp2)
            elif(node.child[1].value == "-"):
                res = self.builder.fsub(Exp1, Exp2)

        return res


    def _codegen_expMultiplicativa(self,node):
        res = None

        if (len(node.child) == 1):
            res = self._codegen_expUnaria(node.child[0])
        else:
            Exp1 = self._codegen_expMultiplicativa(node.child[0])
            Exp2 = self._codegen_expUnaria(node.child[2])

            if(node.child[1].value == "*"):
                res = self.builder.fmul(Exp1, Exp2)
            elif(node.child[1].value == "/"):
                res = self.builder.fdiv(Exp1, Exp2)

        return res

    def _codegen_expUnaria(self,node):
        res = None

        if(node.type == "fator"):
            res = self._codegen_fator(node)
        elif (len(node.child) == 1):
            res = self._codegen_fator(node.child[0])
        else:
            if(node.child[0].value == "-"):
                res = self._codegen_fator(node.child[1],node.child[0])

        return res

    def _codegen_fator(self, node, op=None):
        res = None

        if(node.child[0].type=="var"):
            try:
                res = self.builder.load(self.tabSimbolos[self.escopo+"-"+node.child[0].value][6])
            except:
                if(res == None):
                    res = self.builder.load(self.tabSimbolos["global-"+node.child[0].value][6])


        elif(node.child[0].type=="chamada_funcao"):
            res = self._codegen_chamadaFuncao(node.child[0])
        elif(node.child[0].type=="numero"):
            res = self._codegen_numero(node.child[0], op)
#        else:
#            return self.expressao(node.child[0])
        return res

    def _codegen_chamadaFuncao(self,node):
        nome_func = node.value
        self.func = self.builder.load(self.tabSimbolos[nome_func][6])

        lista_args = self._codegen_argsChamadaFuncao(node.child[0])
        return self.builder.call(self.func,lista_args)

    def _codegen_argsChamadaFuncao(self, node):
        if(len(node.child)==1):
            if(node.child[0].type=="expressao"):
                return self._codegen_expressao(node.child[0])
            else:
                return []
        else:
            retArgs = []
            retArgs.append(self._codegen_argsChamadaFuncao(node.child[0]))
            retArgs.append(self._codegen_expressao(node.child[1]))

            return retArgs

    def _codegen_numero(self, node, op=None):
        res = None
        valor = node.value

        string = repr(valor)
        if "."in string:
            if(op):
                valor = float(valor)*-1
            res = ir.Constant(ir.DoubleType(), valor)
        else:
            if(op):
                valor = int(valor)*-1
            res = ir.Constant(ir.IntType(32), valor)

        return res

    def _codegen_escreva(self,node):
        escreva_t = ir.FunctionType(ir.VoidType(), [ir.IntType(32)])
        print("ola")
        self.escreva = ir.Function(self.module, escreva_t, 'escreva')
        print("ola2")
        x = self._codegen_expressao(node.child[0])
        print("ola3")
        self.builder.call(self.escreva, [x])
        print("ola4")
        #self.mod = self.compile_ir()
        #func_ptr = self.ee.get_function_address("escreva")
        #cfunc = CFUNCTYPE(c_int32)(func_ptr)
        #retval = cfunc()

    def _codegen_leia(self, node):
        print("COCOOCOCOCOCOCCOOCCO")
        if(self.leia != None):
            leia_t = ir.FunctionType(ir.IntType(32), [])
            print(leia_t)
            self.leia = ir.Function(self.module, leia_t, name = 'leia')
            x = self.builder.call(self.leia, [])
            res = ir.Constant(ir.DoubleType(), [x])
            self.builder.ret(res)
            #self.mod = self.compile_ir()
            #func_ptr = self.ee.get_function_address("leia")
            #cfunc = CFUNCTYPE(c_int32)(func_ptr)
            #retval = cfunc()

    def _codegen_tipo(self, node):
        #Caso string
        if(node == 'inteiro'):
            return ir.IntType(32)
        elif(node == 'flutuante'):
            return ir.DoubleType()
        else:
            #Caso type
            if(node.type=="inteiro"):
                return ir.IntType(32)
            else:
                return ir.DoubleType()


    def compile_ir(self):
        self.mod = llvm.parse_assembly(str(self.module))
        self.mod.verify()
        self.ee.add_module(self.mod)
        self.ee.finalize_object()
        return self.mod

    def create_execution_engine(self):
        target = llvm.Target.from_triple("x86_64-pc-linux-gnu")
        target_machine = target.create_target_machine()
        backing_mod = llvm.parse_assembly("")
        engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
        return engine

        llvm.load_library_permanently("//funcoesC.so")



if __name__ == '__main__':
    GenCod = Gerador_Cod(sys.argv[1])
    print(GenCod.module)
