#CÓDIGO1
def funcao_1(num1,num2):
    resultado=num1*num2
    if resultado <=1000:
        return resultado
    else:
        return num1+num2

print(funcao_1(20,30))

#CÓDIGO2
def funcao_2(num):
    numero_anterior=0
    for i in range(num):
        resultado=numero_anterior+i
        print('Número A ', i,'Número B ', numero_anterior,' Resultado: ', resultado)
        numero_anterior=i

print(funcao_2(10))

#CÓDIGO3
def funcao_3(str):
    for i in range(0,len(str)-1,2):
        print('indice[',i,']', str[i])

print(funcao_3('Testando a Função'))

#CÓDIGO4
def funcao_4(lista_numerica):
    print('valor passado ', lista_numerica)
    a=lista_numerica[0]
    b=lista_numerica[-1]
    if a==b:
        return True
    else:
        return False

lista=[10,20,30,40,10]
print(funcao_4(lista))

#CÓDIGO5
class Classe_1:
    def funcao_da_classe_1(self,string):
        dicionario={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        valor=0
        for i in range(len(string)):
            if i>0 and dicionario[string[i]]>dicionario[string[i-1]]:
                valor+=dicionario[string[i]]-2*dicionario[string[i-1]]
            else:
                valor+=dicionario[string[i]]
        return valor

#CÓDIGO6
class A:
    def __init__(self):
        self.calcI(30)
        print('i da Classe A',self.i)

    def calcI(self,i):
        self.i=2*i;

class B(A):
    def __init__(self):
        super().__init__()

    def calcI(self,i):
        self.i=3*i;

b=B()

#CÓDIGO7
class Classe_2():
    def __init__(self,l,w):
        self.a=l
        self.b=w

    def metodo_1(self):
        return self.a*self.b

objeto_1=Classe_2(12,10)