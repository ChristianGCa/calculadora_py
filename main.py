from tkinter import *
from tkinter import ttk


#cores
cor1 = "#1f1f1f"  # Preta
cor2 = "#ffffff"  # Branca
cor3 = "#005180"  # Azul escuro
cor4 = "#3f3f3f"  # Vermelha
cor5 = "#FF7300"  # Laranja
cor6 = "#3C6B3C"  # Verde

fonte_botao = ('Ivy 12 bold')

janela = Tk()
janela.title("Calculadora")
janela.geometry("240x350")
janela.config(bg=cor1)


# Frames
frame_tela = Frame(janela, width=240, height=60, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=240, height=290, bg=cor2)
frame_corpo.grid(row=1, column=0)


# Botões
b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text="%", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_2.place(x=120, y=0)

b_3 = Button(frame_corpo, text="/", width=4, height=2, bg=cor5, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_3.place(x=180, y=0)

b_3 = Button(frame_corpo, text="7", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_3.place(x=0, y=58)

b_4 = Button(frame_corpo, text="8", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_4.place(x=60, y=58)

b_5 = Button(frame_corpo, text="9", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_5.place(x=120, y=58)

b_6 = Button(frame_corpo, text="*", width=4, height=2, bg=cor5, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_6.place(x=180, y=58)

b_7 = Button(frame_corpo, text="4", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_7.place(x=0, y=116)

b_8 = Button(frame_corpo, text="5", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_8.place(x=60, y=116)

b_9 = Button(frame_corpo, text="6", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_9.place(x=120, y=116)

b_10 = Button(frame_corpo, text="-", width=4, height=2, bg=cor5, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_10.place(x=180, y=116)

b_11 = Button(frame_corpo, text="1", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_11.place(x=0, y=174)

b_12 = Button(frame_corpo, text="2", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_12.place(x=60, y=174)

b_13 = Button(frame_corpo, text="3", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_13.place(x=120, y=174)

b_14 = Button(frame_corpo, text="+", width=4, height=2, bg=cor5, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_14.place(x=180, y=174)

b_15 = Button(frame_corpo, text="0", width=11, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_15.place(x=0, y=232)

b_16 = Button(frame_corpo, text=".", width=4, height=2, bg=cor2, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_16.place(x=120, y=232)

b_17 = Button(frame_corpo, text="=", width=4, height=2, bg=cor6, font=fonte_botao, relief=RAISED, overrelief=RIDGE, cursor="hand2")
b_17.place(x=180, y=232)

janela.mainloop()