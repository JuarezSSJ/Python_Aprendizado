"""
Cadastro de CPF
Crie um programa para cadastro de CPF de clientes que recebe o CPF em um input box apenas com números.
Ex: 'Insira seu CPF (digite apenas números)'
Caso o usuário digite algo diferente de números ou digite menos de 11 caracteres (tamanho do CPF brasileiro),
 o programa deve exibir uma mensagem de "Digite seu CPF corretamente e digite apenas números"
"""

cpf = input("Insira seu CPF (digite apenas números): ")

#Tirar espaços desnecessarios digitados;
cpf = cpf.split() #essa função retira os espaços vazios tanto do inicio quanto do final

def verificar (cpf):
    for ver in cpf:
        if(ver == "-" or ver == "." or len(cpf) != 11 or cpf.isnumeric() == False):
            print("Digite seu CPF corretamente e digite apenas números")
            return False
            break
        else:
            print("CPF Cadastrado com sucesso!")
            return True
while (verificar(cpf) == False):
    cpf = str(input("Insira seu CPF (digite apenas números): "))
