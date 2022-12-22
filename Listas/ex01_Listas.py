emails = ["juarez@gmail.com",
          "juarezssj@gmail.com",
          "casa@gmail.com",
          "bola@hotmail.com",
          "fogo@furia.com",
          "gol@hotmail.com"]

#lista.append = funciona para cadastrar item na lista
#lista.index(item) = pesquisa na lista e informa qual o indice daquele item

print(emails)

#remomendo um item da lista
emails.remove("juarezssj@gmail.com")
print(emails)

#tamanho = len(lista) = informa o tamanho da lista

#lista1.extend(lista2) = modifica a lista1 colocando os item da lista2
#ou lista_nova = lista1 + lista2

#ordenarlista - lista.sort()
emails.sort()
print(emails)

#Print das listas
#método join = lista.join(separador)

print("\n".join(emails))

#separando um texto e transformando em lista

texto = "mesa, cadeira, fogão, bola, computador, loja, tela, tv"
lista_tratada = texto.split(", ")

print("\n",lista_tratada)