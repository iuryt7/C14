import requests

def main():
    r = requests.get("https://pokeapi.co/api/v2/pokemon")
    if r.status_code == 200:
        print("Requisição bem-sucedida!")
        print(r.json())
    else:
        print("Falha na requisição:", r.status_code)

if __name__ == "__main__":
    main()