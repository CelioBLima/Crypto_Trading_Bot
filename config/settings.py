from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Chaves da API da Binance
API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Configuração do par de moedas e intervalo de tempo
SYMBOL = "BTCUSDT"
# INTERVAL = "1h"  # 1 hora
INTERVAL = "1m"  # 1 minuto

# Número de candles a serem coletados
CANDLE_LIMIT = 60