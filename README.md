# 🌫️ Global Air Pollution Analysis — 2026 Smog Crisis

## 📌 Sobre o Projeto

Este projeto foi desenvolvido com foco em **Análise de Dados**, utilizando técnicas aprendidas no curso da Generation Brasil na área de Tecnologia da Informação.

O objetivo é analisar dados globais de poluição atmosférica durante o período conhecido como **“Smog Season” (2025–2026)**, identificando padrões, tendências e possíveis relações entre poluentes atmosféricos em diferentes cidades do mundo.

---

# 🎯 Objetivos do Projeto

* Realizar um processo completo de **ETL (Extract, Transform, Load)**
* Limpar e tratar dados ambientais
* Explorar padrões de poluição atmosférica
* Criar análises estatísticas e visuais
* Comparar níveis de poluição entre cidades
* Investigar correlação entre poluentes
* Desenvolver dashboards e insights analíticos

---

# 🌎 Dataset Utilizado

Dataset: **Global Air Pollution Dataset: The 2026 Smog Crisis**

## 📊 Informações do Dataset

* 📅 Período: Outubro/2025 até Janeiro/2026
* 🏙️ 8 grandes cidades globais
* ⏱️ Dados horários
* 📈 17.472 registros
* ✅ Zero valores ausentes

---

# 🧪 Principais Variáveis

| Coluna                  | Descrição                               |
| ----------------------- | --------------------------------------- |
| `Date`                  | Data e hora da medição                  |
| `City`                  | Cidade do sensor                        |
| `PM2.5`                 | Partículas finas altamente prejudiciais |
| `PM10`                  | Poeira e partículas maiores             |
| `NO2`                   | Poluição relacionada ao trânsito        |
| `CO`                    | Monóxido de carbono                     |
| `Aerosol_Optical_Depth` | Bloqueio da luz solar por partículas    |
| `AQI_Class`             | Classificação da qualidade do ar        |

---

# 🛠️ Tecnologias Utilizadas

## 📌 Linguagem

* Python

## 📌 Bibliotecas

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly

## 📌 Ferramentas

* Jupyter Notebook
* VS Code
* Git & GitHub
* Power BI

---

# 🔄 Pipeline ETL

## 1️⃣ Extract

Importação do dataset CSV.

```python
import pandas as pd

df_raw = pd.read_csv("Global_Air_Pollution_Data_2025_2026.csv")
```

---

## 2️⃣ Transform

Tratamento e preparação dos dados:

* Verificação de valores nulos
* Conversão de datas
* Padronização de colunas
* Análise estatística
* Criação de métricas

---

## 3️⃣ Load

Exportação dos dados tratados para:

* dashboards
* análises
* visualizações
* relatórios

---

# 📊 Análises Realizadas

## 🌫️ Análise de PM2.5

* Identificação das cidades mais poluídas
* Horários de pico de poluição
* Evolução diária do smog

## 🚗 Trânsito vs Poluição

* Correlação entre `NO2` e `PM2.5`
* Impacto do tráfego urbano

## 🌎 Comparação entre Cidades

* Ranking de qualidade do ar
* Diferenças climáticas e ambientais

## 📈 Visualização de Dados

* Gráficos temporais
* Heatmaps
* Dashboards interativos

---

# 📌 Estrutura do Projeto

```bash
📂 global-air-pollution-analysis
│
├── 📂 data
│   ├── raw
│   ├── clean
│
├── 📂 notebooks
│
├── 📂 dashboard
│
├── 📂 images
│
├── README.md
│
└── requirements.txt
```

---

# 🚀 Possíveis Expansões

* Machine Learning para previsão de PM2.5
* Modelos preditivos de AQI
* Integração com APIs climáticas
* Dashboard em tempo real
* Deploy em nuvem

---

# 📚 Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conhecimentos de:

* ETL
* Data Cleaning
* Data Visualization
* Análise Exploratória de Dados (EDA)
* Estatística
* Storytelling com Dados
* Versionamento com Git/GitHub

---

# 🧠 Insights Esperados

* Como o tráfego impacta o smog?
* Quais cidades apresentam maior risco ambiental?
* Existem horários críticos de poluição?
* Qual poluente possui maior correlação com o AQI?

---

# ⚖️ Licença

Dataset disponibilizado sob licença:

**CC0 — Public Domain**

---

# 👨‍💻 Autor

Projeto desenvolvido para fins educacionais e portfólio na área de:

* Análise de Dados
* Business Intelligence
* Ciência de Dados

📌 Desenvolvido utilizando práticas aprendidas na Generation Brasil.
