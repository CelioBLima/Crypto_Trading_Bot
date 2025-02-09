import os
from binance.client import Client
import pandas as pd
from datetime import datetime
from time import sleep

# Carregar as variáveis de ambiente
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

# Inicializar o cliente da Binance
client = Client(API_KEY, API_SECRET)

def get_candlesticks(symbol, interval, start_str, end_str=None):
    """Função para obter dados de candlesticks."""
    klines = client.get_historical_klines(symbol, interval, start_str, end_str)
    data = []
    for kline in klines:
        data.append({
            'timestamp': datetime.fromtimestamp(kline[0] / 1000),
            'open': float(kline[1]),
            'high': float(kline[2]),
            'low': float(kline[3]),
            'close': float(kline[4]),
            'volume': float(kline[5])
        })
    return pd.DataFrame(data)

if __name__ == "__main__":
    symbol = 'BTCUSDT'
    interval = Client.KLINE_INTERVAL_1MINUTE
    start_str = '1 day ago UTC'

    while True:
        df = get_candlesticks(symbol, interval, start_str)
        print(df.tail())  # Exibir as últimas linhas do DataFrame
        sleep(60)  # Aguardar 1 minuto antes de coletar novamente
