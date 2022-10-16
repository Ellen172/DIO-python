# fazer a media da nota do aluno, recebendo as notas de cada bimestre, 
# e validar se valores estão corretos

nota1 = int(input('Insira a nota do 1º bimestre: '))
if nota1 > 10: 
    nota1 = int(input('Nota incorreta. Insira a nota do 1º bimestre: '))

nota2 = int(input('Insira a nota do 2º bimestre: '))
if nota2 > 10: 
    nota2 = int(input('Nota incorreta. Insira a nota do 2º bimestre: '))

nota3 = int(input('Insira a nota do 3º bimestre: '))
if nota3 > 10: 
    nota3 = int(input('Nota incorreta. Insira a nota do 3º bimestre: '))

nota4 = int(input('Insira a nota do 4º bimestre: '))
if nota4 > 10: 
    nota4 = int(input('Nota incorreta. Insira a nota do 14º bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('media = {}'.format(media))