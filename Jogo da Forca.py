import requests
from tkinter import *

def jogar():

 palavra = "perfume"
 letras_usuario = []
 chances = 4
 ganhou = False


 while True:
    # criando a logica do jogo
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"você tem {chances} chances")
    tentativa = input("Escolha uma letra para advinhar: ")
    letras_usuario.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou:
        break
 if ganhou:
    print(f"Parabéns, você ganhou. A palavra era: {palavra}")
 else:
    print(f"você perdeu! A palavra era: {palavra}")



janela = Tk()
janela.title("Jogo da Forca")

texto_orientacao = Label(janela, text="Clique no botão para começar a jogar")
texto_orientacao.grid(column=0, row=0)

botao = Button(janela, text="Começar a Jogar", command=jogar)
botao.grid(column=0, row=1)

janela.mainloop()
