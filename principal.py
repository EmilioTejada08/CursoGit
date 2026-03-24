"""
Programa principal para realizar operaciones matemáticas.
"""
import funciones.matematicas as matematicas

print("Bienvenido a mi programa.")
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

print("------------------------------")

op = input("¿Qué operación quieres realizar? ")
match op:
    case "suma":
        matematicas.sumar(num1, num2)
    case "resta":
        matematicas.restar(num1, num2)
    case "multiplicación":
        matematicas.multiplicar(num1, num2)
    case "división":
        matematicas.dividir(num1, num2)
    case "potencia":
        matematicas.potencia(num1, num2)
    case "raíz":
        matematicas.raiz(num1, num2)
    case "módulo":
        matematicas.modulo(num1, num2)
    case "División entera":
        matematicas.division_entera(num1, num2)
    case _:
        print("Operación no reconocida.")
