# -*- coding: utf-8 -*-
"""Desenvolvimento de Sistemas II - Exercício de Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LRlftrfYBK7vCvs59x8w7JdTa8pkYgHJ
"""

dic_cliente = {}
dic_movimento = {}

def menu():
  print("\n=======================================")
  print("\t\tBANCO SENAI")
  print("=======================================\n")
  print("1 – Cadastro de CLIENTES")
  print("2 – DEPÓSITOS")
  print("3 – SAQUES")
  print("4 – SALDO")
  print("5 – Sair")
  opcao = int(input("– Digite a opção desejada: "))
  return opcao

def cadastro_novo(lista, nome, conta, telefone):
  lista.append(conta)
  lista.append(nome)
  lista.append(telefone)

def cadastro_disc(cadastro, cpf, lista):
  cadastro[cpf] = lista

def cadastro_movimentacao(dic_movimento, conta):
  saldo = 0.00
  dic_movimento[conta] = saldo

def cadastro_cliente():
  while True:
    cliente = []
    cpf = int(input("Digite seu CPF: "))
    conta = input("Digite sua conta: ")
    nome = input("Digite seu nome: ")
    telefone = input("Digite seu telefone: ")

    cadastro_novo(cliente, nome, conta, telefone)
    cadastro_disc(dic_cliente, cpf, cliente)
    cadastro_movimentacao(dic_movimento, conta)

    mais_cadastro = input("\nDeseja cadastrar outro Cliente: S/N: ")
    if (mais_cadastro == "N"):
      break

def deposito(dic_cliente, dic_movimento):
  while True:
    if dic_cliente == {}:
      print("\nNão existem CLIENTES cadastrados. Cadastre pelo menos 1 cliente")
    while True:
      cpf_verificar = int(input("Digite seu CPF: "))
      if cpf_verificar in dic_cliente.keys():
        print("\nSeja bem-vindo\n")
        print("Nome do Cliente: ", dic_cliente[cpf_verificar][1])
        conta = dic_cliente[cpf_verificar][0]
        print("Saldo: R$", dic_movimento[conta])
        break
      else:
        print("CPF Invalido, favor digitar outro CPF\n")
    valor_deposito = float(input("\nDigite o valor a ser depositado: R$"))
    conta = dic_cliente[cpf_verificar][0]
    valor_em_conta = dic_movimento[conta]
    dic_movimento[conta] = valor_deposito + valor_em_conta
    print("Deposito realizado com sucesso!\n")
    mais_depositos = input("\nDeseja realizar outro deposito - S/N: ")
    if (mais_depositos == "N"):
      break
  #print(dic_movimento)

def saque(dic_cliente, dic_movimento):
  while True:
    if dic_cliente == {}:
      print("\nNão existem CLIENTES cadastrados. Cadastre pelo menos 1 cliente")
    while True:
      cpf_verificar = int(input("Digite seu CPF: "))
      if cpf_verificar in dic_cliente.keys():
        print("\nSeja bem-vindo\n")
        print("Nome do Cliente: ", dic_cliente[cpf_verificar][1])
        conta = dic_cliente[cpf_verificar][0]
        print("Saldo: R$", dic_movimento[conta])
        break
      else:
        print("CPF Invalido, favor digitar outro CPF\n")
    valor_saque = float(input("\nDigite o valor a ser sacado: R$"))
    conta = dic_cliente[cpf_verificar][0]
    
    if dic_movimento[conta] >= valor_saque:
      transacao = dic_movimento[conta]
      dic_movimento[conta] = transacao - valor_saque
      print("Saque realizado com Sucesso")
    else:
      print("Saldo indisponível!")
      print("Seu saldo é R$", dic_movimento[conta])
    mais_saques = input("\nDeseja realizar outro saque - S/N: ")
    if (mais_saques == "N"):
      break

def saldo(dic_cliente, dic_movimento):
  if dic_cliente == {}:
    print("Não existem CLIENTES cadastrados. Cadastre pelo menos 1 cliente")
  for chave in dic_cliente:
    print("\nCPF do CLIENTE: ", chave)
    print("Nome do Cliente: ", dic_cliente[chave][1])
    conta = dic_cliente[chave][0]
    print("Saldo: R$", dic_movimento[conta])

while True:
  opcao = menu()
  if opcao == 1:
    cadastro_cliente()
  elif opcao == 2:
    deposito(dic_cliente, dic_movimento)
  elif opcao == 3:
    saque(dic_cliente, dic_movimento)
  elif opcao == 4:
    saldo(dic_cliente, dic_movimento)
  elif opcao == 5:
    print("\n\nVOLTE SEMPRE!!!",)
    break
  else:
      print("\nOpção inválida.\n")

lista_contas = []
listas_valores = []
for chave in dic_movimento:
  lista_contas = chave
  listas_valores = dic_movimento[chave]
print(lista_contas)
print(listas_valores)

#teste
#deposito(dic_cliente)
cliente_test = ["1452-6", "Simone de Castro Albuquerque", "71-91552-9999"]
cliente_test1 = ["1452-6", "Luis", "71-91552-9999"]
cliente_test2 = ["1452-6", "carlos", "71-91552-9999"]
#dic_cliente_test= {45678625877: cliente_test, 4: cliente_test1, 45: cliente_test2}
dic_movimento_test= {"1452-6": 100.0, "1011-2": 200.0, "1234-5": 150.0}
#cpf2 = 45678625877
#for chave in dic_cliente_test:
#  print(dic_cliente_test[chave][1])
#deposito(dic_cliente_test, dic_movimento_test)
#saque(dic_cliente_test, dic_movimento_test)
#saldo(dic_cliente_test, dic_movimento_test)
#print(dic_cliente_test [cpf2][0])
lista_contas = []
listas_valores = []
for chave in dic_movimento_test:
  lista_contas = chave
  listas_valores = dic_movimento_test[chave]
lista_contas = dic_movimento_test.keys()
print(lista_contas)
print(listas_valores)