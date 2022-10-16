
a = int(input('Digite o valor a: ')) # o valor recebido no input sera string, converte para int
b = int(input('Digite o valor b: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print('soma: ' + str(soma)) # converte de int pra string
print('subtracao: {} \nmultiplicacao: {}' .format(subtracao, multiplicacao)) # usando format (na ordem em que chaves aparecem)
print('divisao: '+ str(int(divisao))) # converte de float para int e de int para string
print('resto: '+ str(resto))
print()
print('soma: {somaAlias} \nsubtração: {subtracao} \nmultiplicação: {multiplicacaoAlias} \ndivisão: {divisao} \nresto: {resto}'
    .format(resto=resto, multiplicacaoAlias=float(multiplicacao), divisao=divisao, somaAlias=soma, subtracao=subtracao))
    # usando format com elementos fora de ordem e alias