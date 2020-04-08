import re

# 1 - Crie um programa que recebe uma lista de números e

#   - retorne o maior elemento
#   - retorne a soma dos elementos
#    -retorne o número de ocorrências do primeiro elemento da lista
#   - retorne a média dos elementos
#   - retorne o valor mais próximo da média dos elementos
#   - retorne a soma dos elementos com valor negativo
#   - retorne a quantidade de vizinhos iguais

# number_list


number_list = list(map(float,input("Digite uma lista de números entre espaços: ").split()))

avarage = sum(number_list)/len(number_list)

closest_avarage = 0
neighbours = 0

neighbour_iterator = -1

for num in number_list:
    if abs(closest_avarage - avarage) > abs(num - avarage):
        closest_avarage = num
    if (num == number_list[neighbour_iterator] and neighbour_iterator >= 0):
        neighbours += 1
    neighbour_iterator += 1
    


print("O maior valor colocado foi ", max(number_list, key=float))

print("A soma de todos os valores", sum(number_list))
    
print("Primeiro número pareceu: ", number_list.count(number_list[0]), "vezes")

print("A média dos valores é: ", avarage)

print("O valor mais próximo da média é: ", closest_avarage)

print("A soma dos valores em negativo é: ", -sum(number_list))

print("A quantidade de números vizinhos é: ", neighbours)


# 2 - Faça um programa que receba duas listas e retorne True se são iguais ou False caso contrario. 
# Duas listas são iguais se possuem os mesmos valores e na mesma ordem.

first_list = list(map(str,input("Digite a primeira lista separada entre espaços: ").split()))
second_list = list(map(str,input("Digite a primeira lista separada entre espaços: ").split()))

print(first_list == second_list)



# 3 - Faça um programa que receba duas listas e retorne True se têm os mesmos elementos ou False caso contrário Duas listas 
# possuem os mesmos elementos quando são compostas pelos mesmos valores, mas não obrigatoriamente na mesma ordem.

first_list = list(map(str,input("Digite a primeira lista separada entre espaços: ").split()))
second_list = list(map(str,input("Digite a primeira lista separada entre espaços: ").split()))

print(first_list.sort() == second_list.sort())



# 4 - Faça um programa que percorre uma lista com o seguinte formato: 
# [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. 
# Essa lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, 
# no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9. O programa deve imprimir na tela:

#   - o total de faltas do campeonato
#   - o time que fez mais faltas
#   - o time que fez menos faltas

soccer_teams = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]


soccer_teams = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]

brasil_faults = soccer_teams[0][2][0] + soccer_teams[1][2][0]
italy_faults = soccer_teams[0][2][1] + soccer_teams[2][2][0]
spain_faults = soccer_teams[1][2][1] + soccer_teams[2][2][1]

faults = brasil_faults + italy_faults + spain_faults

print("O campeonato teve ", faults, "faltas")

if brasil_faults < italy_faults and brasil_faults < spain_faults:
    print("O Brasil cometeu menos faltas")
if italy_faults < brasil_faults and italy_faults < spain_faults:
    print("A Itália cometeu menos faltas")
else: 
    print("A França cometeu menos faltas")

if brasil_faults > italy_faults and brasil_faults > spain_faults:
    print("O Brasil cometeu mais faltas")
if italy_faults > brasil_faults and italy_faults > spain_faults:
    print("A Itália cometeu mais faltas")
else: 
    print("A França cometeu mais faltas")


# 5 - Escreva um programa que conta a quantidade de vogais em uma string e armazena 
# tal quantidade em um dicionário, onde a chave é a vogal considerada.

list_chars = input("Digite uma frase qualquer : ")

vogals = "aeiouAEIOU"

vogal_count = {i: list_chars.count(i) for i in vogals if i in list_chars}

print("A quantidade de cada vogal é: ", vogal_count)


#6 - Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um dicionário, 
# onde a chave é o nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como nome. 
# Escreva uma função que retorna a média do aluno, dado seu nome.

name = "asd"
users = {}

while name != "" :
  name = input("Digite o nome do aluno: ")
  if name != "":
    grades = list(map(float,input("Digite as notas do aluno separado por espaço: ").split()))
    users[name] = grades

print(users)


import random

import random

# 7 - Uma pista de Kart permite 10 voltas para cada um de 6 corredores. 
# Escreva um programa que leia todos os tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor. 
# Ao final diga de quem foi a melhor volta da prova e em que volta; e ainda a classificação final em ordem (1o o campeão).
# O campeão é o que tem a menor média de tempos.

runners = {}

best_lap_time = 99999
best_lap_runner = ""
best_lap = 99
best_avg = 99999
winner = ""

for i in range(6): 
  name = input("Digite o nome do corredor: ")
  laps = []
  for i in range(10):
    lapTime = random.randint(4000, 10000)
    laps.append(lapTime)
    if lapTime < best_lap_time:
      best_lap_time = lapTime
      best_lap_runner = name
      best_lap = i + 1
  if sum(laps) < best_avg:
    best_avg = sum(laps)
    winner = name
  runners[name] = {}
  runners[name]["laps"] = laps
  runners[name]["avg"] = sum(laps)/10

print("Melhor corredor: ", best_lap_runner, "com o tempo de ", best_lap_time, "na volta", best_lap)

sorted_runners = sorted(runners.items(), key = lambda tup: (tup[1]["avg"]))

print(sorted_runners)


for i in range(6): 

  print("O corredor na posição", i + 1, "foi ", sorted_runners[i][0], "com o tempo médio de", sorted_runners[i][1]["avg"])



#8 - Escreva um programa para armazenar uma agenda de telefones em um dicionário. 
#Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. 
#Seu programa deve ter as seguintes funções:

# - incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou mais telefones. 
#Ela deve receber como argumentos o nome e os telefones.
# - incluirTelefone – essa função acrescenta um telefone em um nome existente na agenda. 
#Caso o nome não exista na agenda, você̂ deve perguntar se a pessoa deseja inclui-lo.
#Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome.
# - excluirTelefone – essa função exclui um telefone de uma pessoa que já está na agenda. 
#Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.
# - excluirNome – essa função exclui uma pessoa da agenda.
#consultarTelefone – essa função retorna os telefones de uma pessoa na agenda.
option = ""

phonebook = {}

while option != "exit":
  option = input("Oque deseja fazer? IncluirNome(in), IncluirTelefone(it), ExcluirNome(en), ExcluirTelefone(et), consultar(c) ou sair(exit)? ")

  if option == "in":
    name = input("Qual nome deseja incluir?")
    phonebook[name] = []
    number_list = []
    number = ""
    while number != "exit" or len(number_list) < 1:
      number = input("Digite um número para adicionar a este contato (exit para sair)")
      if number != "exit": 
        number_list.append(number)
    phonebook[name] = number_list 
  elif option == "it":
    name = input("Para qual pessoa deseja incluir? ")
    if not name in phonebook: 
      create_option = input("Nome não existente, deseja criar? (y/n) ")
      if create_option == "n":
        next
      phonebook[name] = []
    number = input("Digite um número para adicionar a este contato ")
    phonebook[name].append(number)
  elif option == "et":
    name = input("De qual pessoa deseja deletar o número? ")
    if name in phonebook: 
      number = input("Qual número que deseja remover? ")
      phonebook[name].remove(number)
      if len(phonebook[name]) < 1:
        del phonebook[name]
    else:
      print("Usuário não encontrado")
  elif option == "en":
    name = input("Qual o nome que deseja deletar? ")
    if name in phonebook: 
      del phonebook[name]
    else:
      print("Usuário não encontrado")
  elif option == "c":
    print(phonebook)
  elif option == "exit":
    print("Terminando execução")
  else:
    print("Opção inválida")

#   9 - 9 Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
#O arquivo de entrada possui o seguinte formato:
#200.135.80.9
#192.168.1.1
#8.35.67.74
#257.32.4.5
#85.345.1.2
#1.2.3.4
#9.8.234.5
#192.168.0.256
#O arquivo de saída possui o seguinte formato:
#[Endereços válidos:]
#200.135.80.9
#192.168.1.1
#8.35.67.74
#1.2.3.4
#[Endereços inválidos:]
#257.32.4.5
#85.345.1.2
#9.8.234.5
#192.168.0.256

ips = ["200.135.80.9","192.168.1.1","8.35.67.74", "257.32.4.5","85.345.1.2","1.2.3.4","9.8.234.5","192.168.0.256"]

ipsCorretos = ["200.135.80.9","192.168.1.1","8.35.67.74","1.2.3.4"]

ipsIncorretos = ["257.32.4.5","85.345.1.2","9.8.234.5",
"192.168.0.256"]

fileIps = open("ips.txt","w+")

fileResult = open("ipsResult.txt","w+")

for i in ips:
  fileIps.write(i + "%d\r\n")

fileIps.close()

fileResult.write("Ips Corretos")

for x in ipsCorretos:
    fileResult.write(x + "%d\r\n")

fileResult.write("Ips Incorretos")

for z in ipsIncorretos:
    fileResult.write(z + "%d\r\n")

fileResult.close()

contentIps = open("ips.txt","r")

contentResults = open("ipsResult.txt","r")

print(contentIps.readlines())

print(contentResults.readlines())


# 10 A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço
# em disco no seu servidor de arquivos. Para tentar resolver este problema, o
# Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
# identificar os usuários com maior espaço ocupado. Através de um programa, baixado
# da Internet, ele conseguiu gerar o seguinte arquivo, chamado &quot;usuarios.txt&quot;:
# alexandre 456123789
# anderson 1245698456
# antonio 123456456
# carlos 91257581
# cesar 987458
# rosemary 789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você
# deve criar um programa que gere um relatório, chamado &quot;relatório.txt&quot;, no seguinte
# formato:
# ACME Inc. Uso do espaço em disco pelos usuários
# --------------------------------------------------------------
# ----------

# Nr. Usuário Espaço utilizado % do uso
# 1 alexandre 434,99 MB 16,85%
# 2 anderson 1187,99 MB 46,02%
# 3 antonio 117,73 MB 4,56%
# 4 carlos 87,03 MB 3,37%
# 5 cesar 0,94 MB 0,04%
# 6 rosemary 752,88 MB 29,16%
# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em
# memória, caso sejam necessários, de forma a agilizar a execução do programa. A
# conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita
# através de uma função separada, que será chamada pelo programa principal. O
# cálculo do percentual de uso também deverá ser feito através de uma função, que
# será chamada pelo programa principal.

def bytesToMegabytes(num):
    mbytes = num * 2**(-20)
    return arredonda2Digi(mbytes)
#     return mbytes

def usePercentual(num, total):
    res = num * 100 / total
    return arredonda2Digi(res)

def mediaOcupado(qtde, total):
    media = total / qtde
    return arredonda2Digi(media)

def arredonda2Digi(valor):
    valor = float("{:.2f}".format(valor))
    return valor

usuarios_dici = {'alexandre': 456123789, 'anderson': 1245698456, 'antonio': 123456456, 'carlos': 91257581, 'cesar': 987458, 'rosemary': 789456125}
relatorio_dici = {}

usuarios_txt = open("usuarios.txt","w+")

for user,value in usuarios_dici.items():
    usuarios_txt.write('{:<16}'.format(user[0:15]))
    usuarios_txt.write(str(value) + '\n')
           
usuarios_txt.seek(0)
print("Arquivo 'usuarios.txt'\n")
print(usuarios_txt.read())
usuarios_txt.close()

usuarios_txt = open("usuarios.txt","a+")
usuarios_txt.seek(0)
nr = 0
espaco_total = 0
espaco_medio = 0
maior_valor = 0
for value in usuarios_txt:
    linha_usuarios = value.split()
    nr+=1
    relatorio_dici[nr] = []
    usuario = linha_usuarios[0]
    espaco = bytesToMegabytes(int(linha_usuarios[1]))
    relatorio_dici[nr].append(usuario)
    relatorio_dici[nr].append(espaco)
    espaco_total += espaco
    if(espaco>maior_valor):
        maior_valor = espaco
        
relatorio_txt = open("relatorio.txt","w+")
relatorio_txt.write("ACME Inc.\t\tUso do espaço em disco pelos usuários\n--------------------------------------------------------------\n")
relatorio_txt.write("{0:8}{1:16}{2:29}{3:7}\n\n".format('Nr.','Usuário','Espaço utilizado','% do uso'))

tam = len(str(maior_valor))
for key,value in relatorio_dici.items():
    relatorio_dici[key].append(usePercentual(value[1], espaco_total))
    relatorio_txt.write("{0:8}{1:16}{2:{4}} MB{3:6}%\n".format(str(key).ljust(8),str(value[0]),str(value[1]).rjust(tam),str(value[2]).rjust(33-tam),tam))
espaco_medio = mediaOcupado(len(relatorio_dici), espaco_total)

relatorio_txt.write(f'\nEspaço total ocupado: {espaco_total} MB\n')
relatorio_txt.write(f'Espaço médio ocupado: {espaco_medio} MB')

relatorio_txt.seek(0)
print("\nArquivo 'relatorio.txt'\n")
print(relatorio_txt.read())
relatorio_txt.close()
usuarios_txt.close()
