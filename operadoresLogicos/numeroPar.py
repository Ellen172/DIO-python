# verificar se um dos numeros é par

a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

if a % 2 == 0 or not b % 2 > 0: # resto de b > 0 significa que o numero é impar
    print('Existe um número par')
else: 
    print('Não existe um número par')