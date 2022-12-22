"""
Recebendo uma lista de e-mail e localizando os respectivos servidores de e-mail
"""

emails = ["juarez@gmail.com",
          "juarez@gmail.com",
          "casa@gmail.com",
          "bola@hotmail.com",
          "fogo@furia.com",
          "gol@hotmail.com"]

servidor_email = []
#email = str(input("Digite seu e-mail: "))

def servidores (email_cliente):
    a=0
    email=""
    for posicao in email_cliente:
        a+=1
        if (posicao == "@"):
            break
    email = email_cliente[a:]
    return email
#Servidores dos e-mail dos clientes
for x in emails:
    print(servidores(x))

"""
Segunda forma utilizando um método
"""

for seg in emails:
    a=seg.find("@")+1
    #print(seg[a:])
    servidor_email.append(seg[a:])

#list(set(lista)) - serve para remover valores duplicados

#print(list(set(servidor_email)))

for serv in list(set(servidor_email)):
    servidor_1 = 0
    for base in servidor_email:
        if serv in base:
            servidor_1+=1
    print("Servidor {} repetiu {} vezes na lista\n".format(serv, servidor_1))
