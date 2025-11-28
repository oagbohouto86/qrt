from config import *
from load_data import *
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class remove_high_correlation(BaseEstimator, TransformerMixin):
    def __init__(self, threshold=0.8):
        self.threshold = threshold
        self.to_remove = []
        self.columns_to_check = ['ANC', 'WBC', 'PLT', 'BM_BLAST', 'MONOCYTES', 'HB']
        

    def fit(self, X, y=None):
        X_new = X[self.columns_to_check]
        corr_matrix = X_new.corr().abs()
        upper_tri = corr_matrix.where(
            np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
        )
        self.to_remove = [
            column for column in upper_tri.columns if any(upper_tri[column] > self.threshold)
        ]
        return self

    def transform(self, X):
        return X.drop(columns=self.to_remove, errors='ignore')

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)