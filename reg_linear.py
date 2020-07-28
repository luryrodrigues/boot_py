#Regressão Linear com NumPy
import matplotlib.pyplot as plt  #visualização de dados
import numpy as np

x = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111, 0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]
y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657, 1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]

#plot de dados
plt.figure(figsize=(10,5))  #instancia um objeto figura e define o tamanho
plt.plot(x,y,'o',label='Dados originais')  #plotando os dados. 'o' é scatterplot, se tirar ele plota do tipo linha
plt.legend()  #para expor o label 'Dados originais'
plt.xlabel('X')  #nome do eixo X
plt.ylabel('Y')  #nome do eixo Y
plt.grid()  #desenha as grids na figura

#A regressão linear é calculada pela matriz pseudo inversa de X multiplicada por Y:  Xbeta=y
#A pseudo-inversa de X pode ser dada pelo método np.linalg.pinv(X)
#beta= pseudo-inv*y

#Iremos estimar uma função do tipo y=a*x+1*b
#transformando para numpy e vetor coluna
x,y=np.array(x).reshape(-1,1), np.array(y).reshape(-1,1)   #o -1 indica que quero ignorar a qtd de linhas

#adicionando bias: para estimar o termo b
X=np.hstack((x,(np.ones(x.shape))))  #adc coluna de 1 no array x. Pois o B é multiplicado por 1 na função  O hstack concatena 2 arrays

#estimando a e b:
beta=np.linalg.pinv(X).dot(y)
print('a estimado: ', beta[0][0])
print('b estimado: ', beta[1][0])

#plotando com o método
plt.figure(figsize=(10,5))
plt.plot(x,y,'o',label='Dados originais')
plt.plot(x,X.dot(beta),label='Regressão linear')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regressão Linear com NumPy')
plt.grid()
plt.show()