class Mano():
    numero_dedos = 5
    color_tez = 'moreno'
    numero_unias = 5

    def golpear(self):
        print 'Punetazo'

class Pie():
    numero_dedos = 6
    talla = 38

    def patear(self):
        print 'Pateo'


class Cuerpo(Pie, Mano):
    estatura = 1.7

    def mover(self, metros):
        print 'Me muevo', metros, 'metros'


alex = Cuerpo()
alex.mover(1000)
print alex.estatura
print alex.numero_dedos

    
