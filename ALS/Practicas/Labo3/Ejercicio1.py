"""
Crea una función decodificadora de fechas. Aceptará fechas del estilo “12 Feb 2015”,
 y las convertirá al sistema ISO-8601, es decir, “2015-02-12” en el ejemplo.
"""

def decodif_fechas(fecha):
    fecha = fecha.split()
    meses = {"Ene": "01", "Feb": "02", "Mar": "03", "Abr": "04", "May": "05", "Jun": "06",
             "Jul": "07", "Ago": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dic": "12"}
    mes_a_numero = meses[fecha[1]]
    nueva_fecha = fecha[2] + "-" + mes_a_numero + "-" + fecha[0]
    return nueva_fecha  

print(decodif_fechas("12 Feb 2015"))
