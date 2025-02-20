from dotenv import load_dotenv
import os
from binance.client import Client

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Chaves da API da Binance
API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Configuração do par de moedas e intervalo de tempo
#SYMBOL = "BTCUSDT"
SYMBOL = "ETHUSDT"
# INTERVAL = "1h"  # 1 hora
INTERVAL = Client.KLINE_INTERVAL_1MINUTE

# column: Nome da coluna de preços (default: 'close').
COLUMN = 'close'

# Número de candles a serem coletados
CANDLE_LIMIT = 80

# O número de períodos a serem considerados para o cálculos de EMA e RSI
PERIODS = 14

# Valores para calculo do MACD
# short_period: Período curto para a média móvel (default: 12).
# long_period: Período longo para a média móvel (default: 26).
# signal_period: Período para a linha de sinal (default: 9).
SHORT_PERIOD = 12
LONG_PERIOD = 26
SIGNAL_PERIOD = 9

