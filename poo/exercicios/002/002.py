# Declaração da classe
class Gafanhoto:
    '''
  Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade
  para criar uma nova pessoa, use
  variavel = Gafanhoto(nome, idade)
    '''
    def __init__(self, nome = 'vazio', idade = 0): # método construtor

         # DEF É UM MÉTODO AGORA
        # Atributos de instancia
        self.nome = nome
        self.idade = idade

        # Métodos de instancia
        #Self é substituido pelo objeto q chamou
    def aniversario(self): 
        self.idade = self.idade + 1

    def __str__(self): #DUNDER METHOD
        return f"{self.nome} é Gafanhota(o) e tem {self.idade} anos de idade"
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome}; idade = {self.idade}"
        
# Declaração de objetos
g1 = Gafanhoto('Luiza', 20)
g1.aniversario() 
print(g1) # vai chamar o dunder method

g2 = Gafanhoto('Cassio', 28)
print(g2.__dict__) # Dunder attribute
print(g2.__getstate__()) # Dunder method
# Os dois mostram a mesma coisa mas o getstate pode personalizar
print(g2.__class__)  # Dunder attribute
print(g2.__doc__) # Dunder attribute

                              