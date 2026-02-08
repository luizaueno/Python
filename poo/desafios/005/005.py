# Crie uma classe Gamer, onde podemos cadastrar nome nick e os jogos favoritos da pessoa, e crie um método de mostrar a ficha

class Gamer:
    def __init__(self, nome, nick, jogos):
        self.nome = nome
        self.nick = nick
        self.jogos = jogos

    def add_favoritos(self):
        self.jogos + 1

    def ficha(self):
        print(f"{'Jogador'}, {self.nick}")
        print(f"{'nome real'}, {self.nome}")
        print(f"{'Jogos favoritos'}, {self.jogos}")
