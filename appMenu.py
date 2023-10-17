from estudiante import *
from curso import *
import os

cursos = [
    Curso("POO"),
    Curso("LABO"),
    Curso("Estadisticas")
]

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Ingresar como alumno")
    print("2 - Ingresar como profesor")
    print("3 - Ver cursos")
    print("4 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls")
    if opt.isnumeric():
        if int(opt) == 1:
            ejemplo = Estudiante("Nicolas", "Rodriguez", "jordiENP@gmail.com", "ABC123!", "12345", "2023")
            ejemplo.__str__()
        elif int(opt) == 2:
            pass
        elif int(opt) == 3:
            #veo la llista, selecciono un curso y me devuelve 
            pass
        elif int(opt) == 4:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....")

print("Hasta luego!.")