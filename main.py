import requests
        
def main():
    r = requests.get("https://pokeapi.co/api/v2/pokemon")
    if r.status_code == 200:
        print("Requisição bem-sucedida!")
        data = r.json()
        print("Primeiros 10 pokémons:")
        for pokemon in data.get("results", [])[:10]:
            print("-", pokemon["name"])
    else:
        print("Falha na requisição:", r.status_code)

if __name__ == "__main__":
    main()