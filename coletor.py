import time
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

partidas_por_pagina = 10
tota_paginas = 20
historico_partidas = []

for pagina in range(1, tota_paginas + 1):

    parametros = {
        "size": partidas_por_pagina,
        "page": pagina,
        "mode": "competitive"
    }

    response = requests.get(url, headers=headers, params=parametros)

    if response.status_code == 200:
        data = response.json()
        partidas = data.get("data", [])

        if not partidas:
            print(f"\nNenhuma partida a mais encontrada na página {pagina}.")
            break

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

        time.sleep(2)

    else:
        print(f"Erro {response.status_code}: Não foi possível buscar os dados.")
        print("Detalhe do erro:", response.text)


#salvando os dados em um arquivo CSV
if len(historico_partidas) > 0:
    df = pd.DataFrame(historico_partidas)
    df.to_csv("dados_brutos.csv", index=False)
else:
    print("\nNenhuma partida foi encontrada.")