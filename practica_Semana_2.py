def negativo():
    numero = int(input("Ingrese un número: "))  
    if numero < 0:
        print("El número es negativo.")
    else:
        print("El número no es negativo.")
    
def cuantos_digitos():
    numero = int(input("Ingrese un número: "))
    cantidad_digitos = len(str(abs(numero)))
    print(f"El número tiene {cantidad_digitos} dígitos.")

def es_primo():
    numero = int(input("Ingrese un número: "))
    if numero < 2:
        print("El número no es primo.")
        return
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print("El número no es primo.")
            return
    print("El número es primo.")

def determinar_posicion_lista():
    lista = []
    for i in range(4):
        numero = int(input(f"Ingrese el número {i+1} de 4: "))
        lista.append(numero)
    numero_mayor = max(lista)
    posicion = lista.index(numero_mayor)
    print(f"El número mayor es {numero_mayor} y su posición en la lista es {posicion}.")

def eliminar_duplicados():
    numeros = [1, 1, 2, 3, 3, 2, 5, 6, 2, 7, 8, 4, 3, 1]
    lista = list(set(numeros))
    print(f"Lista original: {numeros}")
    print(f"Lista sin duplicados: {lista}")

def mostrar_menu():
    while True:
        print("\n############### ELIJA UNA OPCIÓN ###############")
        print("1. Determinar si un número es negativo")
        print("2. Saber cuántos dígitos tiene un número")
        print("3. Comprobar si un número es primo")
        print("4. Determinar posición del número mayor en una lista")
        print("5. Eliminar duplicados de una lista de prueba")
        print("6. Salir del programa")
        print("################################################")
        
        opcion = int(input("Ingrese una opción (1-6): "))
        print("-" * 48)

        match opcion:
            case 1:
                negativo()
            case 2:
                cuantos_digitos()
            case 3:
                es_primo()
            case 4:
                determinar_posicion_lista()
            case 5:
                eliminar_duplicados()
            case 6:
                print("Saliendo del programa... ¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")

mostrar_menu()


