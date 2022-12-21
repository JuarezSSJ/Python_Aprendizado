"""
Cálculo de Bônus*/
Crie um programa que calcule e dê um print no bônus que os funcionários devem receber segundo a regra:
A meta é 1000 vendas.
Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas.
Caso contrário o valor de bônus do funcionário é 0.
Print o bônus dos 3 funcionários
"""
vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

def calculoMeta (func):
    if(func >= 2000):
        func = func * 0.15
    elif(func < 2000 and func >= 1000):
        func = func * 0.1
    else:
        func = 0
    print("Seu bônos é: R${}".format (func))


calculoMeta(vendas_funcionario1)
calculoMeta(vendas_funcionario2)
calculoMeta(vendas_funcionario3)

"""
Cálculo de bônus com uma nova regra
Agora, crie um novo código que calcule e dê um print no bônus dos funcionários novamente. Porém há uma nova regra nesse 2º caso:
A meta é 1000 vendas
Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:

Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas
Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas
Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0.
Use as mesmas variáveis de vendas_funcionários
"""