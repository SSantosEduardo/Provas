minimo = 0 
maximo = 10
validos = 1,2,3,4,5,6,7,8,9,10
while True:
    valor = int(input('Digite umm valor entre 0 e 10:  '))
    
    if valor == validos:
        print('Valor valido')
    
    elif valor < minimo:
        print('valor menor que o necessario, tente novamente')
    
    elif valor > maximo:
        print('valor maior que o necessario, tente novamente')