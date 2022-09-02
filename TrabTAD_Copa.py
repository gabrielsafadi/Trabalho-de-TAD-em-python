class Jogo:

    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2
        self.placar = [0,1]
      
    def resultado(self):
      return f"{self.time1} ({self.placar[0]}) x ({self.placar[1]}) {self.time2}"


p1 = Jogo("csa", "crb")

print(p1.time1)
print(p1.time2)
print(p1.resultado())
