import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pd.set_option('display.max_columns', None)
train_data = pd.read_excel('data/income_data.xlsx')
# test_data = pd.read_excel('data/income_test.xlsx')

symbol_dict_df = pd.read_excel('data/symbol_dictionary.xlsx')
symbol_dict = dict(zip(symbol_dict_df['name_display'], symbol_dict_df['name_abbreviation']))


class PREPROCESS:
    def __init__(self, df, symbol_dict, drop_instance=True):
        self.df = df
        self.symbol_dict = symbol_dict
        self.drop_instance = drop_instance
        self.data_short = self.colunm_processing()
        self.data_after_na = self.nan_value_processing()

    def colunm_processing(self):
        data = self.df.rename(columns=symbol_dict)
        if self.drop_instance == True:
            data = data.drop('MARSUPWT', axis=1)
        return data

    def nan_value_processing(self):
        data = self.data_short.replace(' ?', np.NAN)

        return data

    def output(self, file_name):
        data = self.data_after_na
        data.to_excel('data/' + str(file_name) + '.xlsx', index=False)


preprocess = PREPROCESS(train_data, symbol_dict)
preprocess.output(file_name='train_with_na')
