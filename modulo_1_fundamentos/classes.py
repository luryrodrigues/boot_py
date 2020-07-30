#ClassePai
class Formas:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
    def perimetro(self):
        return (2*self.x)+(2*self.y)
    def escala(self,escala):
        self.x=self.x*escala
        self.y=self.y*escala

#Instanciando um objeto na classe Formas
retangulo=Formas(2,3)
print(retangulo.area())
print(retangulo.perimetro())

#criando uma ClasseFilha
class Quadrado(Formas):
    def __init__(self,x):
        self.x=x
        self.y=x
#também posso adicionar novos métodos às classes filhas ou sobrescrever métodos, por exemplo:
    def area(self):
        return self.x*self.x     #sobrescrevi o método área

quadrado_1=Quadrado(3)
print(quadrado_1.area())
print(quadrado_1.perimetro())

#outra forma de criar uma classe filha:
class Quadrado2(Formas):
    def __init__(self,comprimento):
        self.comprimento=comprimento
        super().__init__(comprimento,comprimento) #o super() permite ter acesso aos métodos e atributos da classe pai

quadrado_2=Quadrado2(3)
print(quadrado_2.area())
print(quadrado_2.perimetro())

class Cubo(Quadrado2):
    def area_superficie(self):
        area_face=super().area()
        return area_face*6
    def volume(self):
        area_face=super().area()
        return area_face*self.comprimento

cubo1=Cubo(4)
print(cubo1.area_superficie())
print(cubo1.volume())

#Polimorfismo é a possibilidade do sistema que estamos trabalhando ter várias versões de um mesmo método, por exemplo.

#Verificando Heranças
print(issubclass(Quadrado,Formas))
print(issubclass(Cubo,Formas))
print(issubclass(Formas,Cubo))

#Verificando Instâncias
print(isinstance(quadrado_1,Cubo))
print(isinstance(quadrado_1,Quadrado))