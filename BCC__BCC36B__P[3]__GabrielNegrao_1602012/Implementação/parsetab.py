
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIGUALDADEMAIORIGUALMAIORMENORIGUALMENORleftSOMASUBTRACAOleftMULTIPLICACAODIVISAOSOMA SUBTRACAO MULTIPLICACAO DIVISAO IGUALDADE DIFERENTE VIRGULA ATRIBUICAO MENOR MAIOR MENORIGUAL MAIORIGUAL ABREPAR FECHAPAR DOISPONTOS ABRECOL FECHACOL ELOGICO NEGACAO NUMERO NUMEROCIENTIFICO IDENTIFICADOR ATE LEIA ESCREVA SE SENAO FIM REPITA INTEIRO PRINCIPAL ENTAO RETORNA FLUTUANTEprograma : lista_declaracoeslista_declaracoes : lista_declaracoes declaracao\n    \t\t\t\t\t\t | declaracao declaracao : declaracao_variaveis\n    \t\t\t\t\t| inicializacao_variaveis\n    \t\t\t\t\t| declaracao_funcao declaracao_variaveis : tipo DOISPONTOS lista_variaveis inicializacao_variaveis : atribuicao atribuicao : var ATRIBUICAO expressao  lista_variaveis : lista_variaveis VIRGULA var\n    \t\t\t\t\t\t| var  var : IDENTIFICADOR\n    \t\t\t| IDENTIFICADOR indice  indice : indice ABRECOL expressao FECHACOL\n    \t\t\t\t| ABRECOL expressao FECHACOLtipo : INTEIROtipo : FLUTUANTE declaracao_funcao : tipo cabecalho\n    \t\t\t\t\t\t  | cabecalho  cabecalho : IDENTIFICADOR ABREPAR lista_parametros FECHAPAR corpo FIM\n    \t\t\t\t  | PRINCIPAL ABREPAR lista_parametros FECHAPAR corpo FIM lista_parametros : lista_parametros VIRGULA parametro\n    \t\t\t\t\t\t | parametro\n                             | vazio parametro : tipo DOISPONTOS IDENTIFICADOR  parametro : parametro ABRECOL FECHACOL  corpo : corpo acao\n    \t\t\t  | vazioacao : expressao\n    \t\t\t| declaracao_variaveis\n    \t\t\t| se\n    \t\t\t| repita\n    \t\t\t| leia\n    \t\t\t| escreva\n    \t\t\t| retorna\n    \t\t\t| error  se : SE expressao ENTAO corpo FIM\n    \t\t   | SE expressao ENTAO corpo SENAO corpo FIM  repita : REPITA corpo ATE expressao  leia : LEIA ABREPAR IDENTIFICADOR FECHAPAR  escreva : ESCREVA ABREPAR expressao FECHAPAR retorna : RETORNA ABREPAR expressao FECHAPARexpressao : expressao_simples\n                     | atribuicao  expressao_simples : expressao_aditiva\n    \t\t\t\t\t\t  | expressao_simples operador_relacional expressao_aditiva expressao_aditiva : expressao_multiplicativa\n    \t\t\t\t\t\t  | expressao_aditiva operador_soma expressao_multiplicativa  expressao_multiplicativa : expressao_unaria\n    \t\t\t\t\t\t\t\t | expressao_multiplicativa operador_multiplicacao expressao_unaria  expressao_unaria : fator\n    \t\t\t\t\t\t | operador_soma fator operador_relacional : MENOR\n    \t\t\t\t\t\t\t| MAIOR\n    \t\t\t\t\t\t\t| IGUALDADE\n    \t\t\t\t\t\t\t| DIFERENTE\n    \t\t\t\t\t\t\t| MENORIGUAL\n    \t\t\t\t\t\t\t| MAIORIGUAL\n    \t\t\t\t\t\t\t| NEGACAO\n    \t\t\t\t\t\t\t| ELOGICO operador_soma : SOMA\n    \t\t\t\t\t  | SUBTRACAO operador_multiplicacao : MULTIPLICACAO\n    \t\t\t\t\t\t\t  | DIVISAO fator : ABREPAR expressao FECHAPAR\n    \t\t\t | var\n    \t\t\t | chamada_funcao\n    \t\t\t | numeronumero : NUMERO\n    \t\t\t  | NUMEROCIENTIFICOchamada_funcao : IDENTIFICADOR ABREPAR lista_argumentos FECHAPAR\n                          | PRINCIPAL ABREPAR lista_argumentos FECHAPARlista_argumentos  : lista_argumentos VIRGULA expressao\n    \t\t\t\t\t\t| expressao\n                            | vaziovazio :'
    
_lr_action_items = {'ELOGICO':([20,33,34,35,36,39,40,41,42,44,48,49,62,72,73,84,85,86,91,92,110,112,],[-13,-49,-69,-45,-67,-68,-12,-70,-66,66,-47,-51,-15,-66,-52,-14,-65,-48,-46,-50,-72,-71,]),'DIFERENTE':([20,33,34,35,36,39,40,41,42,44,48,49,62,72,73,84,85,86,91,92,110,112,],[-13,-49,-69,-45,-67,-68,-12,-70,-66,68,-47,-51,-15,-66,-52,-14,-65,-48,-46,-50,-72,-71,]),'REPITA':([20,24,25,26,33,34,35,36,39,40,41,42,44,47,48,49,51,54,62,72,73,77,78,80,81,84,85,86,91,92,93,94,95,98,99,100,101,102,103,107,108,110,112,114,121,125,126,127,128,129,130,131,132,133,],[-13,-12,-7,-11,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,-9,-76,-15,-66,-52,-76,-10,-28,94,-14,-65,-48,-46,-50,94,-76,-31,-30,-29,-32,-35,-33,-27,-36,-34,-72,-71,94,-76,-39,94,-40,-42,-41,-37,-76,94,-38,]),'MENOR':([20,33,34,35,36,39,40,41,42,44,48,49,62,72,73,84,85,86,91,92,110,112,],[-13,-49,-69,-45,-67,-68,-12,-70,-66,63,-47,-51,-15,-66,-52,-14,-65,-48,-46,-50,-72,-71,]),'ABREPAR':([9,10,17,20,21,23,24,25,26,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,51,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,91,92,93,94,95,96,97,98,99,100,101,102,103,106,107,108,109,110,111,112,114,117,118,120,121,125,126,127,128,129,130,131,132,133,],[19,22,19,-13,32,32,-12,-7,-11,32,32,-49,-69,-45,-67,60,-61,-68,61,-70,-66,-43,32,-62,-44,-47,-51,-9,-76,32,32,32,-15,-53,-55,32,-60,-57,-56,-58,-54,-59,-66,-52,-64,32,-63,-76,-10,-28,32,-14,-65,-48,-46,-50,32,-76,-31,32,116,-30,-29,-32,-35,-33,-27,117,-36,-34,118,-72,32,-71,32,32,32,32,-76,-39,32,-40,-42,-41,-37,-76,32,-38,]),'NUMERO':([20,21,23,24,25,26,31,32,33,34,35,36,38,39,40,41,42,44,45,46,47,48,49,51,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,91,92,93,94,95,96,98,99,100,101,102,103,107,108,110,111,112,114,117,118,120,121,125,126,127,128,129,130,131,132,133,],[-13,34,34,-12,-7,-11,34,34,-49,-69,-45,-67,-61,-68,-12,-70,-66,-43,34,-62,-44,-47,-51,-9,-76,34,34,34,-15,-53,-55,34,-60,-57,-56,-58,-54,-59,-66,-52,-64,34,-63,-76,-10,-28,34,-14,-65,-48,-46,-50,34,-76,-31,34,-30,-29,-32,-35,-33,-27,-36,-34,-72,34,-71,34,34,34,34,-76,-39,34,-40,-42,-41,-37,-76,34,-38,]),'MULTIPLICACAO':([20,33,34,36,39,40,41,42,48,49,62,72,73,84,85,86,92,110,112,],[-13,-49,-69,-67,-68,-12,-70,-66,76,-51,-15,-66,-52,-14,-65,76,-50,-72,-71,]),'FECHACOL':([20,33,34,35,36,39,40,41,42,43,44,47,48,49,51,56,57,62,72,73,84,85,86,91,92,110,112,],[-13,-49,-69,-45,-67,-68,-12,-70,-66,62,-43,-44,-47,-51,-9,83,84,-15,-66,-52,-14,-65,-48,-46,-50,-72,-71,]),'INTEIRO':([0,3,4,6,7,8,11,14,15,16,19,20,22,24,25,26,33,34,35,36,39,40,41,42,44,47,48,49,51,54,55,62,72,73,77,78,80,81,84,85,86,91,92,93,94,95,98,99,100,101,102,103,104,107,108,110,112,113,114,121,125,126,127,128,129,130,131,132,133,],[1,-8,1,-4,-19,-3,-6,-5,-2,-18,1,-13,1,-12,-7,-11,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,-9,-76,1,-15,-66,-52,-76,-10,-28,1,-14,-65,-48,-46,-50,1,-76,-31,-30,-29,-32,-35,-33,-27,-20,-36,-34,-72,-71,-21,1,-76,-39,1,-40,-42,-41,-37,-76,1,-38,]),'FIM':([20,24,25,26,33,34,35,36,39,40,41,42,44,47,48,49,51,54,62,72,73,77,78,80,81,84,85,86,91,92,93,95,98,99,100,101,102,103,107,108,110,112,121,125,126,127,128,129,130,131,132,133,],[-13,-12,-7,-11,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,-9,-76,-15,-66,-52,-76,-10,-28,104,-14,-65,-48,-46,-50,113,-31,-30,-29,-32,-35,-33,-27,-36,-34,-72,-71,-76,-39,130,-40,-42,-41,-37,-76,133,-38,]),'IGUALDADE':([20,33,34,35,36,39,40,41,42,44,48,49,62,72,73,84,85,86,91,92,110,112,],[-13,-49,-69,-45,-67,-68,-12,-70,-66,64,-47,-51,-15,-66,-52,-14,-65,-48,-46,-50,-72,-71,]),'SE':([20,24,25,26,33,34,35,36,39,40,41,42,44,47,48,49,51,54,62,72,73,77,78,80,81,84,85,86,91,92,93,94,95,98,99,100,101,102,103,107,108,110,112,114,121,125,126,127,128,129,130,131,132,133,],[-13,-12,-7,-11,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,-9,-76,-15,-66,-52,-76,-10,-28,96,-14,-65,-48,-46,-50,96,-76,-31,-30,-29,-32,-35,-33,-27,-36,-34,-72,-71,96,-76,-39,96,-40,-42,-41,-37,-76,96,-38,]),'ATRIBUICAO':([9,12,20,40,42,62,84,],[-12,23,-13,-12,23,-15,-14,]),'NEGACAO':([20,33,34,35,36,39,40,41,42,44,48,49,62,72,73,84,85,86,91,92,110,112,],[-13,-49,-69,-45,-67,-68,-12,-70,-66,71,-47,-51,-15,-66,-52,-14,-65,-48,-46,-50,-72,-71,]),'FLUTUANTE':([0,3,4,6,7,8,11,14,15,16,19,20,22,24,25,26,33,34,35,36,39,40,41,42,44,47,48,49,51,54,55,62,72,73,77,78,80,81,84,85,86,91,92,93,94,95,98,99,100,101,102,103,104,107,108,110,112,113,114,121,125,126,127,128,129,130,131,132,133,],[13,-8,13,-4,-19,-3,-6,-5,-2,-18,13,-13,13,-12,-7,-11,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,-9,-76,13,-15,-66,-52,-76,-10,-28,13,-14,-65,-48,-46,-50,13,-76,-31,-30,-29,-32,-35,-33,-27,-20,-36,-34,-72,-71,-21,13,-76,-39,13,-40,-42,-41,-37,-76,13,-38,]),'VIRGULA':([19,20,22,24,25,26,28,29,30,33,34,35,36,39,40,41,42,44,47,48,49,50,51,60,61,62,72,73,78,79,82,83,84,85,86,87,88,89,90,91,92,110,112,119,],[-76,-13,-76,-12,52,-11,55,-24,-23,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,55,-9,-76,-76,-15,-66,-52,-10,-25,-22,-26,-14,-65,-48,111,-75,-74,111,-46,-50,-72,-71,-73,]),'ESCREVA':([20,24,25,26,33,34,35,36,39,40,41,42,44,47,48,49,51,54,62,72,73,77,78,80,81,84,85,86,91,92,93,94,95,98,99,100,101,102,103,107,108,110,112,114,121,125,126,127,128,129,130,131,132,133,],[-13,-12,-7,-11,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,-9,-76,-15,-66,-52,-76,-10,-28,109,-14,-65,-48,-46,-50,109,-76,-31,-30,-29,-32,-35,-33,-27,-36,-34,-72,-71,109,-76,-39,109,-40,-42,-41,-37,-76,109,-38,]),'PRINCIPAL':([0,1,3,4,5,6,7,8,11,13,14,15,16,20,21,23,24,25,26,31,32,33,34,35,36,38,39,40,41,42,44,45,46,47,48,49,51,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,91,92,93,94,95,96,98,99,100,101,102,103,104,107,108,110,111,112,113,114,117,118,120,121,125,126,127,128,129,130,131,132,133,],[10,-16,-8,10,10,-4,-19,-3,-6,-17,-5,-2,-18,-13,37,37,-12,-7,-11,37,37,-49,-69,-45,-67,-61,-68,-12,-70,-66,-43,37,-62,-44,-47,-51,-9,-76,37,37,37,-15,-53,-55,37,-60,-57,-56,-58,-54,-59,-66,-52,-64,37,-63,-76,-10,-28,37,-14,-65,-48,-46,-50,37,-76,-31,37,-30,-29,-32,-35,-33,-27,-20,-36,-34,-72,37,-71,-21,37,37,37,37,-76,-39,37,-40,-42,-41,-37,-76,37,-38,]),'DOISPONTOS':([1,5,13,27,105,],[-16,18,-17,53,18,]),'LEIA':([20,24,25,26,33,34,35,36,39,40,41,42,44,47,48,49,51,54,62,72,73,77,78,80,81,84,85,86,91,92,93,94,95,98,99,100,101,102,103,107,108,110,112,114,121,125,126,127,128,129,130,131,132,133,],[-13,-12,-7,-11,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,-9,-76,-15,-66,-52,-76,-10,-28,97,-14,-65,-48,-46,-50,97,-76,-31,-30,-29,-32,-35,-33,-27,-36,-34,-72,-71,97,-76,-39,97,-40,-42,-41,-37,-76,97,-38,]),'MAIOR':([20,33,34,35,36,39,40,41,42,44,48,49,62,72,73,84,85,86,91,92,110,112,],[-13,-49,-69,-45,-67,-68,-12,-70,-66,70,-47,-51,-15,-66,-52,-14,-65,-48,-46,-50,-72,-71,]),'FECHAPAR':([19,20,22,28,29,30,33,34,35,36,39,40,41,42,44,47,48,49,50,51,58,60,61,62,72,73,79,82,83,84,85,86,87,88,89,90,91,92,110,112,119,122,123,124,],[-76,-13,-76,54,-24,-23,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,77,-9,85,-76,-76,-15,-66,-52,-25,-22,-26,-14,-65,-48,110,-75,-74,112,-46,-50,-72,-71,-73,127,128,129,]),'RETORNA':([20,24,25,26,33,34,35,36,39,40,41,42,44,47,48,49,51,54,62,72,73,77,78,80,81,84,85,86,91,92,93,94,95,98,99,100,101,102,103,107,108,110,112,114,121,125,126,127,128,129,130,131,132,133,],[-13,-12,-7,-11,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,-9,-76,-15,-66,-52,-76,-10,-28,106,-14,-65,-48,-46,-50,106,-76,-31,-30,-29,-32,-35,-33,-27,-36,-34,-72,-71,106,-76,-39,106,-40,-42,-41,-37,-76,106,-38,]),'error':([20,24,25,26,33,34,35,36,39,40,41,42,44,47,48,49,51,54,62,72,73,77,78,80,81,84,85,86,91,92,93,94,95,98,99,100,101,102,103,107,108,110,112,114,121,125,126,127,128,129,130,131,132,133,],[-13,-12,-7,-11,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,-9,-76,-15,-66,-52,-76,-10,-28,107,-14,-65,-48,-46,-50,107,-76,-31,-30,-29,-32,-35,-33,-27,-36,-34,-72,-71,107,-76,-39,107,-40,-42,-41,-37,-76,107,-38,]),'IDENTIFICADOR':([0,1,3,4,5,6,7,8,11,13,14,15,16,18,20,21,23,24,25,26,31,32,33,34,35,36,38,39,40,41,42,44,45,46,47,48,49,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,91,92,93,94,95,96,98,99,100,101,102,103,104,107,108,110,111,112,113,114,116,117,118,120,121,125,126,127,128,129,130,131,132,133,],[9,-16,-8,9,17,-4,-19,-3,-6,-17,-5,-2,-18,24,-13,40,40,-12,-7,-11,40,40,-49,-69,-45,-67,-61,-68,-12,-70,-66,-43,40,-62,-44,-47,-51,-9,24,79,-76,40,40,40,-15,-53,-55,40,-60,-57,-56,-58,-54,-59,-66,-52,-64,40,-63,-76,-10,-28,40,-14,-65,-48,-46,-50,40,-76,-31,40,-30,-29,-32,-35,-33,-27,-20,-36,-34,-72,40,-71,-21,40,122,40,40,40,-76,-39,40,-40,-42,-41,-37,-76,40,-38,]),'SENAO':([20,24,25,26,33,34,35,36,39,40,41,42,44,47,48,49,51,62,72,73,78,80,84,85,86,91,92,95,98,99,100,101,102,103,107,108,110,112,121,125,126,127,128,129,130,133,],[-13,-12,-7,-11,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,-9,-15,-66,-52,-10,-28,-14,-65,-48,-46,-50,-31,-30,-29,-32,-35,-33,-27,-36,-34,-72,-71,-76,-39,131,-40,-42,-41,-37,-38,]),'MAIORIGUAL':([20,33,34,35,36,39,40,41,42,44,48,49,62,72,73,84,85,86,91,92,110,112,],[-13,-49,-69,-45,-67,-68,-12,-70,-66,69,-47,-51,-15,-66,-52,-14,-65,-48,-46,-50,-72,-71,]),'ATE':([20,24,25,26,33,34,35,36,39,40,41,42,44,47,48,49,51,62,72,73,78,80,84,85,86,91,92,94,95,98,99,100,101,102,103,107,108,110,112,114,125,127,128,129,130,133,],[-13,-12,-7,-11,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,-9,-15,-66,-52,-10,-28,-14,-65,-48,-46,-50,-76,-31,-30,-29,-32,-35,-33,-27,-36,-34,-72,-71,120,-39,-40,-42,-41,-37,-38,]),'SOMA':([20,21,23,24,25,26,31,32,33,34,35,36,38,39,40,41,42,44,46,47,48,49,51,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,91,92,93,94,95,96,98,99,100,101,102,103,107,108,110,111,112,114,117,118,120,121,125,126,127,128,129,130,131,132,133,],[-13,38,38,-12,-7,-11,38,38,-49,-69,38,-67,-61,-68,-12,-70,-66,-43,-62,-44,-47,-51,-9,-76,38,38,38,-15,-53,-55,38,-60,-57,-56,-58,-54,-59,-66,-52,-64,38,-63,-76,-10,-28,38,-14,-65,-48,38,-50,38,-76,-31,38,-30,-29,-32,-35,-33,-27,-36,-34,-72,38,-71,38,38,38,38,-76,-39,38,-40,-42,-41,-37,-76,38,-38,]),'ABRECOL':([9,20,24,30,40,62,79,82,83,84,],[21,31,21,56,21,-15,-25,56,-26,-14,]),'SUBTRACAO':([20,21,23,24,25,26,31,32,33,34,35,36,38,39,40,41,42,44,46,47,48,49,51,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,91,92,93,94,95,96,98,99,100,101,102,103,107,108,110,111,112,114,117,118,120,121,125,126,127,128,129,130,131,132,133,],[-13,46,46,-12,-7,-11,46,46,-49,-69,46,-67,-61,-68,-12,-70,-66,-43,-62,-44,-47,-51,-9,-76,46,46,46,-15,-53,-55,46,-60,-57,-56,-58,-54,-59,-66,-52,-64,46,-63,-76,-10,-28,46,-14,-65,-48,46,-50,46,-76,-31,46,-30,-29,-32,-35,-33,-27,-36,-34,-72,46,-71,46,46,46,46,-76,-39,46,-40,-42,-41,-37,-76,46,-38,]),'MENORIGUAL':([20,33,34,35,36,39,40,41,42,44,48,49,62,72,73,84,85,86,91,92,110,112,],[-13,-49,-69,-45,-67,-68,-12,-70,-66,67,-47,-51,-15,-66,-52,-14,-65,-48,-46,-50,-72,-71,]),'DIVISAO':([20,33,34,36,39,40,41,42,48,49,62,72,73,84,85,86,92,110,112,],[-13,-49,-69,-67,-68,-12,-70,-66,74,-51,-15,-66,-52,-14,-65,74,-50,-72,-71,]),'$end':([2,3,4,6,7,8,11,14,15,16,20,24,25,26,33,34,35,36,39,40,41,42,44,47,48,49,51,62,72,73,78,84,85,86,91,92,104,110,112,113,],[0,-8,-1,-4,-19,-3,-6,-5,-2,-18,-13,-12,-7,-11,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,-9,-15,-66,-52,-10,-14,-65,-48,-46,-50,-20,-72,-71,-21,]),'NUMEROCIENTIFICO':([20,21,23,24,25,26,31,32,33,34,35,36,38,39,40,41,42,44,45,46,47,48,49,51,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,84,85,86,91,92,93,94,95,96,98,99,100,101,102,103,107,108,110,111,112,114,117,118,120,121,125,126,127,128,129,130,131,132,133,],[-13,41,41,-12,-7,-11,41,41,-49,-69,-45,-67,-61,-68,-12,-70,-66,-43,41,-62,-44,-47,-51,-9,-76,41,41,41,-15,-53,-55,41,-60,-57,-56,-58,-54,-59,-66,-52,-64,41,-63,-76,-10,-28,41,-14,-65,-48,-46,-50,41,-76,-31,41,-30,-29,-32,-35,-33,-27,-36,-34,-72,41,-71,41,41,41,41,-76,-39,41,-40,-42,-41,-37,-76,41,-38,]),'ENTAO':([20,33,34,35,36,39,40,41,42,44,47,48,49,51,62,72,73,84,85,86,91,92,110,112,115,],[-13,-49,-69,-45,-67,-68,-12,-70,-66,-43,-44,-47,-51,-9,-15,-66,-52,-14,-65,-48,-46,-50,-72,-71,121,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'numero':([21,23,31,32,45,59,60,61,65,75,81,93,96,111,114,117,118,120,126,132,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'expressao_unaria':([21,23,31,32,59,60,61,65,75,81,93,96,111,114,117,118,120,126,132,],[33,33,33,33,33,33,33,33,92,33,33,33,33,33,33,33,33,33,33,]),'corpo':([54,77,94,121,131,],[81,93,114,126,132,]),'acao':([81,93,114,126,132,],[103,103,103,103,103,]),'indice':([9,24,40,],[20,20,20,]),'se':([81,93,114,126,132,],[95,95,95,95,95,]),'lista_variaveis':([18,],[25,]),'lista_argumentos':([60,61,],[87,90,]),'programa':([0,],[2,]),'expressao_aditiva':([21,23,31,32,60,61,65,81,93,96,111,114,117,118,120,126,132,],[35,35,35,35,35,35,91,35,35,35,35,35,35,35,35,35,35,]),'atribuicao':([0,4,21,23,31,32,60,61,81,93,96,111,114,117,118,120,126,132,],[3,3,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'operador_relacional':([44,],[65,]),'vazio':([19,22,54,60,61,77,94,121,131,],[29,29,80,88,88,80,80,80,80,]),'parametro':([19,22,55,],[30,30,82,]),'chamada_funcao':([21,23,31,32,45,59,60,61,65,75,81,93,96,111,114,117,118,120,126,132,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'lista_declaracoes':([0,],[4,]),'tipo':([0,4,19,22,55,81,93,114,126,132,],[5,5,27,27,27,105,105,105,105,105,]),'declaracao_variaveis':([0,4,81,93,114,126,132,],[6,6,98,98,98,98,98,]),'leia':([81,93,114,126,132,],[102,102,102,102,102,]),'cabecalho':([0,4,5,],[7,7,16,]),'escreva':([81,93,114,126,132,],[108,108,108,108,108,]),'declaracao':([0,4,],[8,15,]),'retorna':([81,93,114,126,132,],[101,101,101,101,101,]),'expressao':([21,23,31,32,60,61,81,93,96,111,114,117,118,120,126,132,],[43,51,57,58,89,89,99,99,115,119,99,123,124,125,99,99,]),'repita':([81,93,114,126,132,],[100,100,100,100,100,]),'declaracao_funcao':([0,4,],[11,11,]),'var':([0,4,18,21,23,31,32,45,52,59,60,61,65,75,81,93,96,111,114,117,118,120,126,132,],[12,12,26,42,42,42,42,72,78,72,42,42,72,72,42,42,42,42,42,42,42,42,42,42,]),'lista_parametros':([19,22,],[28,50,]),'expressao_simples':([21,23,31,32,60,61,81,93,96,111,114,117,118,120,126,132,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'operador_multiplicacao':([48,86,],[75,75,]),'operador_soma':([21,23,31,32,35,59,60,61,65,75,81,91,93,96,111,114,117,118,120,126,132,],[45,45,45,45,59,45,45,45,45,45,45,59,45,45,45,45,45,45,45,45,45,]),'inicializacao_variaveis':([0,4,],[14,14,]),'expressao_multiplicativa':([21,23,31,32,59,60,61,65,81,93,96,111,114,117,118,120,126,132,],[48,48,48,48,86,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'fator':([21,23,31,32,45,59,60,61,65,75,81,93,96,111,114,117,118,120,126,132,],[49,49,49,49,73,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa','Analisador_Sintatico.py',42),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','Analisador_Sintatico.py',46),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','Analisador_Sintatico.py',47),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','Analisador_Sintatico.py',54),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','Analisador_Sintatico.py',55),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','Analisador_Sintatico.py',56),
  ('declaracao_variaveis -> tipo DOISPONTOS lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','Analisador_Sintatico.py',60),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','Analisador_Sintatico.py',64),
  ('atribuicao -> var ATRIBUICAO expressao','atribuicao',3,'p_atribuicao','Analisador_Sintatico.py',68),
  ('lista_variaveis -> lista_variaveis VIRGULA var','lista_variaveis',3,'p_lista_variaveis','Analisador_Sintatico.py',72),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis','Analisador_Sintatico.py',73),
  ('var -> IDENTIFICADOR','var',1,'p_var','Analisador_Sintatico.py',80),
  ('var -> IDENTIFICADOR indice','var',2,'p_var','Analisador_Sintatico.py',81),
  ('indice -> indice ABRECOL expressao FECHACOL','indice',4,'p_indice','Analisador_Sintatico.py',88),
  ('indice -> ABRECOL expressao FECHACOL','indice',3,'p_indice','Analisador_Sintatico.py',89),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','Analisador_Sintatico.py',96),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo2','Analisador_Sintatico.py',100),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_declaracao_funcao','Analisador_Sintatico.py',104),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_declaracao_funcao','Analisador_Sintatico.py',105),
  ('cabecalho -> IDENTIFICADOR ABREPAR lista_parametros FECHAPAR corpo FIM','cabecalho',6,'p_cabecalho','Analisador_Sintatico.py',112),
  ('cabecalho -> PRINCIPAL ABREPAR lista_parametros FECHAPAR corpo FIM','cabecalho',6,'p_cabecalho','Analisador_Sintatico.py',113),
  ('lista_parametros -> lista_parametros VIRGULA parametro','lista_parametros',3,'p_lista_parametros','Analisador_Sintatico.py',117),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','Analisador_Sintatico.py',118),
  ('lista_parametros -> vazio','lista_parametros',1,'p_lista_parametros','Analisador_Sintatico.py',119),
  ('parametro -> tipo DOISPONTOS IDENTIFICADOR','parametro',3,'p_parametro','Analisador_Sintatico.py',126),
  ('parametro -> parametro ABRECOL FECHACOL','parametro',3,'p_parametro2','Analisador_Sintatico.py',130),
  ('corpo -> corpo acao','corpo',2,'p_corpo','Analisador_Sintatico.py',134),
  ('corpo -> vazio','corpo',1,'p_corpo','Analisador_Sintatico.py',135),
  ('acao -> expressao','acao',1,'p_acao','Analisador_Sintatico.py',142),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','Analisador_Sintatico.py',143),
  ('acao -> se','acao',1,'p_acao','Analisador_Sintatico.py',144),
  ('acao -> repita','acao',1,'p_acao','Analisador_Sintatico.py',145),
  ('acao -> leia','acao',1,'p_acao','Analisador_Sintatico.py',146),
  ('acao -> escreva','acao',1,'p_acao','Analisador_Sintatico.py',147),
  ('acao -> retorna','acao',1,'p_acao','Analisador_Sintatico.py',148),
  ('acao -> error','acao',1,'p_acao','Analisador_Sintatico.py',149),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','Analisador_Sintatico.py',153),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se','Analisador_Sintatico.py',154),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','Analisador_Sintatico.py',161),
  ('leia -> LEIA ABREPAR IDENTIFICADOR FECHAPAR','leia',4,'p_leia','Analisador_Sintatico.py',166),
  ('escreva -> ESCREVA ABREPAR expressao FECHAPAR','escreva',4,'p_escreva','Analisador_Sintatico.py',170),
  ('retorna -> RETORNA ABREPAR expressao FECHAPAR','retorna',4,'p_retorna','Analisador_Sintatico.py',174),
  ('expressao -> expressao_simples','expressao',1,'p_expressao','Analisador_Sintatico.py',178),
  ('expressao -> atribuicao','expressao',1,'p_expressao','Analisador_Sintatico.py',179),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','Analisador_Sintatico.py',183),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','Analisador_Sintatico.py',184),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','Analisador_Sintatico.py',191),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_expressao_aditiva','Analisador_Sintatico.py',192),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','Analisador_Sintatico.py',199),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','Analisador_Sintatico.py',200),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','Analisador_Sintatico.py',207),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria','Analisador_Sintatico.py',208),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','Analisador_Sintatico.py',215),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operador_relacional','Analisador_Sintatico.py',216),
  ('operador_relacional -> IGUALDADE','operador_relacional',1,'p_operador_relacional','Analisador_Sintatico.py',217),
  ('operador_relacional -> DIFERENTE','operador_relacional',1,'p_operador_relacional','Analisador_Sintatico.py',218),
  ('operador_relacional -> MENORIGUAL','operador_relacional',1,'p_operador_relacional','Analisador_Sintatico.py',219),
  ('operador_relacional -> MAIORIGUAL','operador_relacional',1,'p_operador_relacional','Analisador_Sintatico.py',220),
  ('operador_relacional -> NEGACAO','operador_relacional',1,'p_operador_relacional','Analisador_Sintatico.py',221),
  ('operador_relacional -> ELOGICO','operador_relacional',1,'p_operador_relacional','Analisador_Sintatico.py',222),
  ('operador_soma -> SOMA','operador_soma',1,'p_operador_soma','Analisador_Sintatico.py',226),
  ('operador_soma -> SUBTRACAO','operador_soma',1,'p_operador_soma','Analisador_Sintatico.py',227),
  ('operador_multiplicacao -> MULTIPLICACAO','operador_multiplicacao',1,'p_operador_multiplicacao','Analisador_Sintatico.py',231),
  ('operador_multiplicacao -> DIVISAO','operador_multiplicacao',1,'p_operador_multiplicacao','Analisador_Sintatico.py',232),
  ('fator -> ABREPAR expressao FECHAPAR','fator',3,'p_fator','Analisador_Sintatico.py',236),
  ('fator -> var','fator',1,'p_fator','Analisador_Sintatico.py',237),
  ('fator -> chamada_funcao','fator',1,'p_fator','Analisador_Sintatico.py',238),
  ('fator -> numero','fator',1,'p_fator','Analisador_Sintatico.py',239),
  ('numero -> NUMERO','numero',1,'p_numero','Analisador_Sintatico.py',246),
  ('numero -> NUMEROCIENTIFICO','numero',1,'p_numero','Analisador_Sintatico.py',247),
  ('chamada_funcao -> IDENTIFICADOR ABREPAR lista_argumentos FECHAPAR','chamada_funcao',4,'p_chamada_funcao','Analisador_Sintatico.py',251),
  ('chamada_funcao -> PRINCIPAL ABREPAR lista_argumentos FECHAPAR','chamada_funcao',4,'p_chamada_funcao','Analisador_Sintatico.py',252),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','Analisador_Sintatico.py',256),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','Analisador_Sintatico.py',257),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_lista_argumentos','Analisador_Sintatico.py',258),
  ('vazio -> <empty>','vazio',0,'p_vazio','Analisador_Sintatico.py',274),
]
