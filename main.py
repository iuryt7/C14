import requests


def main():
    requisao = requests.get("https://pokeapi.co/api/v2/pokemon")
    if requisao.status_code == 200:
        print("Requisição bem-sucedida!")
        data = requisao.json()
        print("Primeiros 10 pokémons:")
        for pokemon in data.get("results", [])[:10]:
            print("-", pokemon["name"])
    else:
        print("Falha na requisição:", requisao.status_code)

if __name__ == "__main__":
    main()