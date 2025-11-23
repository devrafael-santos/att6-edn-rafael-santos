import requests

# mostre valor atual, máxima, mínima e data/hora da última atualização

def get_cotacao(moedas = ["USD-BRL", "EUR-BRL", "BTC-BRL"]): 
    api_url = "https://economia.awesomeapi.com.br/last/" + ",".join(moedas)
    
    response = requests.get(api_url)
    data = response.json()
    
    if response.status_code == 200:
        cotacoes = {}
        
        for par in moedas:
            info = data.get(par.replace("-", ""))
            if info:
                cotacoes[par] = {
                    'nome': info['name'],
                    'valor': info['bid'],
                    'variação': info['varBid'],
                    'máxima': info['high'],
                    'mínima': info['low'],
                    'data_hora': info['create_date']
                }
        return cotacoes
    else:
        raise ValueError("Failed to fetch data from the API")

cotacoes = get_cotacao()

for par, info in cotacoes.items():
    print(f"Cotação de {info['nome']}:")
    print(f"  Valor Atual: R$ {info['valor']}")
    print(f"  Variação: R$ {info['variação']}")
    print(f"  Máxima: R$ {info['máxima']}")
    print(f"  Mínima: R$ {info['mínima']}")
    print(f"  Data/Hora da Última Atualização: {info['data_hora']}\n")