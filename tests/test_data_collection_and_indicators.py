import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from trading.binance_api import get_candlestick_data
from indicators.technical_analysis import calculate_ema, calculate_rsi, calculate_macd, calculate_macd2
from config.settings import SYMBOL, INTERVAL, CANDLE_LIMIT, PERIODS, SHORT_PERIOD, LONG_PERIOD, SIGNAL_PERIOD

def main():

    print("|----------------------------CALCULAR CANDLESTICK----------------------------|")
    # Coletar dados de candlestick
    #df = get_candlestick_data(symbol=SYMBOL, interval=INTERVAL, limit=CANDLE_LIMIT)
    df = get_candlestick_data()
    #print(df.columns)
    print(df.tail())

     # Calcular EMA
    print("|----------------------------CALCULAR EMA----------------------------|")
    print({CANDLE_LIMIT})
    #df = calculate_ema(df, period=PERIODS) # pode ser ajustado no settings.py
    df = calculate_ema(df)
    
    print(df.tail())
    #print(df.columns)

    print("|----------------------------CALCULAR RSI----------------------------|")

    # Calcular RSI
    #print(df.head()) 
    df = calculate_rsi(df, period=PERIODS) # pode ser ajustado
    print(df.tail())


    print("|----------------------------CALCULAR MACD----------------------------|")    
    # Calcular MACD 
    df = calculate_macd(df, short_period=SHORT_PERIOD, long_period=LONG_PERIOD, signal_period=SIGNAL_PERIOD)
    print(df.tail())

    print("|----------------------------DADOS FINAIS----------------------------|")
    # Exibir os dados com os indicadores calculador
    print(df.tail())

if __name__ == "__main__":
    main()