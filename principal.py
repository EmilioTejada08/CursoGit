"""
Programa principal para realizar operaciones matemáticas.
"""
import math
import funciones.matematicas

print("Bienvenido a mi programa.")
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

print("------------------------------")

op = input("¿Qué operación quieres realizar? ")
match op:
    case "suma":
        funciones.matematicas.sumar(num1, num2)
    case "resta":
        funciones.matematicas.restar(num1, num2)
    case "multiplicación":
        funciones.matematicas.multiplicar(num1, num2)
    case "división":
        funciones.matematicas.dividir(num1, num2)
    case "potencia":
        funciones.matematicas.potencia(num1, num2)
    case "raíz":
        print(f"La raíz cuadrada de {num1} es {math.sqrt(num1)}")
        print(f"La raíz cuadrada de {num2} es {math.sqrt(num2)}")
    case "módulo":
        funciones.matematicas.modulo(num1, num2)
    case "División entera":
        funciones.matematicas.division_entera(num1, num2)
    case _:
        print("Operación no reconocida.")
