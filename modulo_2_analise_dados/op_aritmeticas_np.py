import numpy as np

#multiplicação elementar
dim=(2,2)
x=np.ones(dim)
y=np.eye(2)

print(f'Multiplicação de elementos de 2 arrays:\n{x*y}')
print(f'Multiplicação com float/int:\n{x*2}') #broadcasting

#multiplicação matricial
print(f'Multiplicação matricial np.dot:\n{np.dot(x,y)}')
print(f'Multiplicação matricial @:\n{x@y}')
print(f'Multiplicação matricial .dot:\n{x.dot(y)}')

#matriz só de 10
print(f'Matriz contendo apenas 10:\n{10 * np.ones(dim)}')

'''Solução de um sistema de equações:
    1a + 2b = 7
    3a - 2b = -11
    solução: (a,b)=(-1,4)
  Matricialmente essse problema tem a seguinte forma:
  yx=c, onde:
  x= [a,b]
  y=[[1,2],[3,-2]]
  c=[7,-11]'''
y=np.array([[1,2],[3,-2]])
c=np.array([7,-11])
#x= matriz inversa de y * c
y_inv=np.linalg.inv(y)
x=np.dot(y_inv,c)
print(f'Solução do sistema de equações: (a,b) = {x}')

