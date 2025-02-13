#! /usr/bin/python3

from tkinter import *
from functools import partial
import pygenda as pg

#tela ver evento
def read_event(screen="home"):
    #ler os items do arquivo
    def read():
        list = pg.read()
        for a in list:
            listbox.insert(END, a.strip())

    #função Excruir item
    def delete_item():
        #recebe a linha do arquivo de texto selecionada
        delete_line = listbox.get(ACTIVE)
        #verifica se a lista não esta visia
        if delete_line == "":
            return

        #deleta a linha do indice
        delete_line = int(delete_line[0])
        pg.delete(delete_line)
        #delata os elementos
        listbox.delete(0, END)

        #incere os elemento a listbox
        read()

    #destroi a tela de onde foi chameda
    if screen=="home":
        #destroi o frame home
        home.destroy()
    elif screen=="add":
        #destroi add
        add.destroy()
    else:
        #se não for nenhuma destroi a janela
        window.destroy()
        return

    global read_list
    read_list=Frame(window)
    read_list.config(background="#0c1821")
    read_list.pack()

    #criando e posicionando label
    label_read=Label(
        read_list,
        text="LISTA DE EVENTOS",
        font=("",25,"bold"),
        background="#0c1821",
        foreground="#f1f1f1"
    )
    label_read.grid(row=0,columnspan=2,pady=(0,10))

    #criando e posicionando os botoes
    button_add_2=Button(
        read_list,
        text="Adicionar",
        width=20,
        height=1,
        background="#011e30",
        foreground="#ffffff",
        activebackground="#011e30",
        activeforeground="#d2d5dd",
        command=partial(add_event, "read")
    )
    button_delete=Button(
        read_list,
        text="Excluir",
        width=20,
        height=1,
        background="#011e30",
        foreground="#ffffff",
        activebackground="#011e30",
        activeforeground="#d2d5dd",
        command=delete_item
    )

    button_add_2.grid(row=1,column=0,padx=(0,5),sticky=E)
    button_delete.grid(row=1,column=1,padx=(5,0),sticky=W)

    #frame de exibição
    show_text=Frame(read_list, background="#0c1821")
    show_text.grid(row=2,columnspan=2,pady=(15,0))
    show_text.config(width=625,height=500)

    #criando e posicionando o listbox
    listbox=Listbox(
        show_text,
        width=76,
        height=27,
        relief="flat",
        background="#0c1821",
        foreground="#ffffff",
        selectbackground="#ffffff",
        selectforeground="#000000",
        highlightthickness=0,
    )

    listbox.pack(side=LEFT)

    #chama a função para adiciona os elemento a listbox
    read()

    #bara de rolagem scrollbar
    scroll=Scrollbar(
        show_text,
        background="#011e30",
        activebackground="#011e30",
        troughcolor="#ffffff",
        command=listbox.yview
    )
    listbox.config(yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT, fill=Y)

#tela Adicionar evento
def add_event(screen="home"):
    #função para limpar os campos e adicionar ao arquivo de dados
    def clear_and_add():
        #verifica se a aulgum campo vasio
        if (str(atv.get())!="" and str(data.get())!="" and str(num.get())!=""):
            #resistra no arquivo de texto
            name = str(atv.get())
            date = str(data.get())
            number = str(num.get())
            pg.add(name, date, number)

            #limpar os campos (entry)
            atv.delete(0,END)
            data.delete(0,END)
            num.delete(0,END)

            #mensagem de adicionada
            label_msg.config(
                text="Adicionado com sucesso!",
                foreground="#008000"
            )
        else:
            #mensagem de campo vasio
            label_msg.config(
                text="Prencha todos os campos!",
                foreground="#ff0000",
            )

    #destroi a tela de onde foi chamando
    if screen == "home":
        #destruir home
        home.destroy()
    else:
        #destroi read list
        read_list.destroy()


    #configurando e posicionando o frame add
    global add
    add=Frame(window)
    add.config(background="#0c1821")
    add.pack()

    #criando e posicionando label add e label dos campos
    label_add=Label(
        add,
        text="ADICIONAR EVENTO ESCOLAR",
        background="#0c1821",
        foreground="#f1f1f1",
        font=('',25,"bold")
    )

    label_atv=Label(
        add,
        text="Disciplina :",
        background="#0c1821",
        foreground="#f1f1f1"
    )
    label_data=Label(
        add,
        text="Data :",
        background="#0c1821",
        foreground="#f1f1f1"
    )
    label_num=Label(
        add,
        text="Numero da atividade :",
        background="#0c1821",
        foreground="#f1f1f1"
    )

    label_add.grid(row=0, column=0, columnspan=2)
    label_atv.grid(row=1, column=0, pady=(50,25), sticky=E)
    label_data.grid(row=2, column=0, pady=25, sticky=E)
    label_num.grid(row=3, column=0, pady=25, sticky=E)

    #label de mensagem campo vasio/adicionada
    label_msg=Label(
        add,
        background="#0c1821",
        font=("",15,"bold")
    )
    label_msg.grid(row=6, columnspan=2)

    #criando e posicionando as entradas
    atv=Entry(add)
    data=Entry(add)
    num=Entry(add)

    atv.grid(row=1, column=1, sticky=W, pady=(50,25))
    data.grid(row=2, column=1, sticky=W)
    num.grid(row=3, column=1, sticky=W)

    #butoes de adicionar e cancelar
    add_button=Button(add,
        text="Adicionar",
        background="#011e30",
        foreground="#ffffff",
        activebackground="#011e30",
        activeforeground="#d2d5dd",
        width=20,
        height=1,
        command=clear_and_add
    )
    cancel_button=Button(add,
        text="Cancelar",
        background="#011e30",
        foreground="#ffffff",
        activebackground="#011e30",
        activeforeground="#d2d5dd",
        width=20,
        height=1,
    )

    #volta para a tela de onde foi chamada
    if screen=="home":
        #se vier de home volta a home
        cancel_button.config(command=partial(Home,False))

    elif screen=="read":
        #se vier de read_list volta a read_list
        cancel_button.config(command=partial(read_event,"add"))

    else:
        #se não vier de nenhuma destroi a janela
        window.destroy()
        return

    add_button.grid(row=4, columnspan=2, pady=25)
    cancel_button.grid(row=5, columnspan=2, pady=25)

#tela home
def Home(first=True):
    #testa se a tela foi chamada do main ou de outra tela
    if first == False:
        #destroi a tela add
        add.destroy()
        #criando e frame home
        global home
        home=Frame(window)

    #configurando e posicionando o frame home
    home.config(bg = "#0c1821")
    home.pack()

    #criando e posicionando label home
    label_home=Label(home, text="PYgenda")
    label_home.config(
        background="#0c1821",
        fg = "#f1f1f1",
        height = 1,
        width = 10,
        font=("",34,"bold")
    )
    label_home.pack()

    #criando e posicionando os botoes iniciais
    button_add = Button(
        home,
        text="Adicionar",
        height = 1,
        width=20,
        bg="#011e30",
        fg="#ffffff",
        bd=0,
        activebackground = "#011e30",
        activeforeground = "#d2d5dd",
        command=add_event
    )

    button_read = Button(
        home,
        text="Ver Lista",
        height = 1,
        width=20,
        bg="#011e30",
        foreground="#f1f1f1",
        activebackground = "#011e30",
        activeforeground = "#d2d5dd",
        command=read_event
    )

    button_add.pack(pady=(150,200))
    button_read.pack()

#---------------------main------------------------
#criando nova janela (instancia de Tk)
window = Tk()

#declarando frames
home=Frame(window)
add=Frame(window)
read_list=Frame(window)

#chamando a tela home (freme home e seus widgets)
Home()

#configura o titolo a cor o icone e o tamanho da janela
window.iconphoto(False, PhotoImage(file="_icon/icon.png"))
window.title("PYgenda")
window.config(background="#0c1821")
window.geometry("625x600+400+100")
window.mainloop()
