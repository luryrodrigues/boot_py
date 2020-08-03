#Regressão Linear com ScikitLearn
import numpy as np
import matplotlib.pyplot as plt

x = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111, 0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]
y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657, 1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]

x,y=np.array(x).reshape(-1,1),np.array(y).reshape(-1,1)

from sklearn.linear_model import LinearRegression

#treinando o modelo y = ax + b
reg=LinearRegression()
reg.fit(x,y)

#coeficientes estimados
print('a estimado: ',reg.coef_.ravel()[0])   #coef é o termo a
print('b estimado: ',reg.intercept_[0])  #intercept é o termo independente (b)

#predição do modelo
y_pred=reg.predict(x)

#score do modelo
score=reg.score(x,y)    #métrica que diz o quão bom é nosso modelo. É o R² da equação.
print('r²: ',score)

#plot de dados
plt.figure(figsize=(10,5))
plt.plot(x,y,'o',label='Dados originais')
plt.plot(x,y_pred,label='Regressão linear (R2: {:.3f}'.format(score))
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regressão linear com Scikit-Learn')
plt.grid()
plt.show()