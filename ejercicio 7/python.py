class Universidad():
    def __init__(self, nombre):
        self.nombre = nombre

class Carrera():
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def __init__(self, nombre_universidad, nombre, edad):
        # Llamamos al constructor de la clase Universidad
        Universidad.__init__(self, nombre_universidad)
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.nombre}")

# Crear una instancia de Estudiante
persona = Estudiante("Harvard", "Mike", 19)
persona.carrera("Ingeniería mecatronica")
persona.datos()
