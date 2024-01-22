from tkinter import *

# Selecionando cores

corDasBordas = "#000000"
corPreto = "#000000"
corBranco = "#ffffff"
corDosOperadoresPrincipais = "#f77925"

# Criando e Ajustando as Configurações da Janela Raíz

janela = Tk()
janela.title("Calculadora_V2")
janela.geometry("250x385")
janela.resizable(width=False, height=False)
janela.config(bg=corPreto)

# Criando Frame do Display

display = Frame(width=238, height=60)
display.grid(row=1, column=1)

# Criando Frames de Borda

bordaSuperior = Frame(width=238, height=5, bg=corDasBordas)
bordaSuperior.grid(row=0, column=1)

bordaEsquerda = Frame(width=5, height=60, bg=corDasBordas)
bordaEsquerda.grid(row=1, column=0)

bordaDireita = Frame(width=5, height=60, bg=corDasBordas)
bordaDireita.grid(row=1, column=2)

bordaInferior = Frame(width=228, height=5, bg=corDasBordas)
bordaInferior.grid(row=2, column=1)

entradas = Frame(width=240, height=310, bg=corBranco)
entradas.grid(row=3, column=1)

# Função para Capturar Valores

vals = ""
text_var = StringVar()


def capturando_valores(event):
    global vals
    vals = vals + str(event)
    text_var.set(vals)


# Função para Calcular o resultado da expressão

def calc():
    resultado = eval(vals)
    text_var.set(resultado)


# Função para Limpar o Display

def limpar():
    global vals
    vals = ""
    text_var.set("")


# Criando um Rótulo

saidaVals = Label(display, textvariable=text_var, width=16, height=3, bg=corPreto, fg="white")
saidaVals.config(padx=7, anchor='e', font="Ivy 18", relief="flat", justify="right")
saidaVals.place(x=0, y=0)

# Criando Botões

button_clear = Button(entradas, command=lambda: limpar(), text='C', width=6, height=3)
button_clear.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_clear.place(x=1, y=0)

button_trocarSinal = Button(entradas, command=lambda: capturando_valores("*(-1)"), text="+/-", width=6, height=3)
button_trocarSinal.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_trocarSinal.place(x=61, y=0)

button_restoDiv = Button(entradas, command=lambda: capturando_valores('%'), text='%', width=6, height=3)
button_restoDiv.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_restoDiv.place(x=121, y=0)

button_div = Button(entradas, command=lambda: capturando_valores('/'), text='/', width=6, height=3)
button_div.config(bg=corDosOperadoresPrincipais, font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_div.place(x=181, y=0)

button_7 = Button(entradas, command=lambda: capturando_valores('7'), text='7', width=6, height=3)
button_7.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_7.place(x=1, y=62)

button_8 = Button(entradas, command=lambda: capturando_valores('8'), text='8', width=6, height=3)
button_8.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_8.place(x=61, y=62)

button_9 = Button(entradas, command=lambda: capturando_valores('9'), text='9', width=6, height=3)
button_9.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_9.place(x=121, y=62)

button_mult = Button(entradas, command=lambda: capturando_valores('*'), text='*', width=6, height=3)
button_mult.config(bg=corDosOperadoresPrincipais, font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_mult.place(x=181, y=62)

button_4 = Button(entradas, command=lambda: capturando_valores('4'), text='4', width=6, height=3)
button_4.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_4.place(x=1, y=124)

button_5 = Button(entradas, command=lambda: capturando_valores('5'), text='5', width=6, height=3)
button_5.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_5.place(x=61, y=124)

button_6 = Button(entradas, command=lambda: capturando_valores('6'), text='6', width=6, height=3)
button_6.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_6.place(x=121, y=124)

button_sub = Button(entradas, command=lambda: capturando_valores('-'), text='-', width=6, height=3)
button_sub.config(bg=corDosOperadoresPrincipais, font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_sub.place(x=181, y=124)

button_1 = Button(entradas, command=lambda: capturando_valores('1'), text='1', width=6, height=3)
button_1.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_1.place(x=1, y=186)

button_2 = Button(entradas, command=lambda: capturando_valores('2'), text='2', width=6, height=3)
button_2.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_2.place(x=61, y=186)

buttom_3 = Button(entradas, command=lambda: capturando_valores('3'), text='3', width=6, height=3)
buttom_3.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
buttom_3.place(x=121, y=186)

button_soma = Button(entradas, command=lambda: capturando_valores('+'), text='+', width=6, height=3)
button_soma.config(bg=corDosOperadoresPrincipais, font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_soma.place(x=181, y=186)

button_0 = Button(entradas, command=lambda: capturando_valores('0'), text='0', width=13, height=3)
button_0.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_0.place(x=3, y=248)

button_pontoFlut = Button(entradas, command=lambda: capturando_valores('.'), text='.', width=6, height=3)
button_pontoFlut.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_pontoFlut.place(x=121, y=248)

button_igual = Button(entradas, command=lambda: calc(), text='=', width=6, height=3, bg=corDosOperadoresPrincipais)
button_igual.config(font="Ivy 10 bold", relief="raised", overrelief="ridge")
button_igual.place(x=181, y=248)

mainloop()
