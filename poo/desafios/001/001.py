# Crie uma classe funcionario com atributos nome setor e cargo e método de se apresentar

# Declaração de classe
class Funcionario:
    # Atributos de classe - serve para todos os objetos da classe
    empresa = "L.A Tech"

    def __init__(self, nome, cargo, setor):

        # Atributos de instancia - específicos do objeto, únicos
        self.nome = nome
        self.cargo = cargo
        self.setor = setor
        
    def apresentacao(self) -> str:
        return f"Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa} "
    
# Declaração de objetos 
f1 = Funcionario("Luiza", "Engenheira de software embarcados", "TI")
print(f1.apresentacao())
f2 = Funcionario("Larissa", "Fotógrafa", "Marketing")
print(f2.apresentacao())
