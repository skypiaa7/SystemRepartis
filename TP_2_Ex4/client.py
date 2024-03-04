import requests
import json


def main():
    url = "http://localhost:8000/RPC2"

    # Example echo method
    payload = {
        "method": "calcul",
        "params": ["17-2"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(url, json=payload).json()

    assert response["result"] == 15
    print(f"la réponse est : {response['result']}")
          
if __name__ == "__main__":
    main()

