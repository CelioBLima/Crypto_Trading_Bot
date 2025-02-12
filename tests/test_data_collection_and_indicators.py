import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from trading.binance_api import get_candlestick_data
from indicators.technical_analysis import calculate_ema, calculate_rsi, calculate_macd
from config.settings import SYMBOL, INTERVAL, CANDLE_LIMIT

def main():
    # Coletar dados de candlestick
    df = get_candlestick_data(symbol=SYMBOL, interval=INTERVAL, limit=CANDLE_LIMIT)

    # Calcular EMA
    df = calculate_ema(df, period=14) # pode ser ajustado

    # Calcular RSI
    df = calculate_rsi(df, period=14) # pode ser ajustado

    # Calcular MACD 
    df = calculate_macd(df)

    # Exibir os dados com os indicadores calculador
    print(df.tail())

if __name__ == "__main__":
    main()