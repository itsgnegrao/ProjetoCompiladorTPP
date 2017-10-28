# -----------------------------------------------------------------------------
# UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - UTFPR-CM
# Gabriel Negrão Silva - 1602012 - 12/09/2017
# Compiladores - Ciência Da Computação
# Analisador_Lexico.py
# -----------------------------------------------------------------------------

import sys
import ply.lex as lex

class Analisador_Lexico:

    def __init__(self, name_arq=""):
        self.lexer = lex.lex(debug=False, module=self, optimize=False)
        self.build(name_arq)

    #Palavras reservadas
    reserved = {
    	'se' : 'SE',
    	'então' : 'ENTAO',
    	'senão' : 'SENAO',
    	'fim' : 'FIM',
    	'repita' : 'REPITA',
    	'flutuante' : 'FLUTUANTE',
    	'retorna' : 'RETORNA',
    	'leia' : 'LEIA',
    	'até' : 'ATE',
    	'escreva' : 'ESCREVA',
    	'inteiro' : 'INTEIRO',
    	'principal' : 'PRINCIPAL'
    }

    # Tokens
    tokens = [
    	'SOMA',
    	'SUBTRACAO',
    	'MULTIPLICACAO',
    	'DIVISAO',
    	'IGUALDADE',
    	'DIFERENTE',
    	'VIRGULA',
    	'ATRIBUICAO',
    	'MENOR',
    	'MAIOR',
    	'MENORIGUAL',
    	'MAIORIGUAL',
    	'ABREPAR',
    	'FECHAPAR',
    	'DOISPONTOS',
    	'ABRECOL',
    	'FECHACOL',
    	'ELOGICO',
    	'NEGACAO',
    	'NUMERO',
    	'NUMEROCIENTIFICO',
    	'IDENTIFICADOR',
    ] + list(reserved.values())

    #Declaração das expressões regulares
    t_SOMA = r'\+'
    t_MULTIPLICACAO = r'\*'
    t_DIVISAO = r'/'
    t_IGUALDADE = r'\='
    t_DIFERENTE = r'\<\>'
    t_VIRGULA = r'\,'
    t_ATRIBUICAO = r'\:\='
    t_MENOR = r'\<'
    t_MAIOR = r'\>'
    t_MENORIGUAL = r'\<\='
    t_MAIORIGUAL = r'\>\='
    t_ABREPAR = r'\('
    t_FECHAPAR = r'\)'
    t_DOISPONTOS = r'\:'
    t_ABRECOL = r'\['
    t_FECHACOL = r'\]'
    t_ELOGICO = r'\&\&'
    t_NEGACAO = r'\!'
    t_ignore = " \t"

    #Trata Numeros científicos
    def t_NUMEROCIENTIFICO(self,t):
    	r'[\d]+\.?[\d]*[Ee](?:[-+]?[\d]+)?'
    	return t

    def t_NUMERO(self,t):
    	r'\d+(\.\d+)?'
    	return t

    def t_SUBTRACAO(self,t):
    	r'\-'
    	return t

    def t_IDENTIFICADOR(self,t):
        r'[a-zA-Z-à-ú][_a-zA-Z_0-9-à-ú]*'
        t.type = self.reserved.get(t.value,'IDENTIFICADOR')
        return t

    def t_COMENTARIO(self,t):
    	r'\{[^}]*[^{]*\}'
    	pass

    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self,t):
        print("Caracter Ilegal '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self,name_arq):
        arq = open(name_arq,'r')
        saida = open(name_arq.replace(".tpp","_Tokens.out"), 'w')
        data = arq.read()

        #Atribui ao lexer (Análisador Léxico) o arquivo para tokenizar.
        lex.input(data)
        while 1:
        	result = lex.token()  #Tokeniza as strings de entrada

        	if not result:
        		break      # caso não houver entradas
        	saida.write("<"+result.type+" , "+result.value+">\n")

        saida.close()
        arq.close()


if __name__ == '__main__':
    Analisador_Lexico(sys.argv[1])
    print("_______________________________________________________________________")
    print("O Analisador Léxico Finalizou com Sucesso.\n")
    print("_______________________________________________________________________")
