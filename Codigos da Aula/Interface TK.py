#Interface gráfica com Tkinter

from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title ("Minha Primeira Janela")#titulo.
janela.geometry ("500x500+400+70")#Tamanho da janela(Tam e Posição).
janela['bg']= "Maroon" #Muda a cor do fundo

#janela.minsize(200,200)#Tamanho min.
#janela.maxsize(600,600)#Tamanho max.
#janela.resizable(False, False)#bloqueio redicionamento da jamnela.
#janela.state("zoomed")#Começa maximizada
#janela.state("iconic")#Começa minimizada


def mensagem1():
    texto = txtnome.get()
    print(texto)
    1
def mensagem2():
    messagebox.showinfo("Informação", "Impossivel restaurar")
    
#messagebox.showwarning("Atenção", "Mensagem de atenção")
#messagebox.showerror("Erro", "Mensagem de erro")

#Adiciona um label(rótulo)
nome = Label (janela,text = "Nome", font = "Arial 20 bold", fg = "Gainsboro", bg = "Maroon");
nome.pack( pady=10)

#Adiciona caixa de texto
txtnome = Entry (janela, font = "Arial 20 bold", bg = "Brown", fg = "Gainsboro")
txtnome.pack(pady=10)

#Adiciona um botão
botao1 = Button (janela, text ="Envie", font = "Arial 20 bold", bg = "Brown", fg = "Gainsboro", command = mensagem1)
botao1.pack(pady=10)

botao2 = Button (janela, text ="Restaure", font = "Arial 20 bold", bg = "Brown", fg = "Gainsboro", command = mensagem2)
botao2.pack(pady=10)

janela.mainloop()

