class Restaurante:
    Restaurante = []

def __init__(self,nome,categoria):
    self.nome = nome
    self.categoria = categoria
    self.ativo = False
    Restaurante.restaurantes.append(self)

def __str__(self):
    return f'{self.nome} | {self.categoria}'

def lister_restaurantes():
    for restaurante in Restaurante.restaurantes
        print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_praca = Restaurante('praca','gourmet')
restaurante_pizza = Restaurante('pizza','italiana')

Restaurante.lister_restaurantes()