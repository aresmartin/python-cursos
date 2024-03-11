"""
Un almacén guarda piezas de fontanería (con un valor común que es el coste), en concreto tuberías (longitud), 
tuercas (ancho), y codos (ángulo). Es necesario llevar un servicio de inventario que permita el alta, baja y 
modificación de piezas. Crea la jerarquía de herencia necesaria para las piezas, y para la clase Inventario, 
reescribe los métodos necesarios, de tal forma que se comporte como una lista de piezas.
"""
class PiezaFontaneria:
    def __init__(self, coste):
        self.coste = coste

    def __str__(self):
        return  f"Coste: {self.coste}"
    
class Tuberia(PiezaFontaneria):
    def __init__(self, coste, longitud):
        super().__init__(coste)
        self.longitud = longitud

    def __str__(self):
        return f"Tubería - Longitud: {self.longitud}, {super().__str__()}"
    
class Tuerca(PiezaFontaneria):
    def __init__(self, coste, ancho):
        super().__init__(coste)
        self.ancho = ancho

    def __str__(self):
        return f"Tuerca - Ancho: {self.ancho}, {super().__str__}"
    
class Codo(PiezaFontaneria):
    def __init__(self, coste, angulo):
        super().__init__(coste)
        self.angulo = angulo

    def __str__(self):
        return f"Codo - Ángulo: {self.angulo}, {super().__str__}"
    
class Inventario:
    def __init__(self):
        self.piezas = []

    def agregar_pieza(self, pieza):
        self.piezas.append(pieza)
    
    def eliminar_pieza(self, pieza):
        if pieza in self.piezas:
            self.piezas.remove(pieza)
        else:
            print("La pieza no esta en el inventario")
    
    def modificar_pieza(self, pieza_vieja, pieza_nueva):
        if pieza_vieja in self.piezas:
            index = self.piezas.index(pieza_vieja)
            self.piezas[index] = pieza_nueva

    def mostrar_inventario(self):
        for i, pieza in enumerate(self.piezas):
            print(f"{i + 1}. {pieza}")

if __name__ == "__main__":

    inventario = Inventario()
    tuberia1 = Tuberia(10, 5)
    tuerca1 = Tuerca(2, 3)
    codo1 = Codo(3, 90)

    inventario.agregar_pieza(tuberia1)
    inventario.agregar_pieza(tuerca1)
    inventario.agregar_pieza(codo1)

    inventario.mostrar_inventario()

    nueva_tuerca = Tuerca(1, 4)
    inventario.modificar_pieza(tuerca1, nueva_tuerca)

    inventario.mostrar_inventario()

    inventario.eliminar_pieza(codo1)

    inventario.mostrar_inventario()