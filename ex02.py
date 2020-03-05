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