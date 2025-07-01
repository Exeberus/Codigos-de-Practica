## Practica "Listas" Bastante-Avanzado

# Ejercicio 3 - Mostrar todos los estudiantes con su nota, Mostrar los estudiantes que aprobaron (nota >= 6.0), Calcular el promedio general del curso, Permitir buscar un estudiante por nombre y mostrar su nota, Permitir agregar un nuevo estudiante con su nota, Mostrar al estudiante con la nota más alta y más baja.
#
#

estudiantes = [
    ["Maximo", 8.5],
    ["Vicky", 6.0],
    ["Santino", 4.5],
    ["Ramiro", 9.2],
    ["Igna", 7.8]
]

# 1) Función para mostrar todos los estudiantes con su nota.

def mostrar_nombres():
    print("/ - - - Estudiantes - - - /")

    # Bucle 'for' para acceder a la lista de listas.
    for estudiante in estudiantes:
        print(f"Estudiante: '{estudiante[0]}' / Nota: '{estudiante[1]}'")

# 2) Función para mostrar todos los estudiantes que aprobaron.

def estudiantes_aprobados():
    print("/ - - - Estudiantes Aprobados - - - /")

    # Bucle 'for' para acceder a la lista de listas.
    for estudiante in estudiantes:
        # Condición 'if' para saber que estudiante aprobo.
        if estudiante[1] >= 6.0:
            print(f"Estudiante: '{estudiante[0]}' Ha aprobado")
        else:
            print(f"Estudiante: '{estudiante[0]}' No ha aprobado")

# 3) Función para promediar las notas.

def promediar_notas():
    print("/ - - - Promedio de notas - - - /")
    notas = 0
    num_estudiantes = 0

    # Bucle 'for' para acceder a la lista de listas.
    for estudiante in estudiantes:
        notas += estudiante[1]
        num_estudiantes += 1

    print(f"El promedio de las notas es: '{notas/num_estudiantes}'")

# 4) Función para buscar estudiante por nombre.

def buscar_nombre():
    busc_nombre = input("Ingrese el nombre que desea buscar: ").capitalize()
    encontrado = True
    i = 0

    # Condición 'if' para saber si el usuario ingreso un nombre
    if busc_nombre:
        # Bucle 'while' para que recorra estudiantes hasta encontrar al estudiante
        while i < len(estudiantes) and encontrado:
            # Condición 'if' para encontrarlo
            if estudiantes[i][0] == busc_nombre:
                print(f"Se ha encontrado a '{busc_nombre}', Su nota es {estudiantes[i][1]}.")
                encontrado = False

            elif estudiantes[i][0] == estudiantes[-1][0]:
                print(f"No se ha encontrado a '{busc_nombre}'.")
            # i+=1 Para seguir recorriendo la lista.
            i+=1

    else:
        # Levantar 'ValueError' si el usuario no ingreso nada.
        raise ValueError("No has ingresado ningun nombre.")
    
# 5) Función para agregar un nuevo estudiante con su nota.

def agregar_estudiante():
    # Variables para ingresar el nuevo estudiante.
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota del estudiante: "))

    # Condición 'if' para saber el usuario ingreso el nombre y la nota
    if nombre and nota:
        estudiante_nuevo = [nombre, nota]
        estudiantes.append(estudiante_nuevo)
    else:
        # Levantar 'ValueError' si el usuario no ambas variables.
        raise ValueError("No has ingresado el o el nombre, o la nota del estudiante.")
    
    print("/ - - - Nueva lista - - - /")
    print(estudiantes)

# 6) Mostrar al estudiante con la nota más alta y más baja.

def notas_ordenadas():
    nota_mayor = estudiantes[0]
    nota_menor = estudiantes[0]

    for i in estudiantes:
        if i[1] > nota_mayor[1]:
            nota_mayor = i
        if i[1] < nota_menor[1]:
            nota_menor = i

    print("/ - - - Lista de mayor y menor nota - - - /")
    print(f"Mayor nota: {nota_mayor}\nMenor nota: {nota_menor}")

## While para crear menu.

print("(- - - - - [Lista de Acciones] - - - - -)")
print("[1] - Mostrar nombre y nota.\n[2] - Mostrar estudiantes que aprobaron.\n[3] - Promediar Notas.\n[4] - Buscar por nombre y mostrar nota.\n[5] - Agregar estudiante con su nota.\n[6] - Notas ordenadas por mayor y menor.\n[c] - Ver lista de comandos.\n[x] - Salir del menú.\n")

comando = input("Ingrese un valor de la lista de 'Acciones': ").lower()
while comando != "x":

    # Detectar comando seleccionado.
    try:
        if comando == "1":
            print(f"Ha elegido la opción [{comando}] - 'Mostrar nombre y nota.'")
            mostrar_nombres()
        elif comando == "2":
            print(f"Ha elegido la opción [{comando}] - 'Mostrar estudiantes que aprobaron.'")
            estudiantes_aprobados()
        elif comando == "3":
            print(f"Ha elegido la opción [{comando}] - 'Promediar Notas.'")
            promediar_notas()
        elif comando == "4":
            print(f"Ha elegido la opción [{comando}] - 'Buscar por nombre y mostrar nota.'")
            buscar_nombre()
        elif comando == "5":
            print(f"Ha elegido la opción [{comando}] - 'Agregar estudiante con su nota.'")
            agregar_estudiante()
        elif comando == "6":
            print(f"Ha elegido la opción [{comando}] - 'Notas ordenadas por mayor y menor.'")
            notas_ordenadas()
        elif comando == "c":
            print(f"Ha elegido la opción [{comando}] - 'Mostrar Lista de Acciones.'")
            print("[1] - Mostrar nombre y nota.\n[2] - Mostrar estudiantes que aprobaron.\n[3] - Promediar Notas.\n[4] - Buscar por nombre y mostrar nota.\n[5] - Agregar estudiante con su nota.\n[6] - Notas ordenadas por mayor y menor.\n[c] - Ver lista de comandos.\n[x] - Salir del menú.\n")
        else:
            print("No ingreso el numero de comando de la lista, intente nuevamente.")

    # Levantar 'ValueError' si el usuario no ingresa el comando.
    except ValueError:
        print("No ha ingresado un valor, intente nuevamente.")
    
    # Seleccionar comando.
    comando = input("Ingrese un valor de la lista de 'Acciones': ").lower()