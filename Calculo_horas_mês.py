ganho_horas = float (input('Quanto você ganha por hora?:  '))
horas_trabalhadas = float (input('Quantas horas você trabalha por mês?:   '))
salario_bruto = ganho_horas*horas_trabalhadas
print(f'Seu salario bruto mensal é de: {salario_bruto}')
ir = salario_bruto * (11/100)
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
impostos = ir+inss+sindicato
salario_liquido = salario_bruto-impostos 
print(f'''
      salario bruto é de: {salario_bruto}
      IR (11%) é de: {ir}
      INSS (8%) é de: {inss}
      sindicato (5%) é de: {sindicato}
      Salario Liquido: {salario_liquido}''')

