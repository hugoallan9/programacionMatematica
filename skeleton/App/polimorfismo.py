class Ave():
    def __init__(self, color = 'rojo'):
        self.color = color

    def mover(self):
	print 'A volar'

class Reptil():
    def __init__(self, numero_patas = 0):
	self.numero_patas = numero_patas

    def mover(self):
	print 'Arrastro'

class Animal():
    especie = ''
    sexo = ''
    peso = 0

    def desplazar(self, animal):
	animal.mover()
        


pajaro = Ave('azul')
print pajaro.color
