class Ponto:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.zone = 0
        self.number = 0
        self.pertence = []


    def tuple_to_point(self, tupla):
        self.x = tupla[0]
        self.y = tupla[1]
        self.number = tupla[2]
        self.zone = tupla[3]

