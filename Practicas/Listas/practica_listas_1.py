## Practica "Listas"

# Ejercicio 1 - Agregar, Reemplazar segundo Elemento, Eliminar ultimo elemento, Mostrar Lista completa, Mostrar cantidad de Elementos.
# 
#

# Lista
lista = ["Maximo", "Matias", "Tomas", "Gabriel", "Lautaro"]

# 1) Función para agregar nombre.
def agregar_nombre():

    # Ingreso de nombre y agregar a la lista.
    nombre_a_cambiar = input("Ingrese un nombre: ").capitalize()
    if nombre_a_cambiar.strip():
        lista.append(nombre_a_cambiar)
    else:
        raise ValueError("Debe ingresar un nombre.")

    # Mostrar el nombre elegido y mostrar nueva lista.
    print(f"Has agregado a la lista el nombre '{nombre_a_cambiar}'")
    print("/- - - Lista - - -/")
    print(lista)

# 2) Función para reemplazar el índice 2 por otro nombre.
def reemplazar_nombre():

    # Ingreso de nombre y reemplazo del segundo índice.
    nombre_de_reemplazo = input("Ingrese un nombre el cual reemplazará al segundo: ").capitalize()
    if nombre_de_reemplazo.strip():
        lista.pop(1)
        lista.insert(1, nombre_de_reemplazo)

    # Levantar 'ValueError' si el usuario no ingresa nada.    
    else:
        raise ValueError("Debe ingresar un nombre.")

    # Mostrar el nombre reemplazado y mostrar nueva lista.
    print(f"Has reemplazado el segundo puesto de la lista por '{nombre_de_reemplazo}'")
    print("/- - - Lista - - -/")
    print(lista)

# 3) Eliminar el ultimo nombre de la lista.
def eliminar_ultimo_nombre():
    
    # Saber si la lista tiene contenido.
    if lista:
        # Eliminar ultimo nombre.
        nombre_eliminado = lista.pop(-1)

        print(f"El nombre eliminado es '{nombre_eliminado}'")
        print("/- - - Lista - - -/")
        print(lista)

    # Levantar 'ValueError' si a lista sí esta vacia.
    else:
        raise ValueError("La lista esta vacia")

# 4) Mostrar la lista.
def mostrar_lista():
    
    # Prints para mostrar lista,
    print("/- - - Lista Completa - - -/")
    print(lista)

# 5) Mostrar cantidad de Elementos en la lista.
def mostrar_cant_elementos():

    # Detectar si es una lista vacia:
    if lista:
        cant_elementos = len(lista)
        print(f"La cantidad de elementos que tiene la lista es de: [{cant_elementos}]")
    else:
        # Levantar 'ValueError' si la lista esta vacia.
        raise ValueError("La lista esta vacia.")
    
## While para crear menu.

print("(- - - - - [Lista de Acciones] - - - - -)")
print("[1] - Agregar nombre.\n[2] - Reemplazar segundo nombre.\n[3] - Eliminar ultimo nombre.\n[4] - Mostrar Lista.\n[5] - Mostrar cantidad de elementos.\n[x] - Salir del Menu.")

comando  = input("Ingrese un valor de la lista de 'Acciones': ").lower()
while comando != "x":

    # Detectar comando seleccionado.
    try:
        if comando == "1":
            print(f"Ha elegido la opción [{comando}] - 'Agregar nombre'")
            agregar_nombre()
        elif comando == "2":
            print(f"Ha elegido la opción [{comando}] - 'Reemplazar segundo nombre'")
            reemplazar_nombre()
        elif comando == "3":
            print(f"Ha elegido la opción [{comando}] - 'Eliminar ultimo nombre'")
            eliminar_ultimo_nombre()
        elif comando == "4":
            print(f"Ha elegido la opción [{comando}] - 'Mostrar Lista'")
            mostrar_lista()
        elif comando == "5":
            print(f"Ha elegido la opción [{comando}] - 'Mostrar cantidad de elementos'")
            mostrar_cant_elementos()
        else:
            print("No ingreso el numero de comando de la lista, intente nuevamente.")

    # Levantar 'ValueError' si el usuario no ingresa el comando.
    except ValueError:
        print("No ha ingresado un valor, intente nuevamente.")
    
    # Seleccionar comando.
    comando = input("Ingrese un valor de la lista de 'Acciones': ").lower()