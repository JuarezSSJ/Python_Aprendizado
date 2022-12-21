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
    if(func >= 1000):
        func = func * 1,1
    print("Seu salario é: R${}".format (func))


calculoMeta(vendas_funcionario1)
calculoMeta(vendas_funcionario2)
calculoMeta(vendas_funcionario3)