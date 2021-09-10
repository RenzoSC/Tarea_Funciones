"""Amplía el programa anterior para hacer una función de búsqueda, que reciba un conjunto de parámetros keyword 
y devuelve los contactos (en una lista) que coincidan con los criterios de búsqueda."""

contactos = []

def agenda():
    añadir = True
    while añadir:
        cuantosContactos = int(input("¿Cuantos contactos desea agregar?(ingrese '0' para finalizar)\n"))
        if cuantosContactos >=1:
            while cuantosContactos >=1:
                contactos.append({})
                cuantosContactos-=1
                añadirContactos()
                masInfo()
        else:
            print("Finalizamos tu sesión entonces! Hasta luego :)")
            print(contactos)
            añadir = False

def añadirContactos():
    nombre = input("Ingrese el nombre de su contacto:\n")
    telefono = int(input("Ingrese el número de teléfono:\n"))
    x= len(contactos) -1
    contactos[x]["Nombre"] = nombre
    contactos[x]["Teléfono"] = telefono
    
def masInfo ():
    bandera = True
    while bandera:
        resp = input("Desea agregar más información del contacto?(Escriba '*' para terminar, 'si' para confirmar)\n")
        if resp.lower() == "si":   
            etiqueta = input("Ingrese una etiqueta\n")
            informacion = input("Ingrese la información\n")
            x = len(contactos) -1
            contactos[x][etiqueta] = informacion
        else:
            bandera = False

inicio = True

while inicio:
    print("¿Deseas 'agendar' o 'filtrar' en tu lista de contactos? (terminar con 'x')")
    resp_inicial = input()
    if resp_inicial.lower() == "agendar":
        agenda()
    elif resp_inicial.lower() == "filtrar":
        print("Ingresa los criterios para filtrar")
        keys = []
        values = []
        filtrado = []
        continuar = True
        while continuar:
            key = input("Clave:\n")
            value = input("Valor:\n")
            terminar = input("Para terminar ingrese 'x' sino aprete cualquier botón\n")
            if terminar == "x":
                continuar = False
            else:
                pass

            keys.append(key)
            values.append(value)
        for contacto in contactos:
            for i in range(0, len(keys)):
                k = keys[i]
                try:
                    if contacto[k] == values[i]:
                        filtrado.append(contacto["Nombre"])
                except KeyError:
                    pass
        print("La lista de personas que cumplen con tu filtrado es:")
        print(filtrado)
    else:
        inicio=False            

