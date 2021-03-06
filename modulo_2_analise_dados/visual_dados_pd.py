import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
df['date']=pd.to_datetime(df['date'])
df=df.set_index('date')

#GRÁFICOS DE LINHA
df.plot(style='-o',linewidth=2.5,color='red',figsize=(10,5),grid=True)
plt.show()
#'o': scatterplot '-o': linha com pontos '--': tracejado '-.': tracejado e pontos   lineidth: espessura da linha
#color='#b05dcf' poderia ser assim também

#GRÁFICO DE BARRAS
classif=df['classification'].value_counts()  #retorna a quantidade de cada entrada na coluna
classif.plot.bar(figsize=(10,5),rot=0)  #rot é a rotação dos labels no eixo x
plt.show()

df.plot(kind='bar',figsize=(10,5),rot=30)  #gráfico de barras pela indexação, nesse caso eixo x vai ser a data.
plt.show()

#GRÁFICO DE PIZZA
print(classif.plot.pie(figsize=(10,5),shadow=True,autopct='%1.1f%%'))   #autopct: coloca porcentagem no gráfico, #shadow é só um estilo
plt.show()