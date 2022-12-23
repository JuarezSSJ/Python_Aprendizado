import tkinter as tk

janela = tk.Tk()

janela.title("Primeira tela")  # editar titulo

# para criar qualquer coisa no Tkinter primeiro temos que criar objeto, depois colocar o objeto dentro da janela

# mudar a cor da letra é foregroud e mudar a cor do label backgroud
mensagem = tk.Label(text="Olá Mundo!!!", foreground="green")

mensagem.pack()  # metodo pack coloca a mensagem dentro da janela do tkinter disponivel

#depois de colocar qualquer mensagem ou item dentro da tela, ela se ajusta para o tamanho

mensagem2 = tk.Label(text="Criando minha primeira tela!!!", background="black", fg="white", width="100", height="30")
#pode ser usado bg = background e fg foreground

mensagem2.pack()

janela.mainloop()  # mainloop = loop infinito para deixar a tela visivel
