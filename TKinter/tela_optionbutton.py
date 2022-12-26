import tkinter as tk


janela = tk.Tk()

janela.title("Criando Option Button")

dicionario_cotacoes = {
    "Dólar": 5.50,
    "Euro": 6.70,
    "Bitcoin": 20000,
}

mensagem = tk.Label(text="Escolha a moeda: ")
mensagem.grid(row=0, column=0, columnspan=3)

# por definição o Radiobutton quando criado já vem marcado
# para resolver isso temos que passar um valor para a variavel (value="Nada"), resolve isso
var_moeda = tk.StringVar(value="Nada")

mensagem_cotacao = tk.Label(text="")
mensagem_cotacao.grid(row=3, column=0, columnspan=3)


def enviar():
    # print(var_moeda.get())
    moeda_preenchida = var_moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    # apos o click será criado um label para apresentar a mensagem para o usuario
    if cotacao_moeda:
        mensagem_cotacao["text"] = f"Cotação do {moeda_preenchida} é de {cotacao_moeda} reais"


botao_euro = tk.Radiobutton(
    text="Euro", variable=var_moeda, value="Euro", command=enviar)
botao_dolar = tk.Radiobutton(
    text="Dólar", variable=var_moeda, value="Dólar", command=enviar)
botao_bitcoin = tk.Radiobutton(
    text="Bitcoin", variable=var_moeda, value="Bitcoin", command=enviar)
botao_euro.grid(row=1, column=0)
botao_dolar.grid(row=1, column=1)
botao_bitcoin.grid(row=1, column=2)


janela.mainloop()
