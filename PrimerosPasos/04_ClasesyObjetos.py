class myClass:
    variable = "blah"
    def function(self): # self es el equivalente a this en otros lenguajes
        print("This is a message inside the class.")

myobjectx = myClass() #Instanciación de la clase
print(myobjectx.variable)

myobjecty = myClass()
myobjecty.variable = "yackity"
print(myobjecty.variable)
print(myobjectx.variable)
myobjectx.function()