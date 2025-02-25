import sys
import os
from tabulate import tabulate

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from trading.binance_api import get_candlestick_data
from indicators.technical_analysis import calculate_ema, calculate_rsi, calculate_macd, calculate_macd2
from strategies.strategy import evaluate_trade_signals
from config.settings import SYMBOL, INTERVAL, CANDLE_LIMIT, EMA_PERIOD, RSI_PERIOD, SHORT_PERIOD, LONG_PERIOD, SIGNAL_PERIOD

def main():

    print("|----------------------------CALCULAR CANDLESTICK----------------------------|")
    # Coletar dados de candlestick
    #df = get_candlestick_data(symbol=SYMBOL, interval=INTERVAL, limit=CANDLE_LIMIT)
    df = get_candlestick_data()
    #print(df.columns)
    #print(df.tail())
    print(tabulate(df.head(20), headers='keys', tablefmt='psql'))

     # Calcular EMA
    print("|----------------------------CALCULAR EMA----------------------------|")
    #print({CANDLE_LIMIT})
    #df = calculate_ema(df, period=PERIODS) # pode ser ajustado no settings.py
    df = calculate_ema(df)  
    #print(df.tail())
    #print(df.to_string())
    print(tabulate(df.head(20), headers='keys', tablefmt='psql')) # df.head(CANDLE_LIMIT)

    print("|----------------------------CALCULAR RSI----------------------------|")

    # Calcular RSI
    #print(df.head()) 
    df = calculate_rsi(df, period=RSI_PERIOD) # pode ser ajustado
    #print(df.tail())
    print(tabulate(df.head(20), headers='keys', tablefmt='psql'))


    print("|----------------------------CALCULAR MACD----------------------------|")    
    # Calcular MACD 
    df = calculate_macd(df, short_period=SHORT_PERIOD, long_period=LONG_PERIOD, signal_period=SIGNAL_PERIOD)
    #print(df.tail())
    print(tabulate(df.head(60), headers='keys', tablefmt='psql'))

    print("|-----------------------------ESTRATEGIA-----------------------------|")
    # Exibir a estrategia de trade avaliada (compra, venda, espera)
    strategi = evaluate_trade_signals(df)
    print('-----------------------------: '+strategi)

if __name__ == "__main__":
    main()