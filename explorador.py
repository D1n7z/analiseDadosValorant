import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#carregando o dataset
try:
    df = pd.read_csv('dados_limpos.csv')
except FileNotFoundError:
    print("O arquivo 'dados_limpos.csv' não foi encontrado.")
    exit()    

#mapa de calor
plt.figure(figsize=(8, 6))

colunas_numericas = df[['kills', 'deaths', 'assists', 'kda_ratio', 'vitoria']]
matriz_correlacao = colunas_numericas.corr()

#gráfico
sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title('Mapa de Calor - Correlação entre Variáveis')
plt.tight_layout()

plt.show()

#grafico 2
taxa_agente = df.groupby('agente')['vitoria'].mean().reset_index()

plt.figure(figsize=(10, 5))
sns.barplot(x='agente', y='vitoria', hue='agente', data=taxa_agente, palette='viridis', legend=False)
plt.title('Taxa de Vitória por Agente')
plt.ylabel('Taxa de Vitória 0 a 1')
plt.xlabel('Agente')
plt.ylim(0, 1)
plt.tight_layout()

plt.show()
