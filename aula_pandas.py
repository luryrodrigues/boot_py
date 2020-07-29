import pandas as pd

df=pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv') #df=dataframe
print(df)

#planilha com 2 abas
excel_file=pd.ExcelFile('https://pycourse.s3.amazonaws.com/temperature.xlsx') #leitura do arquivo todo

#ler uma aba da planilha
#dados numéricos já estão com o separador '.'
df2=pd.read_excel(excel_file,sheet_name='Sheet1')
print(df2)

#dados numéricos com separador ',' devem ser transformados para '.'
df3=pd.read_excel(excel_file,sheet_name='Sheet2',decimal=',')
print(df3)

#ler as primeiras N linhas
print(df.head(3))

#ler as últimas N linhas
print(df.tail(3))

#tipos de dados
print(df.dtypes)

#estatísticas básicas
print(df.describe())

#informações
print(df.info())

#nome das colunas
print(df.columns)
#df.columns=['col1','col2','col3']  renomeia as colunas

#INDEXAÇÃO NO PANDAS

#seleção de uma coluna
print(df['date'])  #retorna uma série

#seleção de multiplas colunas
print(df[['classification','temperatura']])  #retorna colunas na ordem da lista

#indexação por índice: ILOC
print(df.iloc[:,1]) #retorna todas as linhas da coluna 1

#indexação por nome: LOC
print(df.loc[:,'temperatura'])

#indexação por indice de multiplas colunas
print(df.iloc[4,1:3])

##indexação por nome de multiplas colunas
print(df.loc[:,['temperatura','classification']])