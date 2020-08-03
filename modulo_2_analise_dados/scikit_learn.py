import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt

df=pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
df['date']=pd.to_datetime(df['date'])
df=df.set_index('date')

#extração de x e y
x, y = df[['temperatura']].values, df[['classification']].values

#pré-processamento
from sklearn.preprocessing import LabelEncoder    #LabelEncoder transforma "labels" em números

#conversão de y para valores numéricos
le=LabelEncoder()   #instanciando a classe
y=le.fit_transform(y.ravel())   #fit gera um mapa para as entradas e transform codifica as entradas. 
#O método ravel() retorna uma vista (view) 1D do array, mas sem modificar o seu conteúdo.

#modelo
from sklearn.linear_model import LogisticRegression   #gera uma função que vai discriminar melhor as classes

#classificador
clf= LogisticRegression()   #instancia a classe LogisticRegression
clf.fit(x,y)    #fit (treinar o modelo) calcula os parâmetros que vao gerar a função que melhor discrimina os dados

#gerando 100 valores de temperatura linearmente espaçados de 0 a 45
x_test=np.linspace(start=0,stop=45,num=100).reshape(-1,1)
#extrapolação do modelo para novos valores de temperatura
y_pred=clf.predict(x_test)

#descodificação do y_pred paara os valores originais
y_pred=le.inverse_transform(y_pred)

#output
output={'new_temp':x_test.ravel(), 'new_class':y_pred.ravel()}
output=pd.DataFrame(output)   #transforma em uma tabela
print(output.head())

#contagem de valores gerados
output['new_class'].value_counts().plot.bar(figsize=(10,5),rot=0,title='Classificação de temperaturas')
plt.show()

#boxplot
output.boxplot(by='new_class',figsize=(10,5),title='Classificação de temperaturas')
plt.show()