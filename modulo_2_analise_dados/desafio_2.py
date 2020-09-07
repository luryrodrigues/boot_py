import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('https://pycourse.s3.amazonaws.com/bike-sharing.csv')

print(df.head(2))

print('a) Qual o tamanho desse dataset?')
print(df.info())

print('b) Qual a média da coluna windspeed?')
print(df['windspeed'].mean())

print('c) Qual a média da coluna temp?')
print(df['temp'].mean())

print('d) Quantos registros existem para o ano de 2011?')
y=df[df['year']==0]
print(y['year'].value_counts())
print('e) E 2012?')
y=df[df['year']==1]
print(y['year'].value_counts())

print('f) Quantas locações de bicicletas foram efetuadas em 2011?')
y=df[df['year']==0]
print(np.sum(y['total_count']))

print('g) Quantas locações de bicicletas foram efetuadas em 2012?')
y=df[df['year']==1]
print(np.sum(y['total_count']))

print('h) Qual estação do ano contém a maior média de locações de bicicletas?')
estacoes={1 : 'inverno', 2 : 'primavera', 3 : 'verão', 4 : 'outono'}
lista=[]
i=1
for i in range (1,5):
  y=df[df['season']==i]
  x=np.mean(y['total_count'])
  lista.append(x)
  i+=1
resp=(lista.index(max(lista)))+1
print(estacoes.get(resp))

print('i) Qual estação do ano contém a menor média de locações de bicicletas?')
resp=(lista.index(min(lista)))+1
print(estacoes.get(resp))

print('j) Qual horário do dia contém a maior média de locações de bicicletas?')
lista=[]
i=0
for i in range (0,24):
  y=df[df['hour']==i]
  x=np.mean(y['total_count'])
  lista.append(x)
  i+=1
print(lista.index(max(lista)))
print('k) Qual horário do dia contém a menor média de locações de bicicletas?')
print(lista.index(min(lista)))

print('l) Que dia da semana contém a maior média de locações de bicicletas?')
weekdays={0 : 'domingo', 1 : 'segunda', 2 : 'terça', 3 : 'quarta', 4: 'quinta', 5: 'sexta', 6: 'sábado'}
lista=[]
i=0
for i in range (0,7):
  y=df[df['weekday']==i]
  x=np.mean(y['total_count'])
  lista.append(x)
  i+=1
resp=lista.index(max(lista))
print(weekdays.get(resp))
print('m) Que dia da semana contém a menor média de locações de bicicletas?')
resp=lista.index(min(lista))
print(weekdays.get(resp))

print('n) Às quartas-feiras (weekday = 3), qual o horário do dia contém a maior média de locações de bicicletas?')
y=df[df['weekday']==3]
x=y.groupby(by='hour')
z=(x['total_count']).mean().sort_values(ascending=False)
print(z.head(1))

print('o) Aos sábados (weekday = 6), qual o horário do dia contém a maior média de locações de bicicletas?')
y=df[df['weekday']==6]
x=y.groupby(by='hour')['total_count'].mean().sort_values(ascending=False)
print(x.head(1))

#gráficos
fig, ax = plt.subplots(nrows=2,sharex=True,figsize=(16,10))

sns.pointplot(data=df,x='hour',y='total_count',hue='season',ax=ax[0])
ax[0].set_title('Locações horárias de bicicleta por estação do ano')
ax[0].grid()

sns.pointplot(data=df,x='hour',y='total_count',hue='weekday',ax=ax[1])
ax[1].set_title('Locações horárias de bicicleta por dia da semana')
ax[1].grid()
plt.show()

fig, ax = plt.subplots()
sns.barplot(data=df,x='year',y='total_count',estimator=sum,ci=None)
ax.set_title('Locações por ano')
plt.show()

