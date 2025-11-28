# Import library
from config import *
from load_data import *
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np



# NEW BLOOD FEATURES
class bloodfeature(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return(self)
    
    def transform(self, X, y=None):
        X['RATIO_ANC_WBC'] = X['ANC'] / (X['WBC']- X['ANC'] + 1e-15)
        X['RATIO_PLT_BC'] = X['PLT'] / (X['WBC']- X['ANC'] + 1e-15)
        X['RATIO_BLAST_WBC'] = X['BM_BLAST'] / (X['WBC']- X['ANC'] + 1e-15)
        X['RATIO_BLAST_PLT'] = X['BM_BLAST'] / (X['PLT'] + 1e-15)
        return(X)
    
    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X)

