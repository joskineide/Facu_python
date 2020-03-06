asd = {123, 321, 123}

print(asd)

#EXERCÍCIO 1 

#I
def empty_list():
    return []
print(empty_list())

#II
def singleton(el):
    return [el]

singl_list = input("Digite alguma coisa para colocar numa lista de um elemento só: ")

print(singleton(singl_list))

#III
def contains(lst, el):
    for element in lst:
        if element == el:
            return True
    return False


lst = input("Digite uma frase: ").split()

el = input("Digite uma frase para procurar nesta frase: ")

print(contains(lst, el))


#IV 
def is_subset(lstx, lsty):
    for ely in lsty:
        contains = False
        for elx in lstx:
            if elx == ely:
                contains = True
        if not contains:
            return False
    return True

lstx = input("Digite uma frase: ").split()

lsty = input("Digite uma sub frase: ").split()

print(is_subset(lstx, lsty))


#V 
def length(lst):
    count = 0
    for el in lst:
        count += 1
    return count

def equals(lstx, lsty):
    if length(lstx) != length(lsty):
        return False
    count = 0
    for el in lstx:
        if lstx[count] != lsty[count]:
            return False
    return True


lstx = input("Digite uma frase: ").split()

lsty = input("Digite uma frase igual: ").split()

print(equals(lstx, lsty))


#VI

def contains(lst, el):
    for element in lst:
        if element == el:
            return True
    return False


def union(lstx, lsty):
    for el in lsty:
        if not contains(lstx, el):
            lstx.append(el)
    return lstx
        

lstx = input("Digite uma frase: ").split()

lsty = input("Digite uma frase para adicionar: ").split()

print(union(lstx, lsty))



#VII

def contains(lst, el):
    for element in lst:
        if element == el:
            return True
    return False


def inter(lstx, lsty):
    result = []
    for el in lsty:
        if contains(lstx, el):
            result.append(el)
    return result
        

lstx = input("Digite uma frase: ").split()

lsty = input("Digite uma frase com palavras em comum: ").split()

print(inter(lstx, lsty))