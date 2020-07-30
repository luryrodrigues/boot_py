import pandas as pd 
import matplotlib.pyplot as plt 

df=pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
df['date']=pd.to_datetime(df['date'])
df=df.set_index('date')

#GROUPBY
x=df.groupby(by='classification').mean()   #agrupa os dados de acordo com a classificação e retorna a média do grupo
print(x)

#DROP (remoção de coluna)
x=df.drop('temperatura',axis=1)  #remove a coluna temperatura
print(x)

#INPLACE
df2=df.copy()
'''é importante fazer o df2=df.copy(). Se fizer df2=df, eles apontam para a mesma posição de memória,
e alterando o df2, o df também iria se alterar. Criando a cópia, o df2 altera e o df não.'''
df2.drop('temperatura',axis=1)
print(f'Método drop coluna temperatura com inplace False, o df original não altera:\n{df2}')
df2.drop('temperatura',axis=1,inplace=True)
print(f'Método drop coluna temperatura com inplace True, o df original é sobrescrito:\n{df2}')
'''com o inplace false: retorna sem a coluna, mas não altera o df2 original,
com o inplace True,sobrescreve o df2 original.'''
