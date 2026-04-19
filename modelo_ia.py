import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier

#carregando o dataset
try:
    df = pd.read_csv('dados_limpos.csv')
except FileNotFoundError:
    print("O arquivo 'dados_limpos.csv' não foi encontrado.")
    exit()

#pré-processamento
df_ia = pd.get_dummies(df, columns=['agente', 'mapa', 'desempenho'])

y = df_ia['vitoria']
X = df_ia.drop('vitoria', axis=1)

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

#modelo de árvore de decisão
arvore = DecisionTreeClassifier(max_depth=3, random_state=42)
arvore.fit(X_treino, y_treino)

plt.figure(figsize=(14, 7))
plot_tree(arvore, feature_names=X.columns, class_names=['Derrota', 'Vitória'], filled=True)
plt.title('Árvore de Decisão - Fluxograma de Vitória')

plt.show()

#modelo de floresta aleatória
floresta = RandomForestClassifier(n_estimators=100, random_state=42)
floresta.fit(X_treino, y_treino)

precisao = floresta.score(X_teste, y_teste)
print(f"Precisão do modelo de Floresta Aleatória: {precisao*100:.1f}%\n")

importancia = floresta.feature_importances_

tabela_importancia = pd.DataFrame({
    'Métrica': X.columns,
    'Importância': importancia * 100
}).sort_values(by='Importância', ascending=False)

print("Importância das Métricas para a Previsão de Vitória:")
print(tabela_importancia.head(10).to_string(index=False))
