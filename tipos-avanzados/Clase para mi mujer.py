# Programa realizado por FABIAN DARIO FLOREZ RAIGOSO
# ID 711595

import random

# Inicialización de estructuras de datos
cupo = [0] * 81  # 0: vacío, 1: ocupado (índices 1-80)
placa = [''] * 81
time_hora = [0] * 81
time_minuto = [0] * 81


def bienvenida():
    print("|******************************************************|")
    print("|                    BIENVENIDO                        |")
    print("|               Parqueadero SAN JORGE                  |")
    print("|******************************************************|")
    input("Presione ENTER para continuar...")
    print("|                                                      |")


def menu():
    print("\n|******************************************************|")
    print("|                      MENU                            |")
    print("| 1. Agregar entrada de vehículo                      |")
    print("| 2. Agregar salida de vehículo                       |")
    print("| 3. Mostrar estado de parqueaderos                   |")
    print("| 4. Buscar vehículo                                  |")
    print("| 5. Salir del programa                               |")
    print("|******************************************************|")
    return int(input("Seleccione una opción: "))


def menu_zona():
    print("|******************************************************|")
    print("|                  SELECCIONE ZONA                     |")
    print("| 1. Aleatorio                                        |")
    print("| 2. Norte                                            |")
    print("| 3. Sur                                              |")
    print("|******************************************************|")
    return int(input("Seleccione zona: "))


def place_plaza(plaza_cliente):
    if (1 <= plaza_cliente <= 21) or (49 <= plaza_cliente <= 63):
        return "NORTE"
    else:
        return "SUR"


def plaza_sistema(zona_plaza, cupo):
    while True:
        moros = random.randint(1, 80)
        valid = False
        if zona_plaza == 1:
            if cupo[moros] == 0:
                valid = True
        elif zona_plaza == 2:
            if (1 <= moros <= 21 or 49 <= moros <= 63) and cupo[moros] == 0:
                valid = True
        elif zona_plaza == 3:
            if (22 <= moros <= 48 or 64 <= moros <= 80) and cupo[moros] == 0:
                valid = True

        if valid:
            print(
                f"|               Parqueadero {moros}, piso {place_plaza(moros)}             |")
            return moros


def parking_full(cupo):
    return sum(cupo[1:81])


def calcular_tiempo(hora_entrada, min_entrada, hora_salida, min_salida):
    x1 = 60 - min_entrada
    x2 = hora_entrada + 1
    x3 = hora_salida - x2
    x4 = x3 * 60
    return x1 + x4 + min_salida


def buscar_placa(placa_busq, placa):
    for i in range(1, 81):
        if placa[i] == placa_busq:
            return i
    return None


def mostrar_parqueaderos(cupo):
    x = []
    for i in range(1, 81):
        x.append("VACIO" if cupo[i] == 0 else "OCUPADO")

    print("|******************** ESTADO PARQUEADEROS *************|")
    for i in range(0, 80, 5):
        line = "|"
        for j in range(5):
            idx = i + j + 1
            if idx > 80:
                break
            line += f" {idx:2}. {x[idx-1]:6} |"
        print(line)
        print("|                                                      |")
    input("Presione ENTER para continuar...")


# Programa principal
bienvenida()

# Inicialización de datos
for i in range(1, 81):
    cupo[i] = 0
    time_hora[i] = 0
    time_minuto[i] = 0

menu_open = True
while menu_open:
    try:
        opcion = menu()

        if opcion == 1:
            if parking_full(cupo) == 80:
                print("| Parqueadero lleno! |")
            else:
                print("|************ AGREGAR ENTRADA ************|")
                zona = menu_zona()
                plaza_asignada = plaza_sistema(zona, cupo)
                cupo[plaza_asignada] = 1
                placa[plaza_asignada] = input("Ingrese placa: ").upper()
                time_hora[plaza_asignada] = int(
                    input("Hora de entrada (0-23): "))
                time_minuto[plaza_asignada] = int(
                    input("Minuto de entrada (0-59): "))
                print(f"| Vehículo registrado en plaza {plaza_asignada} |")
                input("Presione ENTER para continuar...")

        elif opcion == 2:
            print("|************ AGREGAR SALIDA *************|")
            p = input("Ingrese placa: ").upper()
            plaza_cliente = buscar_placa(p, placa)

            if plaza_cliente:
                h_s = int(input("Hora de salida (0-23): "))
                m_s = int(input("Minuto de salida (0-59): "))
                tiempo = calcular_tiempo(
                    time_hora[plaza_cliente], time_minuto[plaza_cliente], h_s, m_s)
                total = tiempo * 220
                print(f"| Total a pagar: ${total} |")
                cupo[plaza_cliente] = 0
                placa[plaza_cliente] = ''
                time_hora[plaza_cliente] = 0
                time_minuto[plaza_cliente] = 0
            else:
                print("| Placa no encontrada |")
            input("Presione ENTER para continuar...")

        elif opcion == 3:
            mostrar_parqueaderos(cupo)

        elif opcion == 4:
            p = input("Ingrese placa: ").upper()
            plaza_cliente = buscar_placa(p, placa)
            if plaza_cliente:
                print(
                    f"| Plaza: {plaza_cliente} ({place_plaza(plaza_cliente)}) |")
                print(
                    f"| Hora entrada: {time_hora[plaza_cliente]:02d}:{time_minuto[plaza_cliente]:02d} |")
            else:
                print("| Placa no encontrada |")
            input("Presione ENTER para continuar...")

        elif opcion == 5:
            print("|*************** HASTA LUEGO ***************|")
            menu_open = False

        else:
            print("Opción inválida")

    except ValueError:
        print("Entrada inválida, intente nuevamente")

print("Programa finalizado")
