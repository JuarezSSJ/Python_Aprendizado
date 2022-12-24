import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

janela.title("Primeira tela")  # editar titulo
                # o 0 seria a linha que estou configurando
janela.rowconfigure(0, weight=1 )#weight = 1 vai  ficar com altura automatica
                # o [0,1] quando por ou mais de uma linha ou mais do que uma coluna deve passar como lista
janela.columnconfigure([0,1], weight=1)
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

# nome = tk.Entry() #aparece um label que permite digitar
# nome.grid(row=1, column=1)

dicionario_cotacoes = {
    "Dólar": 5.50,
    "Euro": 6.70,
    "Bitcoin": 20000,
}

#pegar as chaves do dicionario e transformando em uma lista
moeda = list(dicionario_cotacoes.keys())
#criar uma lista para evitar que o usuario erre na digitação
moeda = ttk.Combobox(janela, values = moeda)
# Combobox (onde vai aparecer a lista, no caso na janela - Values o que terá na lista)
moeda.grid(row=1, column=1)

def mudarNome():
    #funçaõ no Tkinter tem acesso a tudo externo
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    # apos o click será criado um label para apresentar a mensagem para o usuario
    mensagem_cotacao = tk.Label(text="Cotação não encontrata")
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f"Cotação do {moeda_preenchida} é de {cotacao_moeda} reais"
    

botao = tk.Button(text="Mudar nome", command= mudarNome)
botao.grid(row=2, column=1)

janela.mainloop()  # mainloop = loop infinito para deixar a tela visivel

nome.get()#pegar o que foi digitado