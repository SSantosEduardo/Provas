nome = input('digite o seu nome?: ')
idade = int(input('digite a sua idade: '))
email = input('digite o sei email: ')
cpf = input('digete o seu cpf: ')
endereço = input('digite seu endereço: ')
print(f''' Seja bem vindo {nome}, seu cadastro foi realizado com sucesso
      Confirme seua dados abaixo para prosseguir.
      seu nome é: {nome}
      sua idade é: {idade}
      seu email é: {email}
      seu CPF é: {cpf}
      seu endereço é: {endereço}''')
check = input('seus dados estao corretos?  ')
print(f'{check} Otimo finalizamos seu cadastro muito obrigado!!')
