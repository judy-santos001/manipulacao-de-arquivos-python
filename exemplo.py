# criar arquivo
arquivo = open("texto.txt", "a") # O caminho relativo é "texto.txt", podemos escolher qual extensão usar :)
arquivo.write("Olá, mundo!")

# OBS : Como para leitura e para texto são os valores padrão, você não precisa especificá-los."r""t"'''

'''Ler ("r").
    Adicionar ("a")
    Escrever ("w")
    Criar ("x")'''

# Abrir arquivo
arquivo = open("texto.txt", "r")
print(arquivo.read())

'''Leia uma linha do arquivo:'''
arquivo = open("texto.txt", "r")
print(arquivo.readline())
#print(arquivo.readline()) Ler outra linha do arquivo:

# É uma boa prática sempre fechar o arquivo quando você terminar de usá-lo.
arquivo = open("texto.txt", "r")
print(arquivo.readline())
arquivo.close()

# remover 
'''Para excluir arquivo utilizando Python, é preciso importar um módulo chamado os,
que contém as funções para interagir com o seu sistema operacional. Essa função recebe o 
caminho do arquivo como argumento e o exclui automaticamente.'''

import os
#A primeira linha: import os é o "argumento de importação". Este argumento é escrito na parte superior do seu arquivo e dá acesso às funções definidas no módulo os.
os.remove("texto.txt")
#A segunda linha: os.remove("texto.txt") remove o arquivo especificado.



'''Para evitar um erro, convém verificar se o arquivo existe antes 
de tentar excluí-lo'''
import os
if os.path.exists("texto.txt"):
  os.remove("texto.txt")
else:
  print("The file does not exist")


# removendo  pasta 
import os
os.rmdir("myfolder")

# OBS : só pode remover pastas vazias.

