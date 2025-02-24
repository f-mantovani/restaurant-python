from fastapi import FastAPI, Query
import requests


app = FastAPI()

print("changes in that file")


@app.get("/")
def start():
    return {"message": "success", "server": "running"}


@app.get("/api/restaurantes/")
def get_restaurantes(restaurante: str = Query(None)):
    """
    Endpoint para mostrar o menu dos restaurantes
    """
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {"Dados": dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item["Company"] == restaurante:
                dados_restaurante.append(
                    {
                        "item": item["Item"],
                        "preco": item["price"],
                        "descricao": item["description"],
                    }
                )
        return {"Restaurante": restaurante, "Cardapio": dados_restaurante}
    else:
        return {"Erro": f"{response.status_code} - {response.text}"}
