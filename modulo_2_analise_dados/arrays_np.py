import numpy as np

#help(np) -> ajuda sobre o módulo

#criação de um array 1D
print('ARRAY 1D')
l=[1,2,3]
x=np.array(l)
print(f'x: {x}')
print(f'Shape: {x.shape}')  #shape: quantidade de elementos em cada dimensão
print(f'Tipo: {type(x)}')

#criação de array 2D, listas aninhadas
print('ARRAY 2D')
l=[[1,2],[3,4]]  #cada lista representa uma linha da matriz
x=np.array(l)
print(f'x: {x}')
print(f'Shape: {x.shape}')

#arrays contendo apenas 0
print('ARRAY DE ZEROS')
dim=(2,2) #(linhas,colunas)
x=np.zeros(dim,dtype=int)
print(f'x: {x}')
print(f'Shape: {x.shape}')

#arrays contendo apenas 1
print('ARRAY DE UNS')
dim=(2,3)
x=np.ones(dim, dtype=int)
print(f'x: {x}')
print(f'Shape: {x.shape}')

#criação de valores dentro de um intervalo
print('ARRAY COM INTERVALO')
x_min,x_max=5,15
x=np.linspace(start=x_min,stop=x_max,num=6,dtype=int)   #6 números linearmente espaçados começando em um número mínimo e terminando em um máximo
print(f'x: {x}')
print(f'Shape: {x.shape}')

#criação de matriz identidade (diagonal 1, e o restante 0)
print('ARRAY COM INTERVALO')
x=np.eye(4,dtype=int)
print(f'x: {x}')
print(f'Shape: {x.shape}')

#criação de valores aleatórios
print('ARRAY COM VALORES ALEATÓRIOS')
dim=(2,3)
x=np.random.random(dim)  #retorna valores aleatórios entre 0 e 1
print(f'x: {x}')
print(f'Shape: {x.shape}')

#slicing em arrays 2D
print('SLICING MATRIZ')
x=np.linspace(start=10,stop=100,num=10,dtype=int)  #retorna um array 1D
x=x.reshape(2,5)   #rearranja o array
print(f'x: {x}')
print(f'Shape: {x.shape}')

#extração de elementos na matriz
print(f'Primeira linha e segunda coluna: {x[0,1]}')

#slicing matriz: extração de subarrays
print(f'Primeira linha, segunda a quarta coluna: {x[0,1:4]}')
print(f'Última coluna inteira: {x[:,-1]}')   #só o dois pontos significa "inteira", [:2] significa de 0 a 2 e [2:] de 2 ao fim
print(f'Primeira linha inteira: {x[0,:]}')

#compartilhamento de memória em subarrays
x=np.array([1,2,3])
print(f'Array X antes: {x}')
y=x[:2]
y[0]=-100  #a alteração do valor em y altera x
print(f'Array X depois: {x}')
#para que esse problema não aconteça, utiliza-se o copy()
x=np.array([1,2,3])
print(f'Array X antes: {x}')
y=x[:2].copy()
y[0]=-100  #depois de usar o copy(), a alteração do valor em y não altera x
print(f'Array X depois: {x}')
