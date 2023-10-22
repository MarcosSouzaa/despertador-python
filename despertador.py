# importando tkinter (interface gráfica)
from tkinter.ttk import *
from tkinter import*
# importando o pillow (manipulação de imagens)
from PIL import Image, ImageTk
from pygame import mixer
#funcionamento do audio
from pygame import mixer
import time
from datetime import datetime

from time import sleep
from threading import Thread # Permite que vários programas/funções sejam executados ao mesmo tempo

# cores
cor0 = '#f0f3f5' # preta
cor1 = '#feffff' # branca
cor2 = '#d6872d' # ouro/gold
cor3 = '#fc766d' # vermelha/red
cor4 = '#403d3d' # preta/black
cor5 = '#4688e8' # azul/blue

# criando janela
janela = Tk()
janela.title('')
janela.geometry('350x150')
janela.configure(background = cor1)
janela.resizable(width=FALSE, height=FALSE) # redimensionável

# dividindo a janela em dois frames
frame_logo = Frame(janela, width=400, height=10, bg=cor1)
frame_logo.grid(row=0, column=0, pady=1, padx=0)

frame_corpo = Frame(janela, width=400, height=290, bg=cor1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0)

# Configurando o frame logo
label_linha = Label(janela, width=400, height=1, bg=cor2, anchor=NW, font=('Ivy 1'))
label_linha.place(x=0, y=0)

# Configurando o frame corpo
imagem = Image.open('icon_alarm.png')
imagem.resize((100, 100))
imagem = ImageTk.PhotoImage(imagem)

label_imagem = Label(frame_corpo, height=100, image=imagem, compound=LEFT, padx=10, anchor=NW, font=('Ivy 16 bold'), bg=cor1, fg=cor3)
label_imagem.place(x=10, y=10)

label_nome = Label(frame_corpo, text='Alarme', height=1, anchor=NE, font=('Ivy 10'), bg=cor1, fg=cor4)
label_nome.place(x=105, y=10)

# criando combo box
label_hora = Label(frame_corpo, text='Horas', height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
label_hora.place(x=127, y=40)
combo_hora = Combobox(frame_corpo, width=2, font=('arial 7'))
combo_hora['value'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12')
combo_hora.current(0)
combo_hora.place(x=130, y=58)

label_minuto = Label(frame_corpo, text='Minutos', height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
label_minuto.place(x=177, y=40)
combo_minuto = Combobox(frame_corpo, width=2, font=('arial 7'))
combo_minuto['value'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12',
                         '13','14','15','16','17','18','19','20','21','22','23','24','25',
                         '26','27','28','29','30','31','32','33','34','35','36','37','38',
                         '39','40','41','42','43','44','45','46','47','48','49','50','51',
                         '52','53','54','55','56','57','58','59')
combo_minuto.current(0)
combo_minuto.place(x=180, y=58)

label_segundo = Label(frame_corpo, text='Segundos', height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
label_segundo.place(x=227, y=40)
combo_segundo = Combobox(frame_corpo, width=2, font=('arial 7'))
combo_segundo['value'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12',
                         '13','14','15','16','17','18','19','20','21','22','23','24','25',
                         '26','27','28','29','30','31','32','33','34','35','36','37','38',
                         '39','40','41','42','43','44','45','46','47','48','49','50','51',
                         '52','53','54','55','56','57','58','59')
combo_segundo.current(0)
combo_segundo.place(x=230, y=58)

label_periodo = Label(frame_corpo, text='Periodo', height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
label_periodo.place(x=277, y=40)
combo_periodo = Combobox(frame_corpo, width=3, font=('arial 7'))
combo_periodo['value'] = ('AM','PM')
combo_periodo.current(0)
combo_periodo.place(x=280, y=58)

# essa função será chamada pelo command para ativar o alarme
def ativar_alarme():
    if selecionado.get() == 1:
        print('Ativar: ', selecionado.get())
    else:
        # criar thread
        t1 = Thread(target=alarme)
        # iniciar o thread
        t1.start()


# essa função será chamada pelo command para desativar o alarme
def desativar_alarme():
    if selecionado.get() == 1:
        print('Alarme desativado: ', selecionado.get())
        mixer.music.stop()
   
# criando um radibotton
selecionado = IntVar()

# Ao chamar a função, vai devolver 1 de True no terminal significando ativado
radio = Radiobutton(frame_corpo,command=ativar_alarme, text='Ativar',value=1, variable=selecionado, font=('Arial 8'), bg=cor1, fg=cor4)
radio.place(x=125, y=95)

def tocar_alarme():   
    mixer.music.load('1.mp3')
    mixer.music.play()
    selecionado.set(0)

    radio = Radiobutton(frame_corpo,command=desativar_alarme, text='Desativar',value=1, variable=selecionado, font=('Arial 8'), bg=cor1, fg=cor4)
    radio.place(x=187, y=95)

def alarme():
    while True:      
        control = selecionado.get()
        hora_alarme = combo_hora.get()
        min_alarme = combo_minuto.get()
        seg_alarme = combo_segundo.get()
        periodo_alarme = combo_periodo.get().upper()

        # obtendo a hora atual
        hora_atual = datetime.now()

        hora = hora_atual.strftime('%I')
        minuto = hora_atual.strftime('%M')
        segundo = hora_atual.strftime('%S')
        periodo = hora_atual.strftime('%p')

        if control == 1:
            if periodo_alarme == periodo:
                if hora_alarme == hora:
                    if min_alarme == minuto:
                        if seg_alarme == segundo:
                            print('Hora de fazer uma pausa!')
                            tocar_alarme()
                            ativar_alarme()
        sleep(1)
        
t1 = Thread(target=alarme)

# iniciar o thread
t1.start()
mixer.init()
 
janela.mainloop()