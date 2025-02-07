import pandas as pd
import ta

def calculate_ema(data: pd.DataFrame, column: str = 'close', period: int = 14) -> pd.Series:
    """
    Calcula a EMA (Média Móvel Exponencial) para os preços de uma coluna.
    
    Parâmetros:
      - data: DataFrame com os dados de preços.
      - column: Nome da coluna de preços (default: 'close').
      - period: Número de períodos para a EMA (default: 14).
      
    Retorna:
      - Uma Series contendo os valores da EMA.
    """
    ema_indicator = ta.trend.EMAIndicator(close=data[column], window=period)
    return ema_indicator.ema_indicator()

def calculate_rsi(data: pd.DataFrame, column: str = 'close', period: int = 14) -> pd.Series:
    """
    Calcula o RSI (Índice de Força Relativa) para os preços de uma coluna.
    
    Parâmetros:
      - data: DataFrame com os dados de preços.
      - column: Nome da coluna de preços (default: 'close').
      - period: Número de períodos para o cálculo do RSI (default: 14).
      
    Retorna:
      - Uma Series contendo os valores do RSI.
    """
    rsi_indicator = ta.momentum.RSIIndicator(close=data[column], window=period)
    return rsi_indicator.rsi()

def calculate_macd(data: pd.DataFrame, column: str = 'close', 
                   short_period: int = 12, long_period: int = 26, signal_period: int = 9) -> pd.DataFrame:
    """
    Calcula o MACD (Moving Average Convergence Divergence) para os preços de uma coluna.
    
    Parâmetros:
      - data: DataFrame com os dados de preços.
      - column: Nome da coluna de preços (default: 'close').
      - short_period: Período curto para a média móvel (default: 12).
      - long_period: Período longo para a média móvel (default: 26).
      - signal_period: Período para a linha de sinal (default: 9).
      
    Retorna:
      - Um DataFrame com as colunas:
          * 'macd': A linha MACD.
          * 'macd_signal': A linha de sinal.
          * 'macd_diff': A diferença (histograma).
    """
    macd_indicator = ta.trend.MACD(close=data[column], window_slow=long_period, window_fast=short_period, window_sign=signal_period)
    df_macd = pd.DataFrame({
        'macd': macd_indicator.macd(),
        'macd_signal': macd_indicator.macd_signal(),
        'macd_diff': macd_indicator.macd_diff()
    }, index=data.index)
    return df_macd
