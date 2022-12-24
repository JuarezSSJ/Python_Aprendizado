import tkinter as tk

janela = tk.Tk()

janela.title("Primeira tela")  # editar titulo

# para criar qualquer coisa no Tkinter primeiro temos que criar objeto, depois colocar o objeto dentro da janela

# mudar a cor da letra é foregroud e mudar a cor do label backgroud
mensagem = tk.Label(text="Olá Mundo!!!", bg="red", foreground="blue", width="30", height="5")

mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")  # metodo pack coloca a mensagem dentro da janela do tkinter disponivel

#row = linha e column = coluna 
# columnspan = informo quantas colunas eu quero que preencha tipo mesclar pensando igual ao excel
#sticky = metodo do grid para preencher, tem de informar para qual lado, NSEW = norte, sul, leste e oeste - iniciais da palavra em inglês

#depois de colocar qualquer mensagem ou item dentro da tela, ela se ajusta para o tamanho

mensagem2 = tk.Label(text="Criando minha primeira tela!!!", background="black", fg="white")
#pode ser usado bg = background e fg foreground

mensagem2.grid(row=1, column=0)

nome = tk.Entry() #aparece um label que permite digitar
nome.grid(row=1, column=1)

janela.mainloop()  # mainloop = loop infinito para deixar a tela visivel

nome.get()#pegar o que foi digitado