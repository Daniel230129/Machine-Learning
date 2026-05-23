#Daniel Caamaño 23-0129

def lista_de_compras():
    #Crea una lista con 5 productos de supermercado.
    lista_compras = ["manzanas", "pan", "leche", "huevos", "queso"]
    print(f"Lista original: {lista_compras}")
    
    #Inserta un nuevo producto al final.
    lista_compras.append("cereal")
    print(f"Lista después de insertar cereal: {lista_compras}")
    
    #Elimina el segundo producto de la lista.
    lista_compras.remove(lista_compras[1])
    print(f"Lista final: {lista_compras}")

def lista_de_numeros():
    #Crea una lista con los numeros del 1 al 10.
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print (f"Lista original: {lista_numeros}")
    
    #Insertar el numero 99 en la tercera posición.
    lista_numeros.insert(2, 99)
    print(f"Lista después de insertar 99 en la tercera posición: {lista_numeros}")

    #Eliminar el numero 5 de la lista.
    lista_numeros.remove(5)
    print(f"Lista después de eliminar el número 5: {lista_numeros}")

    #Muestra la lista ordenada de mayor a menor.
    lista_numeros.sort(reverse=True)
    print(f"Lista ordenada de mayor a menor: {lista_numeros}")

def lista_de_estudiantes():
    #Crea una lista con los nombres de 5 estudiantes.
    lista_estudiantes = ["Ana", "Luis", "Carlos", "Marta", "Sofia"]
    print(f"Lista original: {lista_estudiantes}")
    
    #Agrega un nuevo estudiante al principio de la lista.
    lista_estudiantes.insert(0, "Jorge")
    print(f"Lista después de agregar Jorge al principio: {lista_estudiantes}")
    
    #Elimina el último estudiante de la lista.
    lista_estudiantes.pop()
    print(f"Lista después de eliminar el último estudiante: {lista_estudiantes}")

    #Muestra el nombre del estudiante que este en la segunda posición.
    print(f"El estudiante en la segunda posición es: {lista_estudiantes[1]}")

def validar_numero_entero():
    while True:
        try:
            #Solicita al usuario que ingrese un número entero por consola
            numero = int(input("Ingrese un número entero: "))
            print(f"El número ingresado es: {numero}")
            break
        except ValueError:
            print("Error: Debes introducir un numero entero valido.")

def menu():
    while True:
        print("\n############### ELIJA UNA OPCIÓN ###############")
        print("1. Lista de compras")
        print("2. Lista de números")
        print("3. Lista de estudiantes")
        print("4. Validar número entero")
        print("5. Salir del programa")
        print("################################################")
        
        opcion = int(input("Ingrese una opción (1-5): "))
        print("-" * 48)

        match opcion:
            case 1:
                lista_de_compras()
            case 2:
                lista_de_numeros()
            case 3:
                lista_de_estudiantes()
            case 4:
                validar_numero_entero()
            case 5:
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, por favor intente nuevamente.")
menu()