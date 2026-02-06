# Crie uma classe chamada churrasco, informe quantas pessoas vao participar e mostre o quanto de carne deve comprar, o custo total e o preço por pessoa



#Criação de classe

class Churrasco: 
    def __init__(self, title = "Churras dos amigos", pessoas = 2):
        self.title = title
        self.pessoas = pessoas
        pessoas = int(input(f'Quantas pessoas vão participar? '))
        self.pessoas = pessoas

    def analisar(self, quantidade = 0.4, preco = 82.40):
        largura = 20
        print(f"{'-'*20} {self.title:^{largura}} {'-'*20}")
        print(f"Analisando {self.title} com {self.pessoas} convidados")
        print(f"Cada participante comerá {quantidade}Kg e cada Kg custa R${preco}")
        compra = quantidade * self.pessoas
        print(f"Recomendo comprar {compra}Kg de carne")
        custo = preco * compra
        print(f"O custo total será de R${custo:.2f}")
        preco_individual = quantidade * preco
        print(f"Cada pessoa pagará R${preco_individual} para participar")
        print("-" * 60)

Churras = Churrasco()
Churras.analisar()