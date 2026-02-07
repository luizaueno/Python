# Crie uma classe livro que vai simular a passagem de páginas de um livro e vai informar se chegou ao fim

class Livro:
    def __init__(self, titulo = "Book one- A2 level", paginas = 20, pag_atual = 1):
        self.titulo = titulo
        self.paginas = paginas
        self.pag_atual = pag_atual
        print(f"Você acabou de abrir o livro {self.titulo} que tem {self.paginas} páginas no total. Você agora está na página {pag_atual} ")
        
    def avancar_paginas(self):
        
        paginas = int(input('Quantas páginas deseja avançar? '))
    
        if (self.pag_atual >= self.paginas):
            print(f'Você chegou ao fim de {self.titulo} na página {self.paginas}')

        if (paginas == 0):
            print("Leitura encerrada")
            return
        if(self.pag_atual < paginas):
            self.pag_atual += paginas
            print(f"Agora você está na página {self.pag_atual}")

        
            

l1 = Livro("Book one- A2 level", 20)
l1.avancar_paginas()