from tkinter import *
from tkinter import ttk


#cores
cor1 = "#1f1f1f"  # Preta
cor2 = "#ffffff"  # Branca
cor3 = "#006379"  # Azul escuro
cor4 = "#3f3f3f"  # Vermelha
cor5 = "#FFD500"  # Amarelo
cor6 = "#0A8754"  # Verde

fonte_botao = ('Ivy 12 bold')
fonte_visor = ('Ivy 15 bold')
CARACTERES_MAX = 19

janela = Tk()
janela.title("Calculadora")
janela.geometry("240x350")
janela.config(bg=cor1)


# Frames
frame_tela = Frame(janela, width=240, height=60, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=240, height=290, bg=cor2)
frame_corpo.grid(row=1, column=0)

expressao = ""
ultimo_resultado = ""
apenas_resultado = False

# Função para calcular. Cada botão clicado adiciona o valor ao texto do visor
def entrar_valores(event):
    global expressao, ultimo_resultado, apenas_resultado

    # Impede que continue digitando se atingir o limite de caracteres
    if len(expressao) >= CARACTERES_MAX:
        return

    if apenas_resultado:
        if event in ['+', '-', '*', '/', '%']:
            expressao = ultimo_resultado + event
        else:
            expressao = str(event)
        apenas_resultado = False
    else:
        expressao += str(event)

    visor.set(expressao)

# Função para calcular
def calcular():
    global expressao, ultimo_resultado, apenas_resultado
    try:
        resultado = eval(expressao)
        visor.set(str(resultado))
        ultimo_resultado = str(resultado)
        apenas_resultado = True
    except Exception:
        visor.set("Erro")
        expressao = ""
        apenas_resultado = False


# Função para limpar a tela
def limpar_tela():
    global expressao
    expressao = ""
    visor.set("")
    apenas_resultado = False


# Labels
visor = StringVar()
app_label = Label(frame_tela, textvariable=visor, width=15, height=2, padx=59, relief=RAISED, anchor="e", justify="right", font=fonte_visor, bg=cor3, foreground=cor2)
app_label.place(x=0, y=0)

# Botões
b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_2.place(x=120, y=0)

b_3 = Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=4, height=2, bg=cor5, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_3.place(x=180, y=0)

b_3 = Button(frame_corpo, command=lambda: entrar_valores('7'), text="7", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_3.place(x=0, y=58)

b_4 = Button(frame_corpo, command=lambda: entrar_valores('8'), text="8", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_4.place(x=60, y=58)

b_5 = Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_5.place(x=120, y=58)

b_6 = Button(frame_corpo, command=lambda: entrar_valores('*'), text="*", width=4, height=2, bg=cor5, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_6.place(x=180, y=58)

b_7 = Button(frame_corpo, command=lambda: entrar_valores('4'), text="4", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_7.place(x=0, y=116)

b_8 = Button(frame_corpo, command=lambda: entrar_valores('5'), text="5", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_8.place(x=60, y=116)

b_9 = Button(frame_corpo, command=lambda: entrar_valores('6'), text="6", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_9.place(x=120, y=116)

b_10 = Button(frame_corpo, command=lambda: entrar_valores('-'), text="-", width=4, height=2, bg=cor5, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_10.place(x=180, y=116)

b_11 = Button(frame_corpo, command=lambda: entrar_valores('1'), text="1", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_11.place(x=0, y=174)

b_12 = Button(frame_corpo, command=lambda: entrar_valores('2'), text="2", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_12.place(x=60, y=174)

b_13 = Button(frame_corpo, command=lambda: entrar_valores('3'), text="3", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_13.place(x=120, y=174)

b_14 = Button(frame_corpo, command=lambda: entrar_valores('+'), text="+", width=4, height=2, bg=cor5, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_14.place(x=180, y=174)

b_15 = Button(frame_corpo, command=lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_15.place(x=0, y=232)

b_16 = Button(frame_corpo, command=lambda: entrar_valores('.'), text=".", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_16.place(x=120, y=232)

b_17 = Button(frame_corpo, command=calcular, text="=", width=4, height=2, bg=cor6, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_17.place(x=180, y=232)



janela.mainloop()