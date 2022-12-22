"""
Cadastro de e-mails
A Hashtag sempre se comunica com seus clientes por e-mail. Para isso, a gente tem em cada página um cadastro de
nome e e-mail. Nesse cadastro, nosso sistema verifica se o e-mail que a pessoa inseriu é um e-mail válido,
verificando se ele tem '@' e se depois do '@' tem algum ponto, afinal:

liragmail.com NÃO é um e-mail - válido
lira@gmail NÃO é um e-mail válido
lira@gmail.com é um e-mail válido

Crie um programa que permita o cadastro de nome e e-mail de uma pessoa (por meio de inputs) e que verifique:
Se nome e e-mail foram preenchidos, caso contrário ele deve avisar para preencher todos os dados corretamente
Se o e-mail contém '@' e se depois do '@' existe algum '.', caso contrário ele deve exibir uma mensagem de e-mail
inválido
"""
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
def tratamento_nome (nome):
    if (len(nome) == 0):
        print("O campo nome não foi preenchido.")
        return True
    else:
        return False

def tratamento_email (email):
    posicao = email.find("@")
    servid = email[posicao:]
    if (servid.find(".") == -1):
        print("E-mail invalido: ")
        return True
    else:
        return False

while tratamento_nome(nome) == True:
    nome = input("Digite seu nome: ")

while tratamento_email(email) == True:
    email = input("Digite seu e-mail: ")

print("\n\n\tCadastro realizado com Sucesso\nNome: {}\nE-mail: {}".format(nome, email))
