class Jogo():

    #times e placar (placar começa em 0x0)
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2
        self.placar = [0,0]
        return None

    #marca gol para o time 1
    def gol_time1(self):
        self.placar[0] += 1
        return self.placar
    
    #marca gol para o time 2
    def gol_time2(self):
        self.placar[1] += 1
        return self.placar

     #retorna resultado do jogo
    def resultado(self):
        return f"{self.time1} ({self.placar[0]}) x ({self.placar[1]}) {self.time2}"

    #retorna o vencedor de acordo com o número de gols e retorna caso seja empate
    def vencedor(self):
        if self.placar[0] > self.placar[1]:
            return self.time1
        elif self.placar[0] < self.placar[1]:
            return self.time2
        else:
            return "Empate!"

#recebendo times
time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")

#armazenando os times
partida = Jogo(time1, time2)

#marcando gols (adicione de acordo com os gols da partida)
partida.gol_time1()
partida.gol_time2()
partida.gol_time1()

#printando resultados e vencedor
print(partida.resultado())
print(partida.vencedor())
print(partida)