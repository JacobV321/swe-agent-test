class Personaje:
    #atributos
    nombre = ""
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    estilo = ""
    
    #constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    #metodos
    def showAtributos():
        print(self.nombre, ":", sep="")
        print("fuerza:", self.fuerza)
        print("inteligencia:", self.inteligencia)
        print("defensa:", self.defensa)
        print("vida:", self.vida)
        
    #metodo
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = fuerza + self.fuerza
        self.inteligencia = inteligencia + self.inteligencia
        self.defensa = defensa + self.defensa
        
mi_personaje = Personaje("rarc", 50, 50, 50, 75)
mi_personaje.showAtributos()

print("-------------")

