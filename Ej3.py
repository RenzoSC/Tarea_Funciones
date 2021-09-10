"""Queremos hacer una función que añada a una lista los contactos de una agenda.

Los contactos se van a guardar en un diccionario, y al menos debe tener el campo de nombre, el campo del teléfono, aunque puede tener más campos.
Los datos se irán pidiendo por teclado, se pedirá de antemanos cuantos contactos se van a guardar.

Si vamos a guardar más información en el contacto, se irán pidiendo introduciendo campos hasta que introduzcamos el "*"."""

contactos = []

def agenda():
    añadir = True
    while añadir:
        cuantosContactos = int(input("¿Cuantos contactos desea agregar?\n"))
        if cuantosContactos >=1:
            while cuantosContactos >=1:
                contactos.append({})
                cuantosContactos-=1
                añadirContactos()
                masInfo()
        else:
            print("Finalizamos tu sesión entonces! Hasta luego :)")
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

agenda()

print("Tu lista de contactos es:")
print(contactos)
