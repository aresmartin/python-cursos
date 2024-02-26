"""
Crea una función decodificadora de fechas. Aceptará fechas del estilo “12 Feb 2015”,
 y las convertirá al sistema ISO-8601, es decir, “2015-02-12” en el ejemplo.
"""


def codif_fechas():
    fecha = input("Ingrese la fecha: ")
    fecha = fecha.split()
    meses = {"Ene": "01", "Feb": "02", "Mar": "03", "Abr": "04", "May": "05", "Jun": "06",
             "Jul": "07", "Ago": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dic": "12"}
    fecha[1] = meses[fecha[1]]
    fecha = "-".join(fecha)
    print(fecha)


codif_fechas()
