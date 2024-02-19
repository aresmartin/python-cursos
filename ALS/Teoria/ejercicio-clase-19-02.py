"""
Un profesor tiene tres notas para cada alumno:
nombre, primer parcial, segundo parcial y proyecto.
Crea un programa que pregunte por las tres notas para
un número indeterminado de alumnos (para terminal, cadena vacía).
Y al final muestre un listado con los alumnos, sus notas y las medias.
Crea dos funciones:
fn1: def pide_notas_alumnos() -> una lista (alumno) de listas (tres notas)
                                una lista (alumno) de tuplas (tres notas)
                                una lista (alumno) de diccionarios:
                                {
                                    "nombre": "Pablo",
                                    "parical1": 5,
                                    "parcial2": 6,
                                    "proyecto": 7
                                }
                                un diccionario (nombre) de diccionarios
                                {
                                    "Pablo": {
                                        "parcial1": 5,
                                        "parcial2": 6,
                                        "proyecto": 7
                                    }
                                }
"""

EQT_PARCIAL1 = "Parcial 1"
EQT_PARCIAL2 = "Parcial 2"
EQT_PRY = "Proyecto"



def pide_notas_alumnos():
    toret = {}
    nombre = " "
    while nombre:
        nombre = input("Nombre del alumno: ").trim() 
        if nombre == "":
            break
        parcial1 = float(input(EQT_PARCIAL1 + ": "))
        parcial2 = float(input("Nota segundo parcial: "))
        proyecto = float(input("Nota proyecto: "))
        alumno = [nombre, parcial1, parcial2, proyecto]
        alumnos.append(alumno)
    return alumnos

def 