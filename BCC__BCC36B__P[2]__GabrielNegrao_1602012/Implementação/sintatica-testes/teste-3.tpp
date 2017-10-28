{Gabriel Negrão Silva
Algoritmo de busca bolha em t++}

inteiro: vetor[1024]
inteiro: tam
tam:=1024

Bolha()
  inteiro: termino
  inteiro: i
  inteiro: aux

  i:= 0.0
  termino:= tamanho - 1

  repita
    repita
      se vetor[i] > vetor[i+1] então
        aux:= vetor[i]
        vetor[i]:= vetor[i+1]
        vetor[i+1]:= aux
        fim
      i:= i + 1
    até i < termino

    termino:= termino -1
  até termino > 0
fim

inteiro principal()
  escreva(Bolha())
  retorna(0)
fim
