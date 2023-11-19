import buscaEmProfundidade as bpd
import buscaEmProfundidadeLetras as bpdl


#Fiz 2 algoritmos, sendo um para trabalhar com apenas vertices que são nomeados por Numeros e o outro para quando os vertices são nomeados por Letras
#Tava tentando fazer apenas um arquivo.py que desse para ler tanto Numero quanto Letra, mas não conseguir.
#Então decidir fazer 2 e esse outro que esta lendo essas informações para que precise apenas desse para interagir com os outros 2.
#Para o Algoritmo rodar é neceassario fornecer o nome da o arquivo txt, apenas o nome sem o .txt
#Com isso infomado é necessario que arquivo txt esteja na mesma pasta, para que so precise acessar apenas o nome dela.

#OBS: caso esteja dando erro em abrir o arquivo .txt o problema é que o compilador tem que ser aberto sá na pasta do codigo.
#irei enviar uma foto para ficar mais claro.
#Testei com os arquivos GD.txt que o vertices são nomeados com inteiros, e testei com o test.txt que os vertices são nomeados por letras.
#Esta junto desses arquivos de codigo.py os arquivos.txt.

def escolherFunção():
    print("Os Vertices do grafo são nomeados por: \n1 - Numeros\n2 - Letras")
    resposta = input()
    
    if resposta == '1': #Caso os vertices forem nomeados por NUMEROS escolha essa Função
        bpd.inicializar_DFS_NUM()
    elif resposta == '2': #Caso os vertices forem nomeados por LETRAS escolha essa Função
        bpdl.inicializar_DFS_LETRA()
    else:
        print("Não foi nenhuma alternativa válida.")


escolherFunção()
