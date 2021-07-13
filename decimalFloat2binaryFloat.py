print("==== USE '.' E NÃO ',' =====")
decimal = float(input("digite o decimal float para transformar para binario: "))

#max 1024 e min 2^-18
res = 1024.0
binario = []
headers = []
binarioFinal = []
start = False
count = 0
numSignedExp = 0

#Faz a verificação do input do usuario, entre + ou -
if decimal < 0:
    signedDecimal = 1
    #evita trabalhar com num negativo no cod principal
    decimal *= -1
else:
    signedDecimal = 0

#firstADD - adiciona o sinal do numero no binario Final
binarioFinal.append(signedDecimal)


###############################################

#percorre do expoente 10 até o -18
for exp in range(10, -19, -1):
  #se o inputado - resultado do expoente > 0:  
  if decimal - res >= 0:
    decimal -= res
    start = True
    #a variavel start determina se o numero ja se iniciou (inicia no primeiro '1' dropado)
    if start:
      headers.append(exp)
      binario.append(1)
      #conta quantos digitos há depois do start ativado, a variavel foi criada pensando em como pegar o primeiro expoente ativado
      count +=1
      if start and count == 1:
        numSignedExp = exp
  else:
    if start:
      headers.append(exp)
      binario.append(0)
      count +=1
  #corta o resultadoExpoente por 2, para ir para o expoente anterior
  res /= 2


###############################################

#determina, por padrao somente, que o sinal do expoente é +
signedExp = 0

#Se o primeiro expoente for menor que 0:
if numSignedExp < 0:
  #o sinal do expoente se torna ativo (1)
  signedExp = 1
  #torna-se positivo para trabalhar com numero positivo
  numSignedExp *= -1

#coloca o sinal do expoente no binario Final 
binarioFinal.append(signedExp)


#Coloca o trecho de  4 binarios dentro do binario Final:
for i in range(3, -1, -1):
  aux = numSignedExp
  numSignedExp = numSignedExp - 2**i
  if numSignedExp < 0:
    binarioFinal.append(0)
    numSignedExp = aux
  else:
    binarioFinal.append(1)

#Escreve na tela desde o primeiro elemento até o ultimo contado da lista de binario
for i in range(0, count):
  numBin = binario[i]
  expoente = headers[i]
  print("Expoente --> {} || {}".format(expoente, numBin))

#esconde o primeiro digito 1 (natural da mantissa, pois trata-se de uma redundância)
del binario[0]

#Como o programa é em 16Bits, é necessário somente 10 digitos de mantissa, logo:
for i in range(0, 10):
  binarioFinal.append(binario[i])


print("\nResultado Final:\n")
print(binarioFinal)

#descomente essa linha para usar o programa no cmd:
#input()
