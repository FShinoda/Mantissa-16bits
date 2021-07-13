
print("==== FAVOR NÃO DIGITAR '.' ENTRE OS DIGITOS BINARIOS =====\n")
binario = int(input("Digite o numero em binario float para descobrir seu decimal: "))

#Exemplos: 

# 1000011010101010 = -3.33203125 
# 1100101010000000 = -0.40625
# 0001111110000010 = 240.25
# 0100110101110100 = 0.170410156 

binListNeg = []
# Inicia-se com 1 pois é aquele '1' redundante que fica escondido no binario original.
binListPos = [1]
divisor = 1000000000000000
digito = 0
numAnt = 0
numDps = 0
numTotal = 0

#Vai do 1 até 16 por se tratar de um conversor 16BITS!!
#O for abaixo, pega digito por digito e adiciona em binListNeg que na verdade é a Mantissa.
for i in range(1, 17):
  if i == 1:
    digito = binario // divisor
    binListNeg.append(digito)
  else:
    digito = binario // divisor % 10
    binListNeg.append(digito)
  
  divisor = divisor // 10


# verifica o primeiro digito que corresponde ao numero final ser pos ou neg.
if binListNeg[0] == 1:
  sinalFinal = -1
elif binListNeg[0] == 0:
  sinalFinal = 1

# Verifica o sinal do expoente, para saber pra onde se moverao os numeros.
if binListNeg[1] == 1:
  sinalExp = -1
elif binListNeg[1] == 0:
  sinalExp = 1

# o expoente convertido para decimal:
expoente = binListNeg[2]*8 + binListNeg[3]*4 + binListNeg[4]*2 + binListNeg[5]*1

# deleta os numeros de 0 até 5 (6 digitos) pois queremos apenas a mantissa agora.
del binListNeg[0:6]

# Movimenta os digitos binarios para antes ou depois da virgula dependendo do sinal e do nr do expoente
if sinalExp < 0:
  # Digamos que "vai para a Direita", o numero diminui e os digitos vão para a mantissa; depois da virgula.
  for i in range(expoente):
    if len(binListPos) > 0:
      binListNeg.insert(0, binListPos[0])
      del binListPos[0]
    else:
      binListNeg.insert(0, 0)
else:
  # Digamos que "vai para a Esquerda", o numero aumenta e os digitos vão para de trás da virgula.
  for i in range(expoente):
    binListPos.append(binListNeg[0])
    del binListNeg[0]

#Se não houver nada dentro da lista de numeros antes da virgula, ele adiciona um '0'. É só para visualização.
if len(binListPos) == 0:
  binListPos.append(0)


print("{} || {}".format(binListPos, binListNeg))

#Inverte a lista que corresponde ao valor inteiro, pois é preciso manipular essa lista de forma espelhada.
binListPos.reverse()

#Faz todo o calculo do valor inteiro e da parte decimal, de acordo com um range determinado pelo length das listas.
for i in range(0, len(binListPos)):
  
  numAnt += (2**i) * binListPos[i]

for j in range(1, len(binListNeg)+1):
  exp = -j
  numDps += 2**exp * binListNeg[j-1]
  print(2**exp * binListNeg[j-1])
  

#soma o valor inteiro com o decimal feitos acima e depois multiplica pelo sinal que descobrimos na ln34
numTotal = (numAnt + numDps) * sinalFinal

print("\nRESULTADO =", numTotal)






