import pandas as pd
import numpy as np 

#metodo de extração - row  
#ETL - EXTRACT - Transform - load 
 


#Coletando os dados BRUTO 
df_Dados_poluicao_raw = pd.read_csv(r'C:\Users\123\OneDrive\Desktop\Cursos\Dados_Poluição\dados_polui-o_2526\Global_Air_Pollution_Data_2025_2026.csv')

#Mostrando os dados 

print('\n ==== Primeiras linhas: ====')
print(df_Dados_poluicao_raw.head())

#Analise Preliminar dos Dados 
#Raio-x da estrutura 
print('\n==== Estrutura dos dados ====')
print(df_Dados_poluicao_raw.info())


#Resumo estatistico 
print('\n==== Resumo estatístico ====')
print(df_Dados_poluicao_raw.describe().T)


# Criando a Engenharia de Dados / Pipeline ETL


def pipeline(df):

    # Criar BACKUP dos dados
    df_limpos = df.copy()

    # Padronização das colunas para snake_case
    df_limpos.columns = [
        col.lower().replace(' ', '_')
        for col in df_limpos.columns
    ]

    # Converter coluna de data
    df_limpos['date'] = pd.to_datetime(df_limpos['date'])

    # Condições de qualidade do ar (PM2.5)
    condicoes = [
        (df_limpos['pm2.5'] <= 12),
        (df_limpos['pm2.5'] <= 34.5),
        (df_limpos['pm2.5'] <= 55.4),
        (df_limpos['pm2.5'] <= 150.4),
        (df_limpos['pm2.5'] > 150.4)
    ]

    # Classificações
    escolhas = [
        'Boa',
        'Moderado',
        'Insalubre para grupos sensíveis',
        'Insalubre',
        'Muito Insalubre/Perigoso'
    ]

    # Criando nova coluna categórica
    df_limpos['status_saude'] = np.select(
        condicoes,
        escolhas,
        default='N/A'
    )
    df_limpos['dia'] = df_limpos['date'].dt.day
    df_limpos['mes'] = df_limpos['date'].dt.month   
    df_limpos['ano'] = df_limpos['date'].dt.year
    df_limpos['hora'] = df_limpos['date'].dt.hour
    df_limpos['minuto'] = df_limpos['date'].dt.minute
    
    return df_limpos

# Aplicando o pipeline
df_Dados_poluicao_final = pipeline(df_Dados_poluicao_raw)
print('\n==== Dados tratados ====')
print(df_Dados_poluicao_final.head(50))