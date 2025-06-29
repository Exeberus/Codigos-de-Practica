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

lista_unida_sin_duplicados()