
import requests

url = "https://br.dolarapi.com/v1/cotacoes/usd"

try:
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()

    cotacoes = resposta.json()

    if not cotacoes:
        print("A API não retornou cotações.")
    else:
        
        print("\n===== COTAÇÃO DO DÓLAR =====")
        print(f"Moeda: {cotacoes['nome']}")
        print(f"Compra: R$ {cotacoes['compra']:.4f}")
        print(f"Venda: R$ {cotacoes['venda']:.4f}")
        print(f"Fechamento anterior: R$ {cotacoes['fechoAnterior']:.4f}")
        print(f"Atualizado em: {cotacoes['dataAtualizacao']}")

except requests.exceptions.RequestException as erro:
    print(f"Falha ao consultar a API: {erro}")
