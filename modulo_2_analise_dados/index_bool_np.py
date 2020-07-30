import numpy as np

#indexação booleana
x=np.array([[1,3,7],[4,11,21],[42,8,9]])
print(f'Array X:\n{x}')
k=2
cond=x>k
print(f'Array X é maior que {k}?\n{cond}')
print(f'Array > {k}\n{x[cond]}')
print(f'{len(x[cond])} elementos que são maiores que {k}!')

cond=(x%2==0)
print(f'Array X somente com os números pares\n{x[cond]}')

#operações úteis numpy
print('Rearranjo de matriz')
y=x.reshape(9,1)
print(y)

print('Transposição de matriz')
y=x.T
print(y)

print('Soma de elementos e eixos')
y=np.sum(x) #soma todos os elementos
print(f'Soma dos elementos:\n{y}')
y=np.sum(x,axis=0)  #axis=0: linha  
print(f'Soma das linhas:\n{y}')
y=np.sum(x,axis=1)  #axis=1: coluna
print(f'Soma das colunas:\n{y}')

print('Média')
y=np.mean(x)
print(f'Média dos elementos:\n{y}')
y=np.mean(x,axis=0)
print(f'Média das linhas:\n{y}')
y=np.mean(x,axis=1)
print(f'Média das colunas:\n{y}')

print('Indentificando índices')
cond = (x%2==0)
i,j=np.where(cond)
print(f'índice i - linhas: {i}\níndice j - colunas: {j}')
i_row=np.where(np.sum(cond,axis=1))[0]  #[0]: só quero o número da linha, e não da coluna
print(np.sum(cond,axis=1))
print(f'índice das linhas que possuem nº pares: {i_row}')
print(f'Linhas que possuem nº pares:\n{x[i_row,:]}') #slicing
