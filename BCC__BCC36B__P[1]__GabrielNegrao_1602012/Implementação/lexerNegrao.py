# -----------------------------------------------------------------------------
# UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - UTFPR-CM
# Gabriel Negrão Silva - 1602012 - 12/09/2017
# Compiladores - Ciência Da Computação
# lexerNegrao.py
# -----------------------------------------------------------------------------

# Importação ply lexer
import ply.lex as lex
import sys

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
	'vazio' : 'VAZIO',
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
	'COMENTARIO'
] + list(reserved.values())

#Declaração das expressões regulares
t_SOMA = r'\+'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_IGUALDADE = r'\='
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
def t_NUMEROCIENTIFICO(t):
	r'[\d]+\.?[\d]*[Ee](?:[-+]?[\d]+)?'
	return t

def t_NUMERO(t):
	r'\d+(\.\d+)?'
	return t

def t_SUBTRACAO(t):
	r'\-'
	return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z-à-ú][_a-zA-Z_0-9-à-ú]*'
    t.type = reserved.get(t.value,'IDENTIFICADOR')
    return t

def t_COMENTARIO(t):
	r'\{[^}]*[^{]*\}'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Caracter Ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

def main():
	#abre o arquivo
	arq = open(sys.argv[1],'r')
	saida = open(sys.argv[1].replace(".tpp","")+"_Tokens.out", 'w')
	data = arq.read()

	lexer = lex.lex()

	#Atribui ao lexer o arquivo para tokenizar
	lexer.input(data)

	while 1:
		result = lexer.token()  #Tokeniza as strings de entrada
		if not result:
			break      # caso não houver entradas
		saida.write("<"+result.type+" , "+result.value+">\n")
	print("O Analisador Finalizou.")
	saida.close()
	arq.close()

#Define a execução pelo terminal
if __name__ == "__main__":
	main()
