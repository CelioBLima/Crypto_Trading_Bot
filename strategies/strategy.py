
from config.settings import EMA_PERIOD, RSI_PERIOD

def evaluate_trade_signals(data):
    """
    Avalia o DataFrame com indicadores e retorna sinais de trade.
    
    Parâmetros:
      - data: DataFrame contendo as colunas 'close', 'ema_14', 'rsi_14', 'macd', 'macd_signal', etc.
      
    Retorna:
      - 'buy' se as condições de compra forem atendidas,
      - 'sell' se as condições de venda forem atendidas,
      - 'hold' caso contrário.
    """
    ema_col = f'ema_{EMA_PERIOD}'
    rsi_col = f'rsi_{RSI_PERIOD}'
    # Exemplo de lógica:
    last = data.iloc[-1]
    
    # Sinal de compra: EMA cruza para cima, RSI indica sobrevenda, MACD confirma
    if last[ema_col] > last['close'] and last[rsi_col] < 30 and last['macd'] > last['macd_signal']:
        return 'buy'
    
    # Sinal de venda: EMA cruza para baixo, RSI indica sobrecompra, MACD confirma
    elif last[ema_col] < last['close'] and last[rsi_col] > 70 and last['macd'] < last['macd_signal']:
        return 'sell'
    
    return 'hold'