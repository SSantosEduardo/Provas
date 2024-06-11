numero_secreto = 25
tentativas_maximas = 5
tentaivas = 0

while tentaivas != numero_secreto and tentativas_maximas > 0:
    tentativa = int(input('Tente adivinhar o numero entre 1 e 40: '))
    tentativas_maximas -= 1
    if tentaivas != numero_secreto:
        print(f'Tentativas restantes: {tentativas_maximas}')
    
    if tentativa == numero_secreto:
        print('Parabens chefe voce acertou!')
        break

    elif tentativa < numero_secreto:
        print('Chutou muito baixo meu patrão tenta de novo ai...')

    elif tentativa > numero_secreto:
        print('Agora voce chutou muito alto irmao abaixa isso ai...')