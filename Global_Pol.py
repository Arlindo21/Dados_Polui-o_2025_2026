import pandas as pd
import numpy as np 

#metodo de extração - row  
#ETL - EXTRACT - Transform - load 
 
#Coletando os dados BRUTO 
df_Dados_poluicao_raw = pd.read_csv(r'C:\Users\123\OneDrive\Desktop\Cursos\Dados_Poluição\dados_polui-o_2526\Global_Air_Pollution_Data_2025_2026.csv')

#Mostrando os dados 
print(df_Dados_poluicao_raw)

#Analise Preliminar dos Dados 
#Raio-x da estrutura 
df_Dados_poluicao_raw.info()

#Resumo estatistico 
df_Dados_poluicao_raw.describe().T
