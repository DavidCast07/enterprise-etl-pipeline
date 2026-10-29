import requests
import json
import os

API_URL = "https://dummyjson.com/products?limit=150"

def fetch_data():
    print(f"Obteniendo datos desde: {API_URL}")
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        data = response.json()
        
        # Guardar el JSON crudo en disco temporalmente
        file_path = "data/raw_products.json"
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
            
        print(f"¡Éxito! Se guardaron {len(data['products'])} productos en {file_path}.")
    else:
        print(f"Error en la extracción. Código de estado: {response.status_code}")

if __name__ == "__main__":
    fetch_data()
