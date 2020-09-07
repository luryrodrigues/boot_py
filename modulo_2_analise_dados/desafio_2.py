import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('https://pycourse.s3.amazonaws.com/bike-sharing.csv')

print(df.head())

print('a) Qual o tamanho desse dataset?')
print(df.info())

print('b) Qual a média da coluna windspeed?')
print(df['windspeed'].describe())

print('c) Qual a média da coluna temp?')
print(df['temp'].mean())

print('d) Quantos registros existem para o ano de 2011? E 2012?')
print(df['year'].value_counts())  #0:2011 1:2012

print('e) Quantas locações de bicicletas foram efetuadas em 2011?')
y=df[df['year']==0]
print(np.sum(y['total_count']))

print('f) Quantas locações de bicicletas foram efetuadas em 2012?')
y=df[df['year']==1]
print(np.sum(y['total_count']))

print('g) Qual estação do ano contém a maior média de locações de bicicletas?')
lista=[]
i=1
for i in range (1,5):
  y=df[df['season']==i]
  x=np.mean(y['total_count'])
  lista.append(x)
  i+=1
print(lista.index(max(lista)))

print('h) Qual estação do ano contém a menor média de locações de bicicletas?')
print(lista.index(min(lista)))

print('i) Qual horário do dia contém a maior média de locações de bicicletas?')
lista=[]
i=0
for i in range (0,24):
  y=df[df['hour']==i]
  x=np.mean(y['total_count'])
  lista.append(x)
  i+=1
print(lista.index(max(lista)))
print('j) Qual horário do dia contém a menor média de locações de bicicletas?')
print(lista.index(min(lista)))

print('k) Que dia da semana contém a maior média de locações de bicicletas?')
lista=[]
i=0
for i in range (0,7):
  y=df[df['weekday']==i]
  x=np.mean(y['total_count'])
  lista.append(x)
  i+=1
print(lista.index(max(lista)))
print('l) Que dia da semana contém a menor média de locações de bicicletas?')
print(lista.index(min(lista)))

print('m) Às quartas-feiras (weekday = 3), qual o horário do dia contém a maior média de locações de bicicletas?')
y=df[df['weekday']==3]
x=y.groupby(by='hour')
z=(x['total_count']).mean().sort_values(ascending=False)
print(z.head(1))

print('n) Aos sábados (weekday = 6), qual o horário do dia contém a maior média de locações de bicicletas?')
y=df[df['weekday']==6]
x=y.groupby(by='hour')['total_count'].mean().sort_values(ascending=False)
print(x.head(1))