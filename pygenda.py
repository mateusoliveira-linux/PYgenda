"""funcionalidade do projeto pygenda
    parte de gravação de arquivo
    dev mateus oliveira"""

#========================================
#url do arquivo de dados
url = "_data/files"

#função para adicionar linhas
def add(matter, date, activity):
    #edita as strings para adiciona-las ao arquivo
    matter = " "+matter.strip().capitalize()+"    "
    date = "Data: "+date.lstrip()+"\n"
    activity = "atv: "+activity.strip()+"    "

    #abre o arquivo
    file = open(url, "a+")

    #descobre a quantidade de linhas do arquivo e soma 1 para gera o indice
    file.seek(0)
    index = len(file.readlines())+1

    #adiciona a nova linha
    file.write(str(index)+matter+activity+date)

    file.close()

#função para deletar linhas
def delete(line = 0):
    #ler o arquivo com lista
    file = open(url, "r")
    list = file.readlines()
    file.close()

    #verifica se a linha existe
    if line > len(list) or line <= 0:
        print("line not defined")
        return

    #delata o evento
    for x, event in enumerate(list):
        if event.strip()[0] == str(line):
            del list[x]

    #ordena o numero do indice novamente
    index = len(list)+1
    for x in range(1, index):
        list[x-1]= str(x)+list[x-1][1:]

    #reinscreve o arquivo
    file = open(url, "w")
    for row in list:
        file.write(row)
    file.close()

#função para ler o arquivo
def read():
    #abre o arquivo em file, ler ele e atribui ele a view e fecha o arquivo
    file = open(url, "r")
    view = file.readlines()
    file.close()

    #retorna uma lista com as linhas do arquivo, se ele tiver vasio retorna
    #uma lista vasia
    return view

#a interface de linha de comando so é executada se o scrip for chamdo direto
if __name__=="__main__":
    green = '\033[1;32m'
    red = "\033[1;31m"
    reset = '\033[0;0m'

    print("====================")
    print("      pygenda")
    print("====================\n")

    while True:

        command_text=input("{}Command{} --> ".format(green, reset))

        #comando para adicionar
        if command_text=="add":
            matter = input("Matter: ")
            date = input("Date: ")
            activity = input("Activity number: ")
            add(matter, date, activity)

        #comando para deleter
        elif command_text=="del":
            #recebe o numero da linha do evento
            res = int(input("inform the event number: "))
            delete(res)

        #comando para ler
        elif command_text=="read":
            #chama a função de ler e atribui a string a res
            res = read()
            print()
            for line in res:
                print(line.strip())
            print()

        #manual de comandos
        elif command_text=="man":
            #imprime lista de comandos
            print("\nadd = add event")
            print("del = delete event")
            print("read = read event")
            print("quit = quit pygenda\n")

        #comando para sair
        elif command_text=="quit":
            break

        #comando não encontrado!
        else:
            print("\n{}command {} not defined!{}\n".format(red, command_text, reset))
