nota_1b = float(input('Digite a nota do 1b: '))
nota_2b = float(input('Digite a nota do 2b: '))
media = (nota_1b + nota_2b) /2
print(f'Sua media total foi de: {media}, segue resultado a baixo.')
if media == 10:
    print('Aprovado com destinção')
elif media >= 7:
    print('Aprovado. Parabens!!')
elif media < 7:
    print('Reprovado')
