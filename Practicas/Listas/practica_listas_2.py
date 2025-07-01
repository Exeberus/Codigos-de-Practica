## Practica "Listas" Medio-Avanzado

# Ejercicio 2 - Mostrar los nombres en la intersección de ambas listas, Unir ambas listas (sin duplicados), Ordenar las listas alfabeticamente, Buscador de nombres en la lista
#
#

# Listas
lista1 = ["Vicky", "Juli", "Abril", "Sofi", "Celeste", "Maximo"]
lista2 = ["Maximo", "Matias", "Ramiro", "Santino", "Tomas", "Vicky"]

# 1) Función para sostrar los nombres en la intersección de ambas listas.

def nombre_en_interseccion():
    lista_intersección = []

    # Bucle 'for' para descubrir que nombres se repiten en la lista.
    for n in lista1:
        # Condición 'if' para saber si se repite en lista2 y no esta en lista_intersección.
        if n in lista2 and n not in lista_intersección:
            print(f"Se agrego '{n}'")
            lista_intersección.append(n)

    # Mostrar lista final
    print("/ - - - Intersección de las listas - - - /")
    print(lista_intersección)

# 2) Función para unir ambas listas sin duplicados.

def lista_unida_sin_duplicados():
    # Lista combinada para bucle 'for'
    lista_combinada = lista1+lista2
    lista_unida = []

    # Bucle 'for' para descubrir cuando se duplican los nombre en la lista.
    for n in lista_combinada:
        # Condición 'if' para saber si 'n' no se repite en 'lista_unida'
        if n not in lista_unida:
            print(f"Se agrego '{n}'")
            lista_unida.append(n)
    
    # Mostrar lista final
    print("/ - - - Listas unidas - - - /")
    print(lista_unida)

# 3) Función para ordenar las listas alfabeticamente.

def listas_ordenadas():
    # Juntar ambas listas y ordenar con un '.sort()'
    lista_combinada = lista1+lista2
    lista_ordenada = []
    
    # Bucle 'for' para descubrir cuando se duplican los nombre en la lista.
    for n in lista_combinada:
        # Condición 'if' para saber si 'n' no se repite en 'lista_unida'
        if n not in lista_ordenada:
            lista_ordenada.append(n)

    # Ordenar lista
    lista_ordenada.sort()

    # Mostrar lista Ordenada final
    print("/ - - - Listas Ordenadas Alfabeticamente - - - /")
    print(lista_ordenada)

# 4) Función para buscar un nombre en las listas.

def buscar_nombre():

    lista_combinada = lista1+lista2
    nombre_buscar = input("Ingrese el nombre que desea buscar en la lista: ").capitalize()
    if nombre_buscar:
        if nombre_buscar in lista_combinada:
            print(f"Se ha encontrado a '{nombre_buscar}' en las listas.")
        else:
            print(f"No se encontro a '{nombre_buscar}' en las listas.")
    else:
        raise ValueError("No has ingresado ningun nombre.")

## While para crear menu.

print("(- - - - - [Lista de Acciones] - - - - -)")
print("[1] - Mostrar nombre en intersección.\n[2] - Combinar ambas listas sin duplicados.\n[3] - Ordenar lista alfabeticamente.\n[4] - Buscar nombre en lista.\n[c] - Ver lista de comandos.\n[x] - Salir del menú.\n")

comando = input("Ingrese un valor de la lista de 'Acciones': ").lower()
while comando != "x":

    # Detectar comando seleccionado.
    try:
        if comando == "1":
            print(f"Ha elegido la opción [{comando}] - 'Mostrar nombre en intersección.'")
            nombre_en_interseccion()
        elif comando == "2":
            print(f"Ha elegido la opción [{comando}] - 'ombinar ambas listas sin duplicados.'")
            lista_unida_sin_duplicados()
        elif comando == "3":
            print(f"Ha elegido la opción [{comando}] - 'Ordenar lista alfabeticamente.'")
            listas_ordenadas()
        elif comando == "4":
            print(f"Ha elegido la opción [{comando}] - 'Buscar nombre en lista.'")
            buscar_nombre()
        elif comando == "c":
            print(f"Ha elegido la opción [{comando}] - 'Mostrar Lista de Acciones.'")
            print("[1] - Mostrar nombre en intersección.\n[2] - Combinar ambas listas sin duplicados.\n[3] - Ordenar lista alfabeticamente.\n[4] - Buscar nombre en lista.\n[c] - Ver lista de comandos.\n[x] - Salir del menú.\n")
        else:
            print("No ingreso el numero de comando de la lista, intente nuevamente.")

    # Levantar 'ValueError' si el usuario no ingresa el comando.
    except ValueError:
        print("No ha ingresado un valor, intente nuevamente.")
    
    # Seleccionar comando.
    comando = input("Ingrese un valor de la lista de 'Acciones': ").lower()