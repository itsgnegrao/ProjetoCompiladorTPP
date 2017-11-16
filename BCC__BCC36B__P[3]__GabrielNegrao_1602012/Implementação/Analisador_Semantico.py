# -----------------------------------------------------------------------------
# UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - UTFPR-CM
# Gabriel Negrão Silva - 1602012 - 16/11/2017
# Compiladores - Ciência Da Computação
# Analisador_Semantico.py
# -----------------------------------------------------------------------------

# Importação ply lexer
from graphviz import Graph
import ply.yacc as yacc
from Analisador_Sintatico import Analisador_Sintatico
import sys
import os

class Analisador_Semantico:

    def __init__(self, code, flag):
        self.tabSimbolos = {}
        self.escopo="global"
        self.debug = flag

        self.arvoreSintatica = Analisador_Sintatico(code).ast
        self.programa(self.arvoreSintatica)

        self.verificaDeclarPrincipal(self.tabSimbolos)
        self.verificaFuncaoUtilizada(self.tabSimbolos)
        self.verificaVarUtilizada(self.tabSimbolos)

    def programa(self,node):
        self.listaDeclaracoes(node.child[0])

    def listaDeclaracoes(self, node):
        if len(node.child)==1:
            self.declaracao(node.child[0])
        else:
            self.listaDeclaracoes(node.child[0])
            self.declaracao(node.child[1])

    def declaracao(self,node):
        if (node.child[0].type == "declaracao_variaveis"):
            self.declaracaoVar(node.child[0])
        elif (node.child[0].type=="inicializacao_variaveis"):
            self.inicializacaoVar(node.child[0])
        else:
            if(len(node.child[0].child)==1):
                self.escopo=node.child[0].child[0].value
            else:
                self.escopo=node.child[0].child[1].value

            self.declaracaoFuncao(node.child[0])
            self.escopo="global"

    def declaracaoVar(self, node):
        tipo = node.child[0].type
        string=""
        i=0
        complemento=""

        for son in self.listaVars(node.child[1]):
            if ("[" in son):
                for i in range(len(son)):
                    if (son[i]=="["):
                        break
                    string += son[i]
                complemento = son[i:]
                son = string

            if (son  in self.tabSimbolos.keys()):
                print("Erro: Já existe uma função declarada como '"+node.value+"'")
                if (self.debug):
                    exit(1)

            if("global-"+son  in self.tabSimbolos.keys()):
                print("Erro: Variável '"+son+ "' já declarada.")
                if (self.debug):
                    exit(1)

            if (self.escopo+"-"+son  in self.tabSimbolos.keys()):
                print("Erro: Variável '"+son+ "' já declarada.")
                if (self.debug):
                    exit(1)

            self.tabSimbolos[self.escopo+"-"+son]=["variavel",son,False,False,tipo+complemento,0]

        return "void"

    def listaVars(self, node):
        retArgs=[]

        if (len(node.child) == 1):
            if (len(node.child[0].child) == 1):
                retArgs.append(node.child[0].value+self.indice(node.child[0].child[0]))
            else:
                retArgs.append(node.child[0].value)

            return retArgs
        else:
            retArgs=self.listaVars(node.child[0])

            if(len(node.child[1].child))==1:
                retArgs.append(node.child[1].value)+self.indice(node.child[1].child[0])
            else:
                retArgs.append(node.child[1].value)

            return retArgs

    def declaracaoFuncao(self, node):
        if len(node.child) ==1:
            tipo = "void"

            if ("global-"+node.child[0].value in self.tabSimbolos.keys()):
                print ("Erro: Já existe uma variável declarada com o nome de -> '"+node.child[0].value+"'.")
                if (self.debug):
                    exit(1)
            elif (node.child[0].value in self.tabSimbolos.keys()):
                print ("Erro: Função "+node.child[0].value+" já declarada.")
                if (self.debug):
                    exit(1)

            self.tabSimbolos[node.child[0].value]=["funcao",node.child[0].value,[],False,tipo,0]
            self.cabecalho(node.child[0])
        else:
            tipo =self.tipo(node.child[0])
            self.tabSimbolos[node.child[1].value]=["funcao",node.child[1].value,[],False,tipo,0]
            self.cabecalho(node.child[1])


    def tipo(self,node):
        if (node.type=="inteiro" or node.type=="flutuante"):
            return node.type
        else:
            print("Erro: Tipo inválido, tipo esperado -> 'inteiro' ou 'flutuante', tipo recebido -> '"+node.child.type+"'.")
            if (self.debug):
                exit(1)

    def cabecalho(self,node):
        listaParams = self.listaParametros(node.child[0])

        self.tabSimbolos[node.value][2] = listaParams
        tipoCorpo=self.corpo(node.child[1])
        tipoFunc = self.tabSimbolos[node.value][4]

        if (tipoCorpo != tipoFunc):
            if (node.value == "principal"):
                print("Warning: A função '"+node.value+"' deveria retornar -> '"+tipoFunc+"' mas retorna -> '"+tipoCorpo+"'.")
            else:
                print("Erro: A função '"+node.value+"' deveria retornar -> '"+tipoFunc+"' mas retorna -> '"+tipoCorpo+"'.")
                if (self.debug):
                    exit(1)


    def listaParametros(self, node):
            listaParams = []

            if (len(node.child) == 1):
                if(node.child[0] == None):
                    return self.vazio(node.child[0])
                else:
                    listaParams.append(self.parametro(node.child[0]))
                    return listaParams

            else:
                lista_param = self.listaParametros(node.child[0])
                lista_param.append(self.parametro(node.child[1]))
                return lista_param

    def parametro(self, node):
        if (node.child[0].type == "parametro"):
            return self.parametro(node.child[0])+"[]"

        self.tabSimbolos[self.escopo+"-"+node.value]=["variavel",node.value,False,True,node.child[0].type,0]
        return self.tipo(node.child[0])

    def vazio(self, node):
        return "void"

    def corpo(self, node):
        if (len(node.child)==1):
            return self.vazio(node.child[0])

        else:
            tipoCorpo1 = self.corpo(node.child[0])
            tipoCorpo2 = self.acao(node.child[1])

            if(tipoCorpo2 != None):
                return tipoCorpo2

    def acao(self, node):
        tipo_ret_acao = "void"

        if (node.child[0].type=="expressao"):
            return self.expressao(node.child[0])
        elif (node.child[0].type=="declaracao_variaveis"):
            return self.declaracaoVar(node.child[0])
        elif (node.child[0].type=="se"):
            return self.se(node.child[0])
        elif (node.child[0].type=="repita"):
            return self.repita(node.child[0])
        elif (node.child[0].type=="leia"):
            return self.leia(node.child[0])
        elif (node.child[0].type=="escreva"):
            return self.escreva(node.child[0])
        elif (node.child[0].type=="retorna"):
            return self.retorna(node.child[0])

    def leia(self, node):
        if (self.escopo+"-"+node.value not in self.tabSimbolos.keys()):
            if ("global-"+node.value not in self.tabSimbolos.keys()):
                print("Erro: Variável -> '"+node.value+"' lida no escopo -> '"+self.escopo+"' não declarada.")
                if (self.debug):
                    exit(1)

        return "void"

    def escreva(self, node):
        tipoExp = self.expressao(node.child[0])

        if (tipoExp == "logico"):
            print("Erro: Expressão escreva inválida em -> '"+self.escopo+"'.")
            if (self.debug):
                exit(1)

        return "void"


    def retorna(self, node):
        tipoExp = self.expressao(node.child[0])

        if (tipoExp == "logico"):
            print("Erro: Expressão de retorno inválida em -> '"+self.escopo+"'.")
            if (self.debug):
                exit(1)

        return tipoExp

    def expressao(self, node):
        if (node.child[0].type=="expressao_simples"):
            return self.expSimples(node.child[0])
        else:
            return self.atribuicao(node.child[0])

    def expSimples(self, node):
        if len(node.child)==1:
            return self.expAditiva(node.child[0])
        else:
            tipoExp1 = self.expSimples(node.child[0])
            self.opRelacional(node.child[1])
            tipoExp2 = self.expAditiva(node.child[2])

            if(tipoExp1 != tipoExp2):
                print("Warning: Operação com tipos diferentes -> '"+tipoExp1+"' e '"+tipoExp2)

            return "logico"

    def expAditiva(self, node):
        if len(node.child)==1:
            return self.expMultiplicativa(node.child[0])
        else:
            tipoExp1 = self.expAditiva(node.child[0])
            self.opSoma(node.child[1])
            tipoExp2 = self.expMultiplicativa(node.child[2])

            if (tipoExp1 != tipoExp2):
                print("Warning: Operação com tipos diferentes -> '"+tipoExp1+"' e '"+tipoExp2)
            if ((tipoExp1=="flutuante") or (tipoExp2=="flutuante")):
                return "flutuante"
            else:
                return "inteiro"

    def expMultiplicativa(self, node):
        if (len(node.child) == 1):
            return self.expUnaria(node.child[0])
        else:
            tipoExp1 = self.expMultiplicativa(node.child[0])
            self.opMultiplicacao(node.child[1])
            tipoExp2 = self.expUnaria(node.child[2])

            if (tipoExp1 != tipoExp2):
                print("Warning: Operação com tipos diferentes -> '"+tipoExp1+"' e '"+tipoExp2)
            if ((tipoExp1=="flutuante") or (tipoExp2=="flutuante")):
                return "flutuante"
            else:
                return "inteiro"

    def expUnaria(self, node):
        if (len(node.child) == 1):
            return self.fator(node.child[0])
        else:
            self.opSoma(node.child[0])
            return self.fator(node.child[1])

    def fator(self, node):
        if(node.child[0].type=="var"):
            return self.var(node.child[0])
        if(node.child[0].type=="chamada_funcao"):
            return self.chamadaFuncao(node.child[0])
        if(node.child[0].type=="numero"):
            return self.numero(node.child[0])
        else:
            return self.expressao(node.child[0])

    def numero(self, node):
        string = repr(node.value)
        if "."in string:
            return "flutuante"
        else:
            return "inteiro"

    def var(self,node):
        name = self.escopo+"-"+node.value

        if (name not in self.tabSimbolos):
            name = "global-"+node.value

            if (name not in self.tabSimbolos):
                print("Erro: Variável '"+node.value+"' chamada em '"+self.escopo+"' não foi declarada.")
                if (self.debug):
                    exit(1)

        if (self.tabSimbolos[name][3] == False):
            print("Erro: Variável '"+name+"' chamada em '"+self.escopo+"' não foi atribuida.")
            if (self.debug):
                exit(1)

        self.tabSimbolos[name][2] = True
        return self.tabSimbolos[name][4]

    def atribuicao(self, node):
        nome = self.escopo+"-"+node.child[0].value

        if (self.escopo+"-"+node.child[0].value not in self.tabSimbolos.keys()):
            nome = "global-"+node.child[0].value

            if ("global"+"-"+node.child[0].value not in self.tabSimbolos.keys()):
                print ("Erro: Variavel '"+node.child[0].value+"' não declarada.")
                if (self.debug):
                    exit(1)

        tipoVar  = self.tabSimbolos[nome][4]
        tipoExp =  self.expressao(node.child[1])


        #atribuida e utilizada
        self.tabSimbolos[nome][2]=True
        self.tabSimbolos[nome][3]=True

        #acha o indice
        if (len(node.child[0].child) != 0):
            if(node.child[0].child[0].type == "indice"):
                tipoPosAcessada = self.indice(node.child[0].child[0]) #valida o tipo do indice
                qtdeAcessada = (len(tipoPosAcessada))
                tipoVar = tipoVar[:-qtdeAcessada]

        if (len(node.child[1].child[0].child[0].child[0].child[0].child[0].child[0].child) != 0):
            if (node.child[1].child[0].child[0].child[0].child[0].child[0].child[0].child[0].type == "indice"):
                tipoPosAcessada = self.indice(node.child[1].child[0].child[0].child[0].child[0].child[0].child[0].child[0]) #valida o tipo do indice
                qtdeAcessada = (len(tipoPosAcessada))
                tipoExp = tipoExp[:-qtdeAcessada]

        if (tipoVar != tipoExp):
            print ("Warning: Coerção de tipos, tipo esperado -> '"+tipoVar+"', tipo recebido -> '"+tipoExp+"'.")

        return "void"

    def chamadaFuncao(self, node):
        if (node.value=="principal"and self.escopo!="principal"):
            print("Erro: Chamada para a função -> 'principal' da função -> '"+self.escopo+"'.")
            if (self.debug):
                exit(1)

        if node.value not in self.tabSimbolos.keys():
            print ("Erro: Função -> '"+node.value+"' não declarada.")
            if (self.debug):
                exit(1)

        if (node.value == "principal" and self.escopo=="principal"):
            print("Warning: Chamada recursiva para a função principal.")

        self.tabSimbolos[node.value][5]=1
        argsLista = []
        argsLista.append(self.listaArgs(node.child[0]))

        if (argsLista[0]==None):
            argsLista = []
        elif (not(type(argsLista[0]) is str)):
            argsLista = argsLista[0]

        argsEsperados = self.tabSimbolos[node.value][2]

        if(type(argsEsperados) is str):
            argsEsperados = []

        if(len(argsLista)!=len(argsEsperados)):
            lenEsperados=(len(argsEsperados))
            lenRecebidos=(len(argsLista))
            print("Erro: Numero de argumentos esperados em '"+node.value+"' -> '"+str(lenEsperados)+"', quantidade de argumentos recebidos -> '"+str(lenRecebidos)+"'.")
            if (self.debug):
                exit(1)

        for i in range(len(argsLista)):
            if(argsLista[i]!=argsEsperados[i]):
                print("Erro: Argumento -> '"+str(i)+"', tipo esperado -> '"+argsEsperados[i]+"', tipo recebido -> '"+ argsLista[i]+"'.")
                if (self.debug):
                    exit(1)

        self.tabSimbolos[node.value][3]=True
        return self.tabSimbolos[node.value][4]

    def listaArgs(self, node):
        if(len(node.child)==1):
            if(node.child[0]==None):
                return
            if(node.child[0].type=="expressao"):
                return self.expressao(node.child[0])
            else:
                return []
        else:
            retArgs = []
            retArgs.append(self.listaArgs(node.child[0]))
            if(not(type(retArgs[0]) is str)):
                retArgs = retArgs[0]

            retArgs.append(self.expressao(node.child[1]))

            return retArgs


    def indice(self, node):
        if(len(node.child) == 1):
            tipo = self.expressao(node.child[0])
            if(tipo != "inteiro"):
                print("Erro: Index inválido, tipo recebido -> '"+tipo+"', tipo permitido -> 'inteiro'")
                if (self.debug):
                    exit(1)
            return("[]")

        else:
            var=self.indice(node.child[0])
            tipo=self.expressao(node.child[1])
            if(tipo != "inteiro"):
                print("Erro: Index inválido na variável'"+var+"', tipo recebido -> '"+tipo+"', tipo permitido -> 'inteiro'")
                if (self.debug):
                    exit(1)

            return ("[]"+var)

    def inicializacaoVar(self,node):
        return self.atribuicao(node.child[0])

    def repita(self, node):
        tipoLoop = self.expressao(node.child[1])

        if (tipoLoop != "logico"):
            print("Erro: Foi dado uma expressão do tipo -> '"+tipoLoop+"', tipo esperado -> 'logica', para 'repita' na função -> '"+self.escopo+"'")
            if (self.debug):
                exit(1)

        tipoCorpo = self.corpo(node.child[0])
        return tipoCorpo

    def se(self, node):
        tipoIf = self.expressao(node.child[0])

        if (tipoIf != "logico"):
            print("Erro: Foi dado uma expressão do tipo -> '"+tipoIf+"', tipo esperado -> 'logica', para 'se' na função -> '"+self.escopo+"'")
            if (self.debug):
                exit(1)

        if (len(node.child) == 2):
            tipoCorpo = self.corpo(node.child[1])
            return tipoCorpo

        else:
            tipoCorpo1 = self.corpo(node.child[1])
            tipoCorpo2 = self.corpo(node.child[2])

            if (tipoCorpo1 != tipoCorpo2):
                if (tipoCorpo1 == "void"):
                    return tipoCorpo2
                else:
                    return tipoCorpo1

            return tipoCorpo1

    def opRelacional(self, node):
        return None

    def opSoma(self, node):
        return None

    def opMultiplicacao(self, node):
        return None

    def verificaFuncaoUtilizada(self, tabSimbolos):
        for escopoNome,conteudo in tabSimbolos.items():
            if((conteudo[0] == "funcao") and (escopoNome!="principal") and (conteudo[5]!=1)):
                print("Warning: Função '"+escopoNome+"' nunca é utilizada.")

    def verificaVarUtilizada(self, tabSimbolos):
        for escopoNome,conteudo in tabSimbolos.items():
            if((conteudo[0]=="variavel") and (conteudo[2]==False)):
                escopo = escopoNome.split("-")

                if(escopo[0]== "global"):
                    print("Warning: Variavel declarada '"+conteudo[1]+"' do escopo 'global' nunca é utilizada.")
                else:
                    print("Warning: Variavel declarada '"+conteudo[1]+"' da função '"+escopo[0]+"' nunca é utilizada.")

    def verificaDeclarPrincipal(self,tabSimbolos):
        if("principal" not in tabSimbolos.keys()):
            print("Erro: Função 'principal' não declarada.")
            if (self.debug):
                exit(1)

    def rchop(thestring, ending):
      if thestring.endswith(ending):
        return thestring[:-len(ending)]
      return thestring

if __name__ == '__main__':

    if(len(sys.argv) < 3):
        print("\nPadrão Esperado: Analisador_Semantico.py ARQUIVO_TESTE --debug=ON/OFF")
        print("\nEX: Analisador_Semantico.py semantica-testes/sema-001.tpp --debug=ON\n")
        exit(1)

    else:
        if((len(sys.argv) == 3) and (sys.argv[2] == "--debug=OFF")):
            As = Analisador_Semantico(sys.argv[1],True)

            print()
            print("_______________________________________________________________________")
            print("O Analisador Semantico Finalizou com Sucesso.\n")
            print("_______________________________________________________________________")
            print()

        elif((len(sys.argv) == 3 ) and (sys.argv[2] == "--debug=ON")):
            As = Analisador_Semantico(sys.argv[1],False)

            print()
            print("_______________________________________________________________________")
            print("O Analisador Semantico Finalizou com Sucesso.\n")
            print("_______________________________________________________________________")
            print()

            for escopoNome, conteudo in As.tabSimbolos.items():
                print(escopoNome,conteudo)
        else:
            print("\nPadrão Esperado: Analisador_Semantico.py ARQUIVO_TESTE --debug=ON/OFF")
            print("\nEX: Analisador_Semantico.py semantica-testes/sema-001.tpp --debug=ON\n")
            exit(1)
