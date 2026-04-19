import pandas as pd

#carregar os dados brutos

try:
    df = pd.read_csv("dados_brutos.csv")
except FileNotFoundError:
    print("O arquivo 'dados_brutos.csv' não foi encontrado.")
    exit()

#limpar os dados

df["kda_ratio"] = (df["kills"] + df["assists"]) / df["deaths"].replace(0, 1)
df["kda_ratio"] = df["kda_ratio"].round(2)

def classificar_kda(kda):
    if kda >= 1.5:
        return "Excelente"
    elif kda >= 1.0:
        return "Bom"
    else:
        return "Ruim"

df["desempenho"] = df["kda_ratio"].apply(classificar_kda)

df = df[(df["kills"] >= 0) & (df["deaths"] >= 0) & (df["assists"] >= 0)]

df.to_csv("dados_limpos.csv", index=False)