import pandas as pd
import numpy as np

class FeatureEngineer:
    def __init__(self, df):
        self.df = df

    def add_feature(self, new_column_name, feature_data):
        self.df[new_column_name] = feature_data
        return self

    def drop_feature(self, column_name):
        self.df = self.df.drop(column_name, axis=1)
        return self

    def fill_missing_values(self, column_name, value):
        self.df[column_name].fillna(value, inplace=True)
        return self

    def create_dummy_variables(self, column_name):
        dummy_variables = pd.get_dummies(self.df[column_name], prefix=column_name, drop_first=True)
        self.df = pd.concat([self.df, dummy_variables], axis=1)
        self.df = self.df.drop(column_name, axis=1)
        return self

    def bin_numerical_feature(self, column_name, bins, labels=False):
        binned_feature, bin_edges = pd.cut(self.df[column_name], bins, labels=labels, retbins=True)
        self.df[column_name] = binned_feature
        return bin_edges

    def log_transform(self, column_name):
        self.df[column_name] = np.log1p(self.df[column_name])
        return self

    def normalize_feature(self, column_name, method='z-score'):
        if method == 'z-score':
            self.df[column_name] = (self.df[column_name] - self.df[column_name].mean()) / self.df[column_name].std()
        elif method == 'min-max':
            self.df[column_name] = (self.df[column_name] - self.df[column_name].min()) / (self.df[column_name].max() - self.df[column_name].min())
        return self

    def feature_scaling(self, column_names, method='z-score'):
        if method == 'z-score':
            for column_name in column_names:
                self.df[column_name] = (self.df[column_name] - self.df[column_name].mean()) / self.df[column_name].std()
        elif method == 'min-max':
            for column_name in column_names:
                self.df[column_name] = (self.df[column_name] - self.df[column_name].min()) / (self.df[column_name].max() - self.df[column_name].min())
        return self

    def get_engineered_dataframe(self):
        return self.df