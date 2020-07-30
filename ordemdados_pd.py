import pandas as pd

df=pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
df['date']=pd.to_datetime(df['date'])
df=df.set_index('date')

#ORDENAÇÃO DE DADOS
print(f'\nDados originais:\n{df}')
x=df.sort_values(by='temperatura')   #sem nenhum argumento vai organizar de forma crescente
print(f'\nDados ordenados por temperatura:\n{x}')

x=df.sort_values(by=['classification','temperatura'])  #ordenação por mais de uma coluna
print(f'\nDados ordenados por classificação e depois por temperatura:\n{x}')

x=df.sort_values(by='temperatura',ascending=False)   #ordenação descrescente
print(f'\nDados ordenados por temperatura de forma decrescente:\n{x}')

x=df.sort_index(ascending=False)   #ordenação pelo índice
print(f'\nDados ordenados pelo índice de forma decrescente:\n{x}')