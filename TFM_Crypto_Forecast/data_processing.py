#Class with methods for data loading, cleaning, feature extraction and anomaly detection from source
#Future methods to load streaming data and upload live forecast

import pandas as pd

class DataProcessor:

    def __init__(self, cryptos): # Constructor
        '''
        API conector and cryptos list to analize
        '''
        self.cryptos = cryptos

    def load_data(self): # Load mehtod
        '''
        Get Data from cryptos selected in constructor or requested by args
        '''
        self.crypto_df = []
        for crypto in self.cryptos:
            path = '/content/drive/MyDrive/Master IA/TFM - Crypto/Datasets/' + crypto + '.csv'
            df = pd.read_csv(path)
            self.crypto_df.append(df)

    def clean_data(self): # Clean method
        '''
        Cleans data to prepare it for better models comprehension and feature extraction
        '''
        #for crypto in crypto_df:

    def get_crypto_df(self, crypto_name):
        '''
        Returns crypto dataframe
        '''
        return(self.crypto_df[self.cryptos.index(crypto_name)])

# Feautre extraction method
'''
- Relative strength index (RSI)
- Average directional index (ADX)
- Ichimoku cloud
- Standard deviation
- Bollinger bands
- Stochastic oscillator
- Moving average convergence divergence (MACD)
- Fib. Retracement
- Exponential moving average (EMA)
- Close-open difference
- Close price above or below open (boolean)
- Support and resistance levels
'''

# Anomaly detection method
'''
Build non supervised methods to detect outliers and anomalies and discard data
'''

# Train-test split method
'''
Analize best train-test split method and returns datasets separated in train and test
'''