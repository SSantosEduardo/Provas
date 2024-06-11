numero_correto = 5
tentativa = 0

print('Bem vindo voce tem 3 tentativas para acertar o numero correto entre 1 e 10. Boa sorte!!')

while tentativa <=2:
    tentativa += 1
    usuario = int(input('Digite um numero:  '))

    if usuario != numero_correto:
        print('Continue tentando')
        print(f'{tentativa} Tentativa ja era!! Cuidado...')
    
    elif usuario == numero_correto:
        print('Parabens voce acertou!')
        break
    
    if tentativa > 2:
        print(f'Não foi dessa vez o numero correto era o {numero_correto}, tente novamente!!')