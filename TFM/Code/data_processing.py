#Class with methods for data loading, cleaning, feature extraction and anomaly detection from source
#Future methods to load streaming data and upload live forecast

import pandas as pd
from crypto_utils import Features

class DataProcessor:

    def __init__(self, cryptos): # Constructor
        '''
        API conector and cryptos list to analize
        '''
        self.cryptos_names = cryptos

    def load_data(self): # Load method
        '''
        Get Data from cryptos selected in constructor or requested by args
        '''
        self.crypto_df = []
        for crypto_name in self.cryptos_names:
            print('Loading...', crypto_name)
            path = '/content/drive/MyDrive/Master IA/TFM - Crypto/Datasets/' + crypto_name + '.csv'
            df = pd.read_csv(path, header=[1])
            self.crypto_df.append(df)

    def clean_data(self, cryptos_names): # Clean method
        '''
        Cleans data to prepare it for better models comprehension and feature extraction
        '''
        i = 0
        for df in self.crypto_df:
            if self.cryptos_names[i] in cryptos_names: # if crypto is already loaded
                print('Drop columns')
                df.drop(columns=['symbol', 'unix', 'Volume USDT'], inplace = True)
                print('Drop Nan')
                df.dropna(inplace =True)
                print('Change date format')
                df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')
            i+=1


    def get_data(self, crypto_name):
        '''
        Returns crypto dataframe with crypto_name
        '''
        return(self.crypto_df[self.cryptos_names.index(crypto_name)])

    def feature_extraction(self, cryptos_names): # Feature extraction method
        '''
        Extracts features from df
        - Close-open difference
        - Close price above or below open (boolean)
        - Support and resistance levels
        - Relative strength index (RSI)
        - Average directional index (ADX)
        - Ichimoku cloud
        - Standard deviation
        - Bollinger bands
        - Stochastic oscillator
        - Moving average convergence divergence (MACD)
        - Fib. Retracement
        - Exponential moving average (EMA)
        - On Balance Volume
        '''
        i = 0
        for df in self.crypto_df:
            if self.cryptos_names[i] in cryptos_names:
                df['High Low Difference'] = df['high'] - df['low']
                df['Open Close Difference'] = df['open'] - df['close']
                df['Result'] = df.apply(Features.high_low(column='High Low Difference'), axis=1)
                df['Support 1'] = 0
                df['Support 2'] = 0
                df['Support 3'] = 0
                df['Support 4'] = 0
                df['Ressistance 1'] = 0
                df['Ressistance 2'] = 0
                df['Ressistance 3'] = 0
                df['Ressistance 4'] = 0
                df['RSI'] = 0
                df['ADX'] = 0
                df['Ichimoku'] = 0
                df['Standard Deviation'] = 0
                df['Bollinger'] = 0
                df['Stochastic Oscillator'] = 0
                df['MACD'] = 0
                df['Fib Retracement'] = 0
                df['EMA'] = 0
                df['OBV'] = 0
            i+=1

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