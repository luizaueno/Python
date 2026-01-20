# Declaração da classe
class Gafanhoto:
    def __init__(self): # método construtor

        # DEF É UM MÉTODO AGORA
        # Atributos de instancia
        self.nome = ""
        self.idade = 0

        # Métodos de instancia
        #Self é substituido pelo objeto q chamou
    def aniversario(self): 
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"
        
# Declaração de objetos
g1 = Gafanhoto()
g1.nome = 'Luiza'
g1.idade = 20
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Cássio'
g2.idade = 28
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())