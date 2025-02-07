import os
import pandas as pd
from binance.client import Client
from binance.exceptions import BinanceAPIException
from config.settings import API_KEY, API_SECRET

# Conectar à API da Binance
client = Client(API_KEY, API_SECRET)

def get_candlestick_data(symbol="BTCUSDT", interval=Client.KLINE_INTERVAL_1HOUR, limit=100):
    """
    Coleta dados de candlesticks (Klines) da Binance para um determinado par de negociação.

    :param symbol: Par de moedas (ex: "BTCUSDT")
    :param interval: Intervalo de tempo (ex: Client.KLINE_INTERVAL_1HOUR)
    :param limit: Número de candles a serem buscados
    :return: DataFrame com os dados dos candlesticks
    """
    try:
        klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)

        # Criar DataFrame a partir dos dados
        df = pd.DataFrame(klines, columns=[
            "timestamp", "open", "high", "low", "close", "volume",
            "close_time", "quote_asset_volume", "number_of_trades",
            "taker_buy_base", "taker_buy_quote", "ignore"
        ])

        # Converter para tipos numéricos
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)

        # Manter apenas colunas relevantes
        df = df[["timestamp", "open", "high", "low", "close", "volume"]]

        return df

    except BinanceAPIException as e:
        print(f"Erro na API da Binance: {e}")
        return None

# Teste rápido
if __name__ == "__main__":
    data = get_candlestick_data()
    print(data.head())
