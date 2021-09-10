"""Realizar una función recursiva que reciba una lista y que calcule el producto de los elementos de la lista:"""

def producto(lista):
    if lista == []:
        return 1
    else:
        numero = lista.pop(0)
        return numero * producto(lista)

print(producto([8,9,10]))