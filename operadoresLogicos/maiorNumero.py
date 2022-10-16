# verificar entre dois valores qual é o maior

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c: 
    print('O maior numero é {}'.format(a))
    print('buuh') # tudo que estiver com indexação de um tab estará dentro do if
elif b > c and b > a:
    print('O maior numero é {}'.format(b))
else: 
    print('O maior numero é {}'.format(c))
print('aaahhhh')