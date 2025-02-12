from binance.spot import Spot
import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.settings import API_KEY, API_SECRET

# Inicialize o cliente da Binance
client = Spot(api_key=API_KEY, api_secret=API_SECRET)

# Obtenha informações da conta para verificar a conexão

try:
    account_info = client.account()
    print("Conexão bem sucedida!")
    print("Informações da conta:", account_info)

except Exception as e:
    print("Erro ao conectar-se à API da Binance", e)