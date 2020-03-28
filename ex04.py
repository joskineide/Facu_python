# 1 Menor de dois pares: Escreva uma função que retorne o menor de dois números
# dados se ambos os números forem pares, mas retorna o maior se um dos dois for
# ímpar. Exemplo:
# menor_de_dois_pares(2,4) --&gt; 2
# menor_de_dois_pares (2,5) --&gt; 5

def evenLowerElseHigher(num1, num2):
    if(num1 % 2 == 0 and num2 % 2 == 0):
        if(num1 < num2):
            return num1
        else:
            return num2
    else:
        if(num1 > num2):
            return num1
        else:
            return num2

print(evenLowerElseHigher(2,4))
print(evenLowerElseHigher(2,5))


# 2 Mesma letra: Escreva uma função que receba uma string com duas palavras e
# retorne True se ambas palavras começarem com a mesma letra. Exemplo:
# mesma_letra(&#39;Cão covarde&#39;) -&gt; True
# mesma_letra(&#39;Vira Lata&#39;) -&gt; False

def checkFirstLetter(text):
    texts = text.lower().split(" ")
    return texts[0][0] == texts[1][0]
    
print(checkFirstLetter("Cão covarde"))
print(checkFirstLetter("Vira Lata"))


# 3 Mestre Yoda: Dada uma sentença, a função deve retornar a sentença com as
# palavras na ordem reversa. Exemplo:
# mestre_yoda(&#39;Eu estou em casa&#39;) --&gt; &#39;casa em estou Eu&#39;
# mestre_yoda(&#39;Estamos prontos&#39;) --&gt; &#39;prontos Estamos&#39;

def phraseInverter(phrase):
    return " ".join(list(reversed(phrase.lower().split(" ")))).capitalize()

print(phraseInverter("Eu estou em casa"))
print(phraseInverter("Estamos prontos"))


# 4 Tem 33: Faça uma função que retorne True se, dada uma lista de inteiros, houver
# em alguma posição da lista um 3 do lado de outro 3. Exemplo:
# tem_33([1,3,3]) --&gt; True
# tem_33([1,3,1,3]) --&gt; False
# tem_33([3,1,3]) --&gt; False


def checkTwoThreeNeighbours(num_list):
    found_three = False
    for num in num_list:
        if found_three and num == 3:
            return True
        found_three = num == 3
    return False

print(checkTwoThreeNeighbours([1,3,3]))
print(checkTwoThreeNeighbours([1,3,1,3]))
print(checkTwoThreeNeighbours([3,1,3]))


# 5 Blackjack: Faça uma função que receba 3 inteiros entre 1 e 11. Se a soma deles for
# menor que 21, retorne o valor da soma. Se for mair do que 21 e houver um 11,
# subtraia 10 da soma antes de apresentar o resultado. Se o valor da soma passar de
# 21, retorne ‘ESTOUROU’. Exemplo:

# blackjack(5,6,7) --&gt; 18
# blackjack(9,9,9) --&gt; &#39;ESTOUROU&#39;
# blackjack(9,9,11) --&gt; 19

def blackJack(card1, card2, card3):
    if(card1 + card2 + card3 > 21):
        if(card1 == 11):
            card1 -= 10
        if(card2 == 11):
            card2 -= 10
        if(card3 == 11):
            card3 -= 10
        if(card1 + card2 + card3 > 21):
            return "ESTOUROU"
        else:
            return card1 + card2 + card3
    else:
        return card1 + card2 + card3


print(blackJack(5,6,7)) 
print(blackJack(9,9,9))
print(blackJack(9,9,11))


# 6 Espião: Escreva uma função que receba uma lista de
# inteiros e retorne True se contém um 007 em ordem, mesmo
# que não contínuo. Exemplo:
# espiao([1,2,4,0,0,7,5]) --&gt; True
# espiao([1,0,2,4,0,5,7]) --&gt; True
# espiao([1,7,2,4,0,5,0]) --&gt; False

def checkSpy(num_list):
    first_zero = False
    second_zero = False
    for num in num_list:
        if second_zero and num == 7:
            return True
        if not second_zero and first_zero and num == 0:
            second_zero = True
        if not first_zero and num == 0:
            first_zero = True
    return False

print(checkSpy([1,2,4,0,0,7,5])) 
print(checkSpy([1,0,2,4,0,5,7])) 
print(checkSpy([1,7,2,4,0,5,0]))