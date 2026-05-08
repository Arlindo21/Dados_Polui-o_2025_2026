import pandas as pd
import numpy as np

# ==================================================
# ETL - EXTRACT | TRANSFORM | LOAD
# Projeto: Global Air Pollution Analysis
# ==================================================

# -----------------------------
# EXTRACT - Coleta dos Dados
# -----------------------------

df_dados_poluicao_raw = pd.read_csv(
    r'C:\Users\123\OneDrive\Desktop\Cursos\Dados_Poluição\dados_polui-o_2526\Global_Air_Pollution_Data_2025_2026.csv'
)

# -----------------------------
# Análise Inicial
# -----------------------------

print('\n📌 Primeiras linhas:')
print(df_dados_poluicao_raw.head())

print('\n📌 Estrutura dos dados:')
print(df_dados_poluicao_raw.info())

print('\n📌 Resumo estatístico:')
print(df_dados_poluicao_raw.describe().T)

# ==================================================
# PIPELINE ETL
# ==================================================

def pipeline(df):

    # Backup dos dados
    df_limpos = df.copy()

    # -----------------------------
    # Padronização das colunas
    # -----------------------------

    df_limpos.columns = [
        col.lower().replace(' ', '_')
        for col in df_limpos.columns
    ]

    # -----------------------------
    # Conversão de datas
    # -----------------------------

    df_limpos['date'] = pd.to_datetime(df_limpos['date'])

    # -----------------------------
    # Classificação PM2.5
    # -----------------------------

    condicoes = [
        (df_limpos['pm2.5'] <= 12),
        (df_limpos['pm2.5'] <= 34.5),
        (df_limpos['pm2.5'] <= 55.4),
        (df_limpos['pm2.5'] <= 150.4),
        (df_limpos['pm2.5'] > 150.4)
    ]

    escolhas = [
        'Boa',
        'Moderado',
        'Insalubre para grupos sensíveis',
        'Insalubre',
        'Muito Insalubre/Perigoso'
    ]

    df_limpos['status_saude'] = np.select(
        condicoes,
        escolhas,
        default='N/A'
    )

    return df_limpos

# ==================================================
# LOAD - Dados Tratados
# ==================================================

df_dados_poluicao_final = pipeline(df_dados_poluicao_raw)

# Visualização final
print('\n📌 Dados tratados:')
print(df_dados_poluicao_final.head(50))