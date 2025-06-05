class Juego:
    def __init__(self, ataque, defensa, bonus):
        self.puntos_ataque = ataque
        self.puntos_defensa = defensa
        self.puntos_bonus = bonus

    def calculate_total_score(self):
        total = self.puntos_ataque + self.puntos_defensa + self.puntos_bonus
        return total

juego = Juego(100, 75, "50")
print("Total de puntos:", juego.calculate_total_score())
