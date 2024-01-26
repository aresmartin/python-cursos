#Creación de variables
helloworld = "Hello" + " " + "World"
print(helloworld)

lotofhellos = "hello" * 10
print(lotofhellos)

even_numbers = [1,2,4,8]
odd_numbers = [3,5,7,9]
all_numbers = even_numbers + odd_numbers
print(all_numbers)

print([1,2,3] * 3)

name = "John"
age = 30
print("%s is %d years old." % (name, age))

#this prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)
print(type(mylist))

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f"

print(format_string % data)

astring = "Hello world!"
print("single quotes are ' '")
print(len(astring))

print(astring.index("o"))#pos 4 porque empieza en 0 (del 0-4 = 5)
print(astring.index("H"))#pos 0

print(astring[3:7])
print(astring[3:7:2])#pos 3-7, de 2 en 2

#Imprimir una cadena al reves:
print(astring[::-1])#pos 0-10, de -1 en -1
print(astring.upper())
print(astring.lower())