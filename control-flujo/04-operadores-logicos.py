# and, or, not

gas = False
encendido = False
edad = 18

print("Puedes pasar" if gas and encendido else "No puedes pasar")

print("Puedes pasar" if gas or encendido else "No puedes pasar")

print("Puedes pasar" if not gas else "No puedes pasar")


if not gas and (encendido or edad > 17):
    print("Puedes super avansar mi papa")
