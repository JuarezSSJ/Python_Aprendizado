import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

janela.title("Primeira tela")  # editar titulo
# o 0 seria a linha que estou configurando
janela.rowconfigure(0, weight=1)  # weight = 1 vai  ficar com altura automatica
# o [0,1] quando por ou mais de uma linha ou mais do que uma coluna deve passar como lista
janela.columnconfigure([0, 1], weight=1)
# para criar qualquer coisa no Tkinter primeiro temos que criar objeto, depois colocar o objeto dentro da janela

# mudar a cor da letra é foregroud e mudar a cor do label backgroud
mensagem = tk.Label(text="Olá Mundo!!!", bg="red",
                    foreground="blue", width="30", height="5")

# metodo pack coloca a mensagem dentro da janela do tkinter disponivel
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

# row = linha e column = coluna
# columnspan = informo quantas colunas eu quero que preencha tipo mesclar pensando igual ao excel
# sticky = metodo do grid para preencher, tem de informar para qual lado, NSEW = norte, sul, leste e oeste - iniciais da palavra em inglês

# depois de colocar qualquer mensagem ou item dentro da tela, ela se ajusta para o tamanho

mensagem2 = tk.Label(text="Criando minha primeira tela!!!",
                     background="black", fg="white")
# pode ser usado bg = background e fg foreground

mensagem2.grid(row=1, column=0)

# nome = tk.Entry() #aparece um label que permite digitar
# nome.grid(row=1, column=1)

mensagem3 = tk.Label(
    text="Caso queira pegar mais cotações ao mesmo tempo digite uma moeda em cada linha:")
mensagem3.grid(row=4, column=0, columnspan=2)


dicionario_cotacoes = {
    "Dólar": 5.50,
    "Euro": 6.70,
    "Bitcoin": 20000,
}

# pegar as chaves do dicionario e transformando em uma lista
moeda = list(dicionario_cotacoes.keys())
# criar uma lista para evitar que o usuario erre na digitação
moeda = ttk.Combobox(janela, values=moeda)
# Combobox (onde vai aparecer a lista, no caso na janela - Values o que terá na lista)
moeda.grid(row=1, column=1)


def mudarNome():
    # funçaõ no Tkinter tem acesso a tudo externo
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    # apos o click será criado um label para apresentar a mensagem para o usuario
    mensagem_cotacao = tk.Label(text="Cotação não encontrata")
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f"Cotação do {moeda_preenchida} é de {cotacao_moeda} reais"


botao = tk.Button(text="Mudar nome", command=mudarNome)
botao.grid(row=2, column=1)

caixa_texto = tk.Text(width=10, height=5)
caixa_texto.grid(row=5, column=0, sticky="nswe")


def buscarCotacoes():
    # criação da função para o botão:
    # quebrar o texto digitado na caixa de texto
    texto = caixa_texto.get("1.0", tk.END)
    # caixa_texto.get("1.0", tk.END) = 1 é a linha e o 0 é o primeiro caracter, tk.END é para pegar todo o texto digitado na caixa
    lista_moedas = texto.split("\n")
    # quebrar o texto em cada enter
    mensagem_lista = []
    # criação de uma lista vazia, com o obj. de colocar todas as cotações e depois criar somente um label
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_lista.append(f"{item}: {cotacao}")
            # append cadastra um item na lista
    mensagem4 = tk.Label(text="\n".join(mensagem_lista))
    mensagem4.grid(row=6, column=0)


botao_multi = tk.Button(text="Mudar nome", command=buscarCotacoes)
botao_multi.grid(row=5, column=1)


janela.mainloop()  # mainloop = loop infinito para deixar a tela visivel
