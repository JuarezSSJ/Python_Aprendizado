import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

janela.title("Treinando Checkbox")

var_promocoes = tk.IntVar()

# criação de um checkbox = quando a caixa está marcada o valor é igual a 1
# quando está desmarcada o valor é igual a 0, por isso IntVar = valor inteiro
checkbox_promocoes = tk.Checkbutton(text="Deseja receber e-mail promocionais?", variable=var_promocoes)
# variable = serve para dizer para qual variavel deve ir o valor
checkbox_promocoes.grid(row=0, column=0)

var_politicas = tk.IntVar()



def enviar():
    # para print na tela, temos que trabalhar com .get() para ler e printar na tela
    print(var_promocoes.get())
    if var_promocoes.get(): # podemos fazer a comparação assim pois para o IF: True = 1 e False = 0
        print("Usuário deseja receber promoções")
    else:
        print("Usuário NÃO deseja receber promoções")

botao_enviar = tk.Button(text="Enviar", command=enviar)
botao_enviar.grid(row=1, column=0)


janela.mainloop()
