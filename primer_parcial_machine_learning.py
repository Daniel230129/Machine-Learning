def calorias_diarias():    
    personas = ["Pedro", "Carla", "Laura", "José", "Marta"]

    calorias_pedro = (2000, 1800, 2100, 2000, 1900, 2500, 2200)
    calorias_carla = (1500, 1600, 1700, 1550, 1500, 1800, 1900)
    calorias_laura = (2500, 2600, 2400, 2300, 2400, 2500, 2600)
    calorias_jose = (1800, 1900, 2000, 2100, 2000, 1900, 1800)
    calorias_marta = (1300, 1400, 1350, 1250, 1200, 1500, 1600)

    # 1. Relacionar cada persona con sus calorías diarias en un diccionario
    calorias = {
        "Pedro": calorias_pedro,
        "Carla": calorias_carla,
        "Laura": calorias_laura,
        "José": calorias_jose,
        "Marta": calorias_marta,
    }

    #Calcular promedio y evaluar
    for nombre, datos in calorias.items():
        promedio = sum(datos) / len(datos)
        if promedio > 2000:
            print(f"{nombre} tiene consumo alto")
        else:
            print(f"{nombre} tiene consumo dentro del rango recomendado")


def salario_empleados():
    nombres_empleados = ["Juan", "Ana", "Luis", "Nadia", "Nico"]

    horas_juan = (8, 8, 8, 8, 8, 0, 0)
    horas_ana = (9, 9, 9, 9, 9, 4, 0)
    horas_luis = (10, 10, 10, 10, 10, 8, 0)
    horas_nadia = (7, 7, 7, 7, 7, 5, 0)
    horas_nico = (5, 5, 5, 5, 5, 0, 0)

    precio_hora = 375

    # 1. Recorre la lista de empleados e imprime cada nombre
    for nombre in nombres_empleados:
        print(nombre)

    # 2. Crea un diccionario con las horas de cada empleado
    diccionario = {
        "Juan": horas_juan,
        "Ana": horas_ana,
        "Luis": horas_luis,
        "Nadia": horas_nadia,
        "Nico": horas_nico,
    }

    for a, b in diccionario.items():
        print(f"{a}: {b}")

    # 3. Recorre el diccionario e imprime el salario semanal
    for nombre, horas in diccionario.items():
        salario_semanal = sum(horas) * precio_hora
        print(f"{nombre}: {salario_semanal}")

        # 4. Evalúa si supera los 18000
        if salario_semanal > 18000:
            print(f"{nombre} tiene un salario alto")
        else:
            print(f"{nombre} tiene salario bajo")


def menu():
    while True:
        print("\n############### ELIJA UNA OPCIÓN ###############")
        print("1. Calorías diarias")
        print("2. Salario de empleados")
        print("3. Salir del programa")
        print("################################################")
        
        opcion = int(input("Ingrese una opción (1-3): "))
        print("-" * 48)

        match opcion:
            case 1:
                calorias_diarias()
            case 2:
                salario_empleados()
            case 3:
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, ingrese una opción entre 1 y 3.")



