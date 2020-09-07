import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('https://pycourse.s3.amazonaws.com/bike-sharing.csv')

'''print(df.head())

print('Qual o tamanho desse dataset?')
print(df.info())

print('Qual a média da coluna windspeed?')
print(df['windspeed'].describe())

print('Qual a média da coluna temp?')
print(df['temp'].mean())

print('Quantos registros existem para o ano de 2011? E 2012?')
print(df['year'].value_counts())  #0:2011 1:2012

print('Quantas locações de bicicletas foram efetuadas em 2011?')
y=df[df['year']==0]
print(np.sum(y['total_count']))

print('Quantas locações de bicicletas foram efetuadas em 2012?')
y=df[df['year']==1]
print(np.sum(y['total_count']))

print('Qual estação do ano contém a maior média de locações de bicicletas?')
lista=[]
i=1
for i in range (1,5):
  y=df[df['season']==i]
  x=np.sum(y['total_count'])
  lista.append(x)
  i+=1
print(lista)
print(max(lista))'''

print('Qual estação do ano contém a menor média de locações de bicicletas?')


'''print('Qual estação do ano contém a menor média de locações de bicicletas?')


print('Qual horário do dia contém a menor média de locações de bicicletas?')


print('Que dia da semana contém a maior média de locações de bicicletas?')


print('Que dia da semana contém a menor média de locações de bicicletas?')


print('Às quartas-feiras (weekday = 3), qual o horário do dia contém a maior média de locações de bicicletas?')


print('Aos sábados (weekday = 6), qual o horário do dia contém a maior média de locações de bicicletas?')'''