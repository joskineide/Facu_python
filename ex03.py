import math  


# 21. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar
# a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi
# contratado para desenvolver o programa que monta a tabela de preços de pães, de
# 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo
# abaixo:
# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços

# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00



raise "hell"



# 1. Faça um Programa que peça dois números e imprima o maior deles.

firstNumber = float(input("Digite um número: "))
secondNumber = float(input("Digite mais um número: "))

if firstNumber > secondNumber:
    print("O primeiro número é maior")
else:
    print("O segundo número é maior")


# 2. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogals = ["a", "e", "i", "o", "u"]
character = input("Digite uma letra")
if character[0] in vogals:
    print("Letra digitado é uma vogal")
else:
    print("Letra digitado é uma consoante")


# 3. Faça um programa para a leitura de duas notas parciais de um aluno. O programa
# deve calcular a média alcançada por aluno e apresentar:
# - A mensagem &quot;Aprovado&quot;, se a média alcançada for maior ou igual a sete;
# - A mensagem &quot;Reprovado&quot;, se a média for menor do que sete;
# - A mensagem &quot;Aprovado com Distinção&quot;, se a média for igual a dez.

firstGrade = float(input("Digite a nota de um aluno: "))

secondGrade = float(input("Digite mais uma nota deste aluno: "))

avarageGrade = (firstGrade+secondGrade)/2

if avarageGrade >= 7:
    print("Aprovado")
else:
    print("Reprovado")
if avarageGrade == 10:
    print("Aprovado com Distinção")


# 4. Faça um Programa que leia três números e mostre-os em ordem decrescente.

firstNumber = float(input("Digite um número: "))
secondNumber = float(input("Digite mais um número: "))
thirdNumber = float(input("Digite um ultimo número: "))

if firstNumber > secondNumber and firstNumber > thirdNumber:
    if secondNumber > thirdNumber:
        print(firstNumber, secondNumber, thirdNumber)
    else:
        print(firstNumber, thirdNumber, secondNumber)
elif secondNumber > firstNumber and secondNumber > thirdNumber:
    if firstNumber > thirdNumber:
        print(secondNumber, firstNumber, thirdNumber)
    else:
        print(secondNumber, thirdNumber, firstNumber)
else:
    if firstNumber > secondNumber:
        print(thirdNumber, firstNumber, secondNumber)
    else:
        print(thirdNumber, secondNumber, firstNumber)


# 5. As Organizações Tabajara resolveram dar um aumento de salário aos seus
# colaboradores e lhe contrataram para desenvolver o programa que calculará os
# reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
# seguinte critério, baseado no salário atual:
# - salários até R$ 280,00 (incluindo) : aumento de 20%
# - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
# informe na tela:
# - o salário antes do reajuste;
# - o percentual de aumento aplicado;
# - o valor do aumento;
# - o novo salário, após o aumento.

salary = float(input("Digite o salário de seu funcionário: "))
salary_raise = 0

if(salary < 280):
    salary_raise = 0.2
elif(salary < 700):
    salary_raise = 0.15
elif(salary < 1500):
    salary_raise = 0.1
else:
    salary_raise = 0.05

print("Salário antes do reajuste: ", salary)
print("Ajuste será aplicado: ", salary_raise*100),
print("Aumento: ", salary*salary_raise)
print("Novo salário: ", salary*(1+salary_raise))


# 6. Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

week_days = {
    "1": "Domingo",
    "2": "Segunda",
    "3": "Terça",
    "4": "Quarta",
    "5": "Quinta",
    "6": "Sexta",
    "7": "Sábado"
}

requested_day = input("Digite um número para ver o dia da semana de acordo: ")

print(week_days.get(requested_day, "Valor inválido"))


# 7. Faça um programa que lê as duas notas parciais obtidas por um aluno numa
# disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos
# obedece à tabela abaixo:
# Média de Aproveitamento Conceito
# Entre 9.0 e 10.0 A
# Entre 7.5 e 9.0 B
# Entre 6.0 e 7.5 C
# Entre 4.0 e 6.0 D
# Entre 4.0 e zero E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
# mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito
# for D ou E.


firstGrade = float(input("Digite a primeira nota do aluno: "))
secondGrade = float(input("Digite a segunda nota do aluno: "))

avarageGrade = (firstGrade+secondGrade)/2

print("Primeira nota:", firstGrade)
print("Segunda nota:", secondGrade)
print("Média:", avarageGrade)


if avarageGrade < 4:
    print("Nota E")
    print("Reprovado")
elif avarageGrade < 6:
    print("Nota D")
    print("Reprovado")
elif avarageGrade < 7.5:
    print("Nota C")
    print("Aprovado")
elif avarageGrade < 9:
    print("Nota B")
    print("Aprovado")
else:
    print("Nota A")
    print("Aprovado")


# 8. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
# informar se os valores podem ser um triângulo. Indique, caso os lados formem um
# triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# - Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
# que o terceiro;
# - Triângulo Equilátero: três lados iguais;
# - Triângulo Isósceles: quaisquer dois lados iguais;
# - Triângulo Escaleno: três lados diferentes;

firstNumber = float(input("Digite o primeiro lado do triângulo: "))
secondNumber = float(input("Digite o segundo lado do triângulo: "))
thirdNumber = float(input("Digite o terceiro lado do triângulo: "))

if firstNumber + secondNumber < thirdNumber or firstNumber + thirdNumber < secondNumber or secondNumber + thirdNumber < firstNumber:
    print("Triângulo inválido")
elif firstNumber == secondNumber and firstNumber == thirdNumber:
    print("É um triângulo equilátero válido")
elif not firstNumber == secondNumber and not firstNumber == thirdNumber and not secondNumber == thirdNumber:
    print("É um triângulo escaleno válido")
else:
    print("É um triângulo isóceles válido")


# 9. Faça um programa que calcule as raízes de uma equação do segundo grau, na
# forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as
# consistências, informando ao usuário nas seguintes situações:
# - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e
# o programa não deve fazer pedir os demais valores, sendo encerrado;
# - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao
# usuário e encerre o programa;
# - Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
# informe-a ao usuário;
# - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

print("Por favor insira os valores para resolver a raiz da equação para a expressão de segundo grau ax2 + bx + c")

a = float(input("a: "))
if a == 0:
    print("Equação não é de segundo grau")
else:
    b = float(input("b: "))
    c = float(input("c: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("Equação não possui uma raiz real")
    else:
        firstRoot = (-b + math.sqrt(b**2-4*a*c))/(2*a)
        if delta == 0:
            print("Equação possui somente uma raiz: ", firstRoot)
        else:
            secondRoot = (-b - math.sqrt(b**2-4*a*c))/(2*a)
            print("Equação possui duas raizes reais, sendo elas: ", firstRoot, " e ", secondRoot)


# 10. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
# usuário a valor do saque e depois informar quantas notas de cada valor serão
# fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é
# de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a
# quantidade de notas existentes na máquina.
# - Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de
# 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# - Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de
# 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

to_withdraw = int(input("Quanto dinheiro gostaria de retirar? "))

one_bills = 0
five_bills = 0
ten_bills = 0
fifty_bills = 0
hundred_bills = 0

if to_withdraw < 10 or to_withdraw > 600:
    print("Não é possível retirar essa quantidade")
else:
    while to_withdraw > 0:
        if to_withdraw  < 5:
            one_bills += 1
            to_withdraw -= 1
        elif to_withdraw < 10:
            five_bills += 1
            to_withdraw -= 5
        elif to_withdraw < 50:
            ten_bills += 1
            to_withdraw -= 10
        elif to_withdraw < 100:
            fifty_bills += 1
            to_withdraw -= 50
        else:
            hundred_bills += 1
            to_withdraw -= 100

    print("Notas de 100:", hundred_bills)
    print("Notas de 50:", fifty_bills)
    print("Notas de 10:", ten_bills)
    print("Notas de 5:", five_bills)
    print("Notas de 1:", one_bills)


# 11. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
# perguntas são:
# &quot;Telefonou para a vítima?&quot;
# &quot;Esteve no local do crime?&quot;
# &quot;Mora perto da vítima?&quot;
# &quot;Devia para a vítima?&quot;
# &quot;Já trabalhou com a vítima?&quot;
# O programa deve no final emitir uma classificação sobre a participação da pessoa no
# crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
# como &quot;Suspeita&quot;, entre 3 e 4 como &quot;Cúmplice&quot; e 5 como &quot;Assassino&quot;. Caso contrário,
# ele será classificado como &quot;Inocente&quot;.

charges = 0

positive = ["sim", "yes", "true", "s", "y"]

print("Responda as seguites questões com sim ou não")

if input("Você já telefonou para a vítima? ").lower() in positive:
    charges += 1
if input("Você já esteve no local do crime? ").lower() in positive:
    charges += 1
if input("Você mora perto da vítima? ").lower() in positive:
    charges += 1
if input("Você tinha alguma divida com a vítima? ").lower() in positive:
    charges += 1
if input("Você já trabalhou com a vítima? ").lower() in positive:
    charges += 1

if charges < 2:
    print("Inocente")
elif charges < 3:
    print("Suspeita")
elif charges < 5:
    print("Cúmplice")
else:
    print("Assassino")


# 12. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# Até 5 Kg Acima de 5 Kg
# Morango R$ 2,50 por Kg R$ 2,20 por Kg
# Maçã R$ 1,80 por Kg R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
# R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um
# algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de
# maças adquiridas e escreva o valor a ser pago pelo cliente.

strawberry = float(input("Kilos de morango: "))
apple = float(input("Kilos de maçã: "))

final_price = 0

if strawberry < 5:
    final_price += strawberry * 2.5
else:
    final_price += strawberry * 2.2

if apple < 5:
    final_price += apple * 1.8
else:
    final_price += apple * 1.5

if final_price > 25:
    final_price = final_price * 0.9

print("O valor a ser pago: ", final_price)


# 13-a. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
# caso o valor seja inválido e continue pedindo até que o usuário informe um valor
# válido.

grade = float(input("Digite uma nota entre 0 e 10: "))

while grade < 0 or grade > 10:
    grade = float(input("Nota inválida, por favor digite uma nota entre 0 e 10: "))
    

# 13-b. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;

# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: &#39;f&#39; ou &#39;m&#39;;
# Estado Civil: &#39;s&#39;, &#39;c&#39;, &#39;v&#39;, &#39;d&#39;;

valid_genders = ["m", "f"]

valid_civil_states = ["s", "c", "v", "d"]


name = input("Digite seu nome: ")

while len(name) < 4:
    name = input("Nome inválido, por favor digite um nome com mais de 3 caractéres: ")

age = int(input("Digite sua idade: "))

while age < 0 or age > 150:
    age = int(input("Idade inválida,, por favor digite uma idade entre 0 e 150 anos: "))

salary = float(input("Digite seu salário: "))

while salary < 0:
    salary = float(input("Salário inválido, por favor digite um salário de 0 ou mais: "))

gender = input("Digite o seu sexo (m ou f): ")

while not gender in valid_genders:
    gender = input("Gênero inválido, por favor selecione uma das opções válidas (m ou f): ")

civil_state = input("Digite seu estado civil(s, c, v ou d): ")

while not civil_state in valid_civil_states:
    civil_state = input("Estado civil inválido, por favor selecione uma das opções válidas (s, c, v ou d): ")


# 14. Faça um programa que leia 5 números e informe o maior número.

current_number = float(input("Digite um número: "))

for _ in range(4):
    new_number = float(input("Digite um número: "))
    if new_number > current_number:
        current_number = new_number

print("O maior número digitado foi: ", current_number)


# 15. Faça um programa que leia 5 números e informe a soma e a média dos números.

total = 0

for _ in range(5):
    total += float(input("Digite um número: "))

print("A soma de todos os números é: ", total)

print("A média dos números é: ", total/5)


# 16. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

count = 1

while count < 50:
    print(count)
    count += 2


# 17. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
# número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver
# a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

number = int(input("Digite o número que deseja ver a tabuada de: "))

count = 1

while count <= 10:
    print(number, "X", count, "=",  number * count)
    count += 1


# 18. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um
# programa capaz de gerar a série até o n−ésimo termo.

n_loops = int(input("Quantos números do fibbonachi deseja ver?: "))

past_number = 0

storage_var = 0

cur_number = 1

for _ in range(n_loops):
    print(cur_number)
    storage_var = cur_number
    cur_number = past_number + cur_number
    past_number = storage_var


# 19. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
# usuário. Ex.: 5!=5.4.3.2.1=120

count = int(input("Quantos números do fibbonachi deseja ver?: "))
total = 1

while count > 0:
    total = total * count
    count -= 1

print(total)


# 20. O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca
# de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele
# desenvolveu um tabela que contém o número de itens que o cliente comprou e ao
# lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar
# quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado
# para desenvolver o programa que monta esta tabela de preços, que conterá os
# preços de 1 até 50 produtos, conforme o exemplo abaixo:
# Lojas Quase Dois - Tabela de preços
# 1 - R$ 1.99
# 2 - R$ 3.98
# ...
# 50 - R$ 99.50

print(" Lojas Quase Dois - Tabela de preços")

count = 1

while count <= 50:
    print(count, "- R$", count*1.99)
    count += 1




# 22. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e
# agora possui uma loja de conveniências. Faça um programa que implemente uma
# caixa registradora rudimentar. O programa deverá receber um número
# desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve
# ser informado pelo operador para indicar o final da compra. O programa deve então
# mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
# para então calcular e mostrar o valor do troco. Após esta operação, o programa
# deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser
# conforme o exemplo abaixo:
# Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ...

# 23. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre
# acidentes de trânsito. Foram obtidos os seguintes dados:
# - Código da cidade;
# - Número de veículos de passeio (em 1999);
# - Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# - Qual a média de veículos nas cinco cidades juntas;
# - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de
# passeio.

# 24. Faça um programa que receba o valor de uma dívida e mostre uma tabela com
# os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor
# da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
# 1 0
# 3 10
# 6 15
# 9 20
# 12 25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela

# R$ 1.000,00 0 1 R$ 1.000,00
# R$ 1.100,00 100 3 R$ 366,00
# R$ 1.150,00 150 6 R$ 191,67
# 25. Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.