#Class with methods for data loading, cleaning, feature extraction and anomaly detection from source
#Future methods to load streaming data and upload live forecast

import pandas as pd

class DataProcessor:

    def __init__(self, cryptos): # Constructor
        '''
        API conector and cryptos list to analize
        '''
        self.cryptos = cryptos

    def load_data(self): # Load method
        '''
        Get Data from cryptos selected in constructor or requested by args
        '''
        self.crypto_df = []
        self.crypto_df_map = {}
        i = 0
        for crypto in self.cryptos:
            path = '/content/drive/MyDrive/Master IA/TFM - Crypto/Datasets/' + crypto + '.csv'
            df = pd.read_csv(path, header=[1])
            self.crypto_df.append(df)
            self.crypto_df_map[crypto] = i
            i+=1

    def clean_data(self, crypto_name): # Clean method
        '''
        Cleans data to prepare it for better models comprehension and feature extraction
        '''
        for df in self.crypto_df:
            df.drop(columns=['symbol', 'unix', 'Volume USDT'], inplace = True)
            df = df.dropna()
            df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')

    def get_data(self, crypto_name):
        '''
        Returns crypto dataframe with crypto_name
        '''
        return(self.crypto_df[self.cryptos.index(crypto_name)])

    def feature_extraction(self, crypto_name): # Feautre extraction method
        '''
        Extracts features from df
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

    def feature_selection(self, crypto_name): # Feautre selection method
        '''
        Eliminates features not relevant or highly correlated to others
        '''

    def detect_anomalies(self, crypto_name): # Anomaly detection method
        '''
        Build non supervised methods to detect outliers and anomalies and discard data
        '''

    def train_test_split(self, crypto_name): # Train-test split method
        '''
        Analize best train-test split method and returns datasets separated in train and test
        '''