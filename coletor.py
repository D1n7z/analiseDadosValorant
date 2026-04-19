import requests
import pandas as pd 
from credenciais import CHAVE 

regiao = 'br'
nome = 'dejota'
tag = '007'

url = f"https://api.henrikdev.xyz/valorant/v3/matches/{regiao}/{nome}/{tag}"
headers = {
    "Authorization": CHAVE
}

response = requests.get(url, headers=headers) 

historico_partidas = []

if response.status_code == 200:
    data = response.json()
    partidas = data.get("data", [])

    for partida in partidas:
        mapa = partida['metadata']['map'] 
        
        meus_status = next((jogador for jogador in partida['players']['all_players'] 
            if jogador['name'].lower() == nome.lower() and jogador['tag'].lower() == tag.lower()), None)
        
       
        if meus_status:
            agente = meus_status['character']
            kills = meus_status['stats']['kills']
            deaths = meus_status['stats']['deaths']
            assists = meus_status['stats']['assists']
            
            
            seu_time = meus_status['team'].lower()
            vitoria = 1 if partida['teams'][seu_time]['has_won'] else 0
            
            
            historico_partidas.append({
                "mapa": mapa,
                "agente": agente,
                "kills": kills,
                "deaths": deaths,
                "assists": assists,
                "vitoria": vitoria
            })

    if len(historico_partidas) > 0:
        df = pd.DataFrame(historico_partidas)
        df.to_csv("dados_brutos.csv", index=False)
    else:
        print("\nNenhuma partida foi encontrada.")

else:
    print(f"Erro {response.status_code}: Não foi possível buscar os dados.")
    print("Detalhe do erro:", response.text)