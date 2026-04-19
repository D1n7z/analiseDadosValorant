# Valorant Data & AI Analysis

Este é um projeto pessoal desenvolvido por diversão para explorar o meu histórico de partidas no **Valorant**. O objetivo é utilizar Ciência de Dados e Machine Learning para identificar padrões de jogo, correlações estatísticas e entender quais fatores (KDA, Agente, Mapa) realmente influenciam na vitória.

## Como o Projeto Funciona

O projeto é dividido em um pipeline de 4 etapas modulares:

1.  **Coleta (`coletor.py`)**: Utiliza a API do HenrikDev para extrair dados brutos das partidas competitivas diretamente dos servidores da Riot.
2.  **Processamento (`processador.py`)**: Limpa os dados, remove partidas inválidas e realiza *Feature Engineering* (criação de métricas como KDA Ratio e categorias de desempenho).
3.  **Exploração (`explorador.py`)**: Gera visualizações estatísticas, como mapas de calor de correlação e taxas de vitória por agente.
4.  **Inteligência Artificial (`modelo_ia.py`)**: Treina modelos de *Decision Tree* e *Random Forest* para prever vitórias e ranquear a importância de cada métrica.

## Tecnologias Utilizadas

- **Python 3**
- **Pandas**: Manipulação e análise de dados.
- **Scikit-Learn**: Modelagem de Machine Learning.
- **Seaborn & Matplotlib**: Visualização de dados.
- **Requests**: Integração com API.

## Insights Descobertos

Através deste projeto, a IA identificou padrões como:
- A importância crítica de manter um **KDA Ratio acima de 1.4** para garantir vitórias.
- O impacto desproporcional do desempenho com a **Jett** no Win Rate.
- A correlação direta entre **sobrevivência (baixas mortes)** e sucesso em mapas específicos como a Bind.

## Como Executar

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/D1n7z/analiseDadosValorant.git](https://github.com/D1n7z/analiseDadosValorant.git)
    ```
2.  Crie um ambiente virtual e instale as dependências:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3.  Crie um arquivo `credenciais.py` com sua chave da API:
    ```python
    CHAVE = "SUA_CHAVE_AQUI"
    ```
4.  Execute os scripts na ordem numérica das fases.

---
*Projeto desenvolvido para fins de estudo em Ciência de Dados.*