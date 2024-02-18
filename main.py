import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')
def get_response(localizacao):
    try:
        url = "https://local-business-data.p.rapidapi.com/search"
        querystring = {"query": localizacao, "language": "pt"}

        headers = {
            "X-RapidAPI-Key": os.getenv('API_KEY'),
            "X-RapidAPI-Host": "local-business-data.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            df = response.json()
            return df
        return None
    except requests.ConnectionError as e:
        print(f'Erro na solicitação da API: {response.status_code} ', e)

def main():
    try:
        localizacao = input('Digite a empresa que deseja pesquisar: ')
        if localizacao is not None:
            response_content = get_response(localizacao)
            id = response_content.get('request_id', None)
            print(f'ID: {id}')
            parameters = response_content.get('parameters', None)
            print(f'Parâmetros: {parameters}\n')
            data = response_content.get('data', None)
            for chave in data:
                print(150*'-')
                for key, valor in chave.items():
                    print(f'{key} - {valor}\n')
        else:
            print('Insira o nome de uma empresa')
    except Exception as e:
        print('Ocorreu um erro: ', e)

if __name__ == "__main__":
    main()

