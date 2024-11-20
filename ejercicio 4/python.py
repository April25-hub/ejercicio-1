class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def nombre_completo(self):
        print(self.nombre + " " + self.apellido)  # Cambie las comillas angulares por comillas normales

class Estudiante(Persona):
    def __init__(self, nom, ape, carr):
        super().__init__(nom, ape)
        self.carrera = carr

    def mostrar_carrera(self):
        print(self.carrera)

# Ejemplo de uso
estudiante = Estudiante("April", "Arzaba", "Diaz")
estudiante.nombre_completo()  # Debería imprimir "April Arzaba"
estudiante.mostrar_carrera()  # Debería imprimir "ingenieria"
