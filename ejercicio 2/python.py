class Persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def cumpleaños(self):
        self.edad += 1

p = Persona(input("Ingrese nombre: "), int(input("Ingrese edad: ")))
p.cumpleaños()  # Incrementa la edad una vez
p.cumpleaños()  # Incrementa la edad otra vez
print(f"{p.nombre} cumple {p.edad} años")
