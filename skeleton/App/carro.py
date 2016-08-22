
class Carro():
    numero_puertas = 0
    numero_llantas = 0
    tipo_transmision = ''
    color = ''
    estilo = ''
    marca = ''
    modelo = 0
    tamanio_motor = 0

    def __init__(self,numero_puertas):
        self.numero_puertas =numero_puertas

  
  
    def arrancar(self):
        print 'ENCENDIDO!!!!'

    def acelerar(self):
        print 'ACELERO!!!!!!'

    def frenar(self):
       print 'FRENO!!!!!!!!!'

    def bocinar(self):
       print 'Piiiiiiiipppp!!!!'

class Moto(Carro):
    tipo_casco = ''
    pass 
    
   


pichirilo = Carro(4)
pichirilo.arrancar()
pichirilo.acelerar()
pichirilo.frenar()
pichirilo.bocinar()
print pichirilo.numero_puertas


pedorra = Moto(0)
pedorra.arrancar()







