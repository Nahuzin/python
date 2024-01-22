from tkinter import *

janela = Tk()
# print(Tk().configure().keys())

corJanela = "black"
corDisplay = "#445359"
corADireita = "#f0842b"
corFonteADireita = "white"

janela.title("Calculadora")  # Definindo título
janela.geometry("235x275")  # Definindo tamanho da janela raíz
janela.config(background=corJanela)  # Definindo cor de fundo da janela raíz

# Criando Frames

display = Frame(janela, width=235, height=50)
display.grid(row=0, column=0)

entradas = Frame(janela, width=235, height=268)
entradas.grid(row=1, column=0)

# Variavel vals

vals = ""

valor_texto = StringVar()


# Criando Função
def inserir_valores(event):
    global vals

    vals = vals + str(event)

    # Passando valor para tela
    valor_texto.set(vals)


# Função para mostrar o resultado

def calcular():
    resultado = eval(vals)
    valor_texto.set(resultado)


# Função para limpar o display

def limparDisplay():
    global vals
    vals = ""
    valor_texto.set("")


# Criando Rótulos

toLabel = Label(display, textvariable=valor_texto, width=20, height=2, bg=corDisplay, fg="white")
toLabel.config(padx=7, relief="flat", anchor='e', justify="right", font="Ivy 15")
# padx = padding dentro do rótulo | anchor = colocar mais a direita | justify = justificar a direita
toLabel.place(x=0, y=0)

# Criando Botões

button_clean = Button(entradas, command=limparDisplay, text='C', width=6, height=2, font='Ivy 10 bold')
button_clean.config(relief="raised", overrelief="ridge")
#  relief = estilo da letra | overrelief = ao passar o mouse por cima algo irá ocorrer | fg = font ground
button_clean.place(x=1, y=0)

button_prcnt = Button(entradas, command=lambda: inserir_valores('%'), text='%', width=6, height=2, font='Ivy 10 bold')
button_prcnt.config(relief="raised", overrelief="ridge")
button_prcnt.place(x=59, y=0)

button_trocaSinal = Button(entradas, command=lambda: inserir_valores("*(-1)"), text="+/-", width=6, height=2)
button_trocaSinal.config(font='Ivy 10 bold', relief="raised", overrelief="ridge")
button_trocaSinal.place(x=117, y=0)

button_div = Button(entradas, command=lambda: inserir_valores('/'), text='/', width=6, height=2, font='Ivy 10 bold')
button_div.config(bg=corADireita, fg=corFonteADireita, relief="raised", overrelief="ridge")
button_div.place(x=176, y=0)

button_7 = Button(entradas, command=lambda: inserir_valores('7'), text='7', width=6, height=2, font="Ivy 10 bold")
button_7.config(relief="raised", overrelief="ridge")
button_7.place(x=1, y=45)

button_8 = Button(entradas, command=lambda: inserir_valores('8'), text='8', width=6, height=2, font="Ivy 10 bold")
button_8.config(relief="raised", overrelief="ridge")
button_8.place(x=59, y=45)

button_9 = Button(entradas, command=lambda: inserir_valores('9'), text='9', width=6, height=2, font="Ivy 10 bold")
button_9.config(relief="raised", overrelief="ridge")
button_9.place(x=117, y=45)

button_mult = Button(entradas, command=lambda: inserir_valores('*'), text='*', width=6, height=2, font="Ivy 10 bold")
button_mult.config(bg=corADireita, fg=corFonteADireita, relief="raised", overrelief="ridge")
button_mult.place(x=176, y=45)

button_4 = Button(entradas, command=lambda: inserir_valores('4'), text='4', width=6, height=2, font="Ivy 10 bold")
button_4.config(relief="raised", overrelief="ridge")
button_4.place(x=1, y=90)

button_5 = Button(entradas, command=lambda: inserir_valores('5'), text='5', width=6, height=2, font="Ivy 10 bold")
button_5.config(relief="raised", overrelief="ridge")
button_5.place(x=59, y=90)

button_6 = Button(entradas, command=lambda: inserir_valores('6'), text='6', width=6, height=2, font="Ivy 10 bold")
button_6.config(relief="raised", overrelief="ridge")
button_6.place(x=117, y=90)

button_sub = Button(entradas, command=lambda: inserir_valores('-'), text='-', width=6, height=2, font="Ivy 10 bold")
button_sub.config(bg=corADireita, fg=corFonteADireita, relief="raised", overrelief="ridge")
button_sub.place(x=176, y=90)

button_1 = Button(entradas, command=lambda: inserir_valores('1'), text='1', width=6, height=2, font="Ivy 10 bold")
button_1.config(relief="raised", overrelief="ridge")
button_1.place(x=1, y=135)

button_2 = Button(entradas, command=lambda: inserir_valores('2'), text='2', width=6, height=2, font="Ivy 10 bold")
button_2.config(relief="raised", overrelief="ridge")
button_2.place(x=59, y=135)

button_3 = Button(entradas, command=lambda: inserir_valores('3'), text='3', width=6, height=2, font="Ivy 10 bold")
button_3.config(relief="raised", overrelief="ridge")
button_3.place(x=117, y=135)

button_soma = Button(entradas, command=lambda: inserir_valores('+'), text='+', width=6, height=2, font="Ivy 10 bold")
button_soma.config(bg=corADireita, fg=corFonteADireita, relief="raised", overrelief="ridge")
button_soma.place(x=176, y=135)

button_zero = Button(entradas, command=lambda: inserir_valores('0'), text="0", width=13, height=2, font="Ivy 10 bold")
button_zero.config(relief="raised", overrelief="ridge")
button_zero.place(x=1, y=180)

button_virgula = Button(entradas, command=lambda: inserir_valores('.'), text='.', width=6, height=2, font="Ivy 10 bold")
button_virgula.config(relief="raised", overrelief="ridge")
button_virgula.place(x=117, y=180)

button_result = Button(entradas, command=lambda: calcular(), text='=', width=6, height=2, font="Ivy 10 bold")
button_result.config(bg=corADireita, fg=corFonteADireita, relief="raised", overrelief="ridge")
button_result.place(x=176, y=180)

janela.mainloop()
