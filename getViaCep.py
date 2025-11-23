import requests

def get_cep(cep = "01001000"):
    api_url = f"https://viacep.com.br/ws/{cep}/json/"
    
    response = requests.get(api_url)
    data = response.json()
    print(data)
    print(cep)
    
    if response.status_code == 200 and 'erro' not in data:
        data = response.json()
        return {
            'logradouro': data.get('logradouro'),
            'bairro': data.get('bairro'),
            'cidade': data.get('cidade'),
            'estado': data.get('estado'),
            'cep': data.get('cep'),
        }
    else:
        raise ValueError("Failed to fetch data from the API")
    
endereco = get_cep()

print("Logradouro:", endereco['logradouro'])
print("Bairro:", endereco['bairro'])
print("Cidade:", endereco['cidade'])
print("Estado:", endereco['estado'])
print("CEP:", endereco['cep'])
