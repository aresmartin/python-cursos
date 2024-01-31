#Crear una lista simple
a = ["spam", "e.mail", 100, 1234]
#print(a)
#print("Num elementos2:" + str(len(a)))#convertir a str

a[2] = a[2] + 23
#print("Tercer elemento cambiado: ", a)

a[0:2] = [1, 12]
#print("Primeros dos elementos cambiados: ", a)

a[0:2] = []
#print("Primeros dos elementos eliminados: ", a)
a[1:1] = ["bleh", "bleh"]
#print("Elementos insertados: ", a)

#Insertar una copia de la lista al comienzo
a[:0] = a
#print("Insertar una copia de la lista al comienzo: ", a)

def printList(l):
    for i in l:
        print(i)

list = [1, 2, 3, 4, 5]
#printList(list)

list = range(2)
#printList(list)

list = range(3, 6)
#printList(list)

list = ["Martin", "Lucia"]
#printList(list)

list = range(1, 10, 2)
#printList(list)

#Cuando se necesite conteo hacia atras --> reversed(range())
list = reversed(range(3))
#printList(list)

#Métodos para menejo de listas: append, del y pop.
#append: agrega un elemento al final de la lista

#print("Pila: ")
miPila = [1,2]
#print(miPila)

print("Insertando un elemento: ")
miPila.append(3)
#print(miPila)

print("Eliminando un elemento:")
miPila.pop()
#print(miPila)

print("Eliminando un elemento:")
miPila.pop()
#print(miPila)

print("Eliminando un elemento:")
miPila.pop()
#print(miPila)

print("Pila: ")
miPila = [1,2]

print("Insertando un elemento: ")
miPila.append(4)
print(miPila)

print("Eliminando un elemento: ")
miPila.pop(0)
print(miPila)

print("Eliminando un elemento: ")
miPila.pop(0)
print(miPila)

print("Eliminando un elemento: ")
miPila.pop(0)
print(miPila)


