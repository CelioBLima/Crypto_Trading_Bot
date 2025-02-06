import pandas as pd

# Função para calcular a EMA (Média Móvel Exponencial)
def calculate_ema(data, period=14, column='close'):
    return data[column].ewm(span=period, adjust=False).mean()

# Função para calcular o RSI (Índice de Força Relativa)
def calculate_rsi(data, period=14, column='close'):
    delta = data[column].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Função para calcular o MACD (Moving Average Convergence Divergence)
def calculate_macd(data, short_period=12, long_period=26, signal_period=9, column='close'):
    short_ema = calculate_ema(data, short_period, column)
    long_ema = calculate_ema(data, long_period, column)
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_period, adjust=False).mean()
    return macd, signal
