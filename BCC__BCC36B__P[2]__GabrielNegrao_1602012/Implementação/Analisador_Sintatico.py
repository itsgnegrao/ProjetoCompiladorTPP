# -----------------------------------------------------------------------------
# UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - UTFPR-CM
# Gabriel Negrão Silva - 1602012 - 12/09/2017
# Compiladores - Ciência Da Computação
# lexerNegrao.py
# -----------------------------------------------------------------------------

# Importação ply lexer
from graphviz import Graph
import ply.yacc as yacc
from Analisador_Lexico import Analisador_Lexico
import sys
import os

class Tree:

    def __init__(self, type_node='', child=[], value=''):
        self.type = type_node
        self.child = child
        self.value = value

    def __str__(self):
        return self.type


class Analisador_Sintatico:

    def __init__(self, code):
        al = Analisador_Lexico(sys.argv[1])
        self.tokens = al.tokens
        self.precedence = (
            ('left', 'IGUALDADE', 'MAIORIGUAL', 'MAIOR', 'MENORIGUAL', 'MENOR'),
            ('left', 'SOMA', 'SUBTRACAO'),
            ('left', 'MULTIPLICACAO', 'DIVISAO'),
        )
        arq = open(code,'r')
        data = arq.read()
        parser = yacc.yacc(debug=False, module=self, optimize=False)
        self.ast = parser.parse(data)

    def p_programa(self,p):
        '''programa : lista_declaracoes'''
        p[0] = Tree('programa', [p[1]])

    def p_lista_declaracoes(self,p):
        '''lista_declaracoes : lista_declaracoes declaracao
    						 | declaracao'''
        if len(p) == 3:
            p[0] = Tree('lista_declaracoes', [p[1], p[2]])
        elif len(p) == 2:
            p[0] = Tree('lista_declaracoes', [p[1]])

    def p_declaracao(self,p):
        ''' declaracao : declaracao_variaveis
    					| inicializacao_variaveis
    					| declaracao_funcao '''
        p[0] = Tree('declaracao',[p[1]])

    def p_declaracao_variaveis(self,p):
        '''declaracao_variaveis : tipo DOISPONTOS lista_variaveis'''
        p[0] = Tree('declaracao_variaveis', [p[1], p[3]])

    def p_inicializacao_variaveis(self,p):
        ''' inicializacao_variaveis : atribuicao '''
        p[0] = Tree('inicializacao_variaveis', [p[1]])

    def p_atribuicao(self,p):
        '''atribuicao : var ATRIBUICAO expressao '''
        p[0] = Tree('atribuicao', [p[1],p[3]])

    def p_lista_variaveis(self,p):
        ''' lista_variaveis : lista_variaveis VIRGULA var
    						| var '''
        if len(p) == 4:
            p[0] = Tree('lista_variaveis', [p[1], p[3]])
        elif len(p) == 2:
            p[0] = Tree('lista_variaveis', [p[1]])

    def p_var(self,p):
        ''' var : IDENTIFICADOR
    			| IDENTIFICADOR indice '''
        if len(p) == 2:
            p[0] = Tree('var', [], p[1])
        elif len(p) == 3:
            p[0] = Tree('var', [p[2]], p[1])

    def p_indice(self,p):
        ''' indice : indice ABRECOL expressao FECHACOL
    				| ABRECOL expressao FECHACOL'''
        if len(p) == 5:
            p[0] = Tree('indice', [p[1], p[3]])
        elif len(p) == 4:
            p[0] = Tree('indice', [p[2]])

    def p_tipo(self,p):
        '''tipo : INTEIRO
    			| FLUTUANTE'''
        p[0] = Tree('tipo')

    def p_declaracao_funcao(self,p):
        ''' declaracao_funcao : tipo cabecalho
    						  | cabecalho '''
        if len(p) == 3:
            p[0] = Tree('declaracao_funcao', [p[1], p[2]])
        elif len(p) == 2:
            p[0] = Tree('declaracao_funcao', [p[1]])

    def p_cabecalho(self,p):
        ''' cabecalho : IDENTIFICADOR ABREPAR lista_parametros FECHAPAR corpo FIM
    				  | PRINCIPAL ABREPAR lista_parametros FECHAPAR corpo FIM'''
        if p[1] == 'PRINCIPAL':
            print("ola")
        p[0] = Tree('cabecalho', [p[3], p[5]], p[1])

    def p_lista_parametros(self,p):
        ''' lista_parametros : lista_parametros VIRGULA parametro
    						 | parametro
                             | vazio'''
        if len(p) == 4:
            p[0] = Tree('lista_parametros', [p[1], p[3]])
        elif len(p) == 2:
            p[0] = Tree('lista_parametros', [p[1]])

    def p_parametro(self,p):
        ''' parametro : tipo DOISPONTOS IDENTIFICADOR
    				  |  parametro ABRECOL FECHACOL '''
        p[0] = Tree('parametro', [p[1]], p[3])

    def p_corpo(self,p):
        ''' corpo : corpo acao
    			  | vazio'''
        if len(p) == 3:
            p[0] = Tree('corpo', [p[1], p[2]])
        elif len(p) == 2:
            p[0] = Tree('corpo', [p[1]])

    def p_acao(self,p):
        '''acao : expressao
    			| declaracao_variaveis
    			| se
    			| repita
    			| leia
    			| escreva
    			| retorna
    			| error '''
        p[0] = Tree('acao', [p[1]])

    def p_se(self,p):
        ''' se : SE expressao ENTAO corpo FIM
    		   | SE expressao ENTAO corpo SENAO corpo FIM '''
        if len(p) == 6:
            p[0] = Tree('se', [p[2], p[4]])
        elif len(p) == 8:
            p[0] = Tree('se', [p[2], p[4], p[6]])

    def p_repita(self,p):
        ''' repita : REPITA corpo ATE expressao '''
        p[0] = Tree('repita', [p[2], p[4]])


    def p_leia(self,p):
        ''' leia : LEIA ABREPAR IDENTIFICADOR FECHAPAR '''
        p[0] = Tree('leia', [], p[3])

    def p_escreva(self,p):
        ''' escreva : ESCREVA ABREPAR expressao FECHAPAR
    				| ESCREVA ABREPAR chamada_funcao FECHAPAR'''
        p[0] = Tree('escreva', [], p[3])

    def p_retorna(self,p):
        ''' retorna : RETORNA ABREPAR expressao FECHAPAR'''
        p[0] = Tree('retorna', [p[3]])

    def p_expressao(self, p):
        '''expressao : expressao_simples
                     | atribuicao '''
        p[0] = Tree('expressao', [p[1]])

    def p_expressao_simples(self,p):
        ''' expressao_simples : expressao_aditiva
    						  | expressao_simples operador_relacional expressao_aditiva'''
        if len(p) == 2:
            p[0] = Tree('expressao_simples', [p[1]])
        elif len(p) == 4:
            p[0] = Tree('expressao_simples', [p[1], p[2], p[3]])

    def p_expressao_aditiva(self,p):
        ''' expressao_aditiva : expressao_multiplicativa
    						  | expressao_aditiva operador_soma expressao_multiplicativa '''
        if len(p) == 2:
            p[0] = Tree('expressao_aditiva', [p[1]])
        elif len(p) == 4:
            p[0] = Tree('expressao_aditiva', [p[1], p[2], p[3]])

    def p_expressao_multiplicativa(self,p):
        ''' expressao_multiplicativa : expressao_unaria
    								 | expressao_multiplicativa operador_multiplicacao expressao_unaria '''
        if len(p) == 2:
            p[0] = Tree('expressao_multiplicativa', [p[1]])
        elif len(p) == 4:
            p[0] = Tree('expressao_multiplicativa', [p[1], p[2], p[3]])

    def p_expressao_unaria(self,p):
        ''' expressao_unaria : fator
    						 | operador_soma fator'''
        if len(p) == 2:
            p[0] = Tree('expressao_unaria', [p[1]])
        elif len(p) == 3:
            p[0] = Tree('expressao_unaria', [p[1], p[2]])

    def p_operador_relacional(self,p):
        ''' operador_relacional : MENOR
    							| MAIOR
    							| IGUALDADE
    							| DIFERENTE
    							| MENORIGUAL
    							| MAIORIGUAL
    							| NEGACAO
    							| ELOGICO'''
        p[0] = Tree('operador_relacional', [])

    def p_operador_soma(self,p):
        ''' operador_soma : SOMA
    					  | SUBTRACAO '''
        p[0] = Tree('operador_soma', [])

    def p_operador_multiplicacao(self,p):
        '''operador_multiplicacao : MULTIPLICACAO
    							  | DIVISAO '''
        p[0] = Tree('operador_multiplicacao', [])

    def p_fator(self,p):
        '''fator : ABREPAR expressao FECHAPAR
    			 | var
    			 | chamada_funcao
    			 | numero'''
        if len(p) == 4:
            p[0] = Tree('fator', [p[2]])
        elif len(p) == 2:
            p[0] = Tree('fator', [p[1]])

    def p_numero(self,p):
        '''numero : NUMERO
    			  | NUMEROCIENTIFICO'''
        p[0] = Tree('numero', [], p[1])

    def p_chamada_funcao(self,p):
        '''chamada_funcao : IDENTIFICADOR ABREPAR lista_argumentos FECHAPAR'''
        p[0] = Tree('chamada_funcao', [p[3]], p[1])

    def p_lista_argumentos(self,p):
        '''lista_argumentos  : lista_argumentos VIRGULA expressao
    						| expressao
                            | vazio'''
        if len(p) == 4:
            p[0] = Tree('lista_argumentos', [p[1], p[3]])
        elif len(p) == 2:
            p[0] = Tree('lista_argumentos', [p[1]])

    def p_error(self,p):
    	if p:
    		print("Erro sintático: '%s', linha %d" % (p.value, p.lineno))
    		exit(1)
    	else:
    		yacc.restart()
    		print("Erro sintático: definições incompletas!")
    		exit(1)

    def p_vazio(self,p):
        'vazio :'
        pass


    def teste():
        #Teste para o uso do Graphviz na geração da imagem da Arvore final.
        print("_______________________________________________________________________")
        print("Inicio do Teste do Graphviz utilizado para plotagem da árvore.")

        print("Testando..")
        tst = Graph('The Round Table',format='png')
        tst.edges(['AB', 'AC'])
        tst.edge('B', 'J')

        print("Salvando imagem..")
        tst.render('tst1')

        print("Limpando o Teste..")
        os.system("rm -rf tst1.png")
        os.system("rm -rf tst1")

        print("Teste Concluído com Sucesso!")
        print("_______________________________________________________________________")



def print_tree(node, level="-"):
    if node != None:
        print("%s %s %s" %(level, node.type, node.value))
        for son in node.child:
            print_tree(son, level+"-")

if __name__ == '__main__':
    Analisador_Sintatico.teste()
    f = Analisador_Sintatico(sys.argv[1])

    #inicia a arvore sintatica de saída
    g = Graph('Arvore Sintatica',format='png')
    #salvando imagem da arvore sintatica.
    g.render('ArvoreSintatica')

    print("_______________________________________________________________________")
    print("O Analisador Sintático Finalizou com Sucesso.\n")
    print("_______________________________________________________________________")
    print_tree(f.ast)
