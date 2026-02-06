# Crie uma classe produto 

# Declaração da classe
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        largura = 30 
        print("-" * largura) # borda superior 
        print(f"{'Produto':^{largura}}") # palavra Produto centralizada 
        print(f"{self.nome:^{largura}}") # imprime o nome centralizado
        print("*" * largura)
        print(f"{self.preco:^{largura}.2f}") # imprime o preço centralizado
        print("-" * largura) # borda inferior

# Declaração de objeto
p1 = Produto("Iphone 17 Pro Max", 11500)
p2 = Produto("Ipad pro", 12500)
p1.etiqueta()
p2.etiqueta()