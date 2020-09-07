import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

#leitura de dados
df=pd.read_csv('https://pycourse.s3.amazonaws.com/movies.csv')

#descritivo dos dados
from pandas_profiling import ProfileReport    #gera um report dos dados

#profile=ProfileReport(df,title='Movies Dataset')  #instanciando a classe e dando um título ao report
#profile.to_file('movies_dataset.html')   #cria um arquivo

#print('Informações sobre o dataset antes da limpeza de dados:')
#print(df.info())

#LIMPEZA DE DADOS
#remoção de colunas com poucos dados válidos
df.drop(['belongs_to_collection','homepage','tagline'],axis='columns',inplace=True)
#remoção de colunas com pouca variabilidade ou irrelevantes  (conforme visto no Movies Dataset)
df.drop(['adult','overview'],axis='columns',inplace=True)  #axis=1 poderia ser também
#remoção de linhas com dados faltantes
df.dropna(axis='index',inplace=True)   #dropna: remove os "not a number"

#print('Informações sobre o dataset após a limpeza de dados:')
#print(df.info())

#ESTRUTURANDO DADOS
#criando one-hot-encoding
import json

def list_to_ohe(df:pd.DataFrame,cols:list):
  #para cada coluna
  n_rows=df.shape[0]
  df.reset_index(inplace=True,drop=True)   #para organizar as linhas
  for col_i in cols:
    dfi=df[col_i]  #selecionando a coluna
    new_cols={}  #dicionário para mapeamento
    for i, row in enumerate(dfi):   #percorrendo cada linha da coluna mapeada
      row=row.replace("\'","\"")    #string como JSON. JSON só aceita aspas duplas
      list_i=json.loads(row)  #json permite acessar as chaves
      for elem in list_i:   #percorrendo cada elemento da lista
        new_col_name='col_i'+'_'+elem['name']   #nova coluna com a categoria   #col_[nome_categoria]
        if new_col_name not in new_cols:   #adiciona nova coluna e preenche com zeros
          new_cols[new_col_name]=np.zeros((n_rows))
        new_cols[new_col_name][i]=1   #atribui classificação
  new_df=pd.DataFrame(new_cols)  #tranforma o difionário em um dataframe
  df=pd.concat([df,new_df],axis=1).reset_index(drop=True)
  return df

#colunas para transformar
cols_to_transform=['genres']
print('Shape antes: ',df.shape)
df=list_to_ohe(df,cols=cols_to_transform)
print('Shape depois: ',df.shape)

#verificando novas colunas de generos de filmes
genres_created=[col for col in df if col.startswith('genres_')]
print('Colunas de gênero de filmes inseridas:\n',np.array(genres_created).reshape(-1,1))

#ANÁLISE DOS DADOS
#filmes sem avaliação
cond=df['vote_count'] < 0.001
print('Quantidade de filmes sem avaliação:\n', sum(cond))
#removendo filmes não avaliados
df=df.loc[~cond]  #~ é o mesmo que not
print('Novo shape: ',df.shape)
#verificando a operação
cond=df['vote_count'] < 0.001
print('Quantidade de filmes sem avaliação:\n', sum(cond))
#nota média entre todos os filmes
C=df['vote_average'].mean()
print('A média de todas as notas é ',C)
#nº mínimo de votos para a análise
print(df['vote_count'].describe())
m=df['vote_count'].quantile(0.9)  #para considerar o filme deve ter uma contagem de votos pelo menos maior que 90% de todos os filmes
print('O número mínimo de votos é ',m)
#filtrando o dataset
df=df[df['vote_count']>m]  #slicing
#adição de nova coluna com o score
v=df['vote_count']
R=df['vote_average']
df.loc[:,'score']=v/(v+m) * R + m/(m+v) * C
#ordenando pelo score calculado
df.sort_values(by='score',ascending=False,inplace=True)
df.reset_index(inplace=True)

#TOP 10 FILMES
df_top_score=df[:10]
print(df[['original_title','vote_count','vote_average','score']].head(10))

#Contagem de GÊNEROS no TOP 10 score
df_top_score_gen=df_top_score[genres_created].sum().sort_values(ascending=False)
print(df_top_score_gen)

#colormap
from matplotlib import cm
cmap=cm.get_cmap('Set3')
#retirando valores nulos
df_top_score_gen=df_top_score_gen[df_top_score_gen > 0]
#formatação
labels=[gen[7:]for gen in df_top_score_gen.index]
#plot
df_top_score_gen.plot.pie(autopct='%1.1f%%',pctdistance=0.8,radius=1.25,labels=labels,cmap=cmap)
plt.ylabel(' ')
plt.suptitle('Gêneros mais frequentes do TOP 10 (score)')
plt.show()

#TOP 10 POPULARIDADE
df['popularity']=df['popularity'].astype(float)
df_top_pop=df.sort_values(by='popularity',ascending=False)
print(df_top_pop[['original_title','score','popularity']]).head(10)
#visualização dos filmes mais populares
df_top_pop[:10].plot.barh(x=['original_title'],y=['popularity'])
plt.gca.invert_yaxis()
plt.show()