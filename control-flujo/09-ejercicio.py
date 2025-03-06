numero_guardado = False

while True:
    if numero_guardado:
        print(f"Numero almacenado en memoria {numero_guardado}")
        operacion = input(
            "Ingrese salir para cerrar o \ningrese una operacion\nsuma\nResta\nDiv\nMulti\n-->").lower()
        if operacion != "salir":
            numero_dos = int(input("Ingrese un numero\n-->"))
            if operacion == "suma":
                resultado = numero_guardado + numero_dos
                print(
                    f"La suma entre {numero_guardado} + {numero_dos} = {resultado}")
            elif operacion == "resta":
                resultado = numero_guardado - numero_dos
                print(
                    f"La resta entre {numero_guardado} - {numero_dos} = {resultado}")
            elif operacion == "multi":
                resultado = numero_guardado * numero_dos
                print(
                    f"La multiplicacion entre {numero_guardado} * {numero_dos} = {resultado}")
            elif operacion == "div" and numero_dos != 0:
                resultado = numero_guardado / numero_dos
                print(
                    f"La division entre {numero_guardado} / {numero_dos} = {resultado}")
            numero_guardado = resultado
        else:
            print("Proceso finalizado")
            break
    else:
        numero_guardado = int(input("Ingrese un numero\n-->"))
