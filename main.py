import requests


def main():
    request = requests.get("https://pokeapi.co/api/v2/pokemon")
    if request.status_code == 200:
        print("Requisição bem-sucedida!")
        data = request.json()
        print("Primeiros 10 pokémons:")
        for pokemon in data.get("results", [])[:10]:
            print("-", pokemon["name"])
    else:
        print("Falha na requisição:", request.status_code)

if __name__ == "__main__":
    main()