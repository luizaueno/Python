# Crie uma classe produto 

# Declaração da classe
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        print(f"{self.nome:^30}\n{self.preco:.^30,.2f}","Produto")


# Declaração de objeto
p1 = Produto("Iphone 17 Pro Max", 11500)
p2 = Produto("Ipad pro", 12500)
p1.etiqueta()
p2.etiqueta()