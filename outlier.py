# outlier.py

import pandas as pd

# z-score 방식 이상치 제거
def outlier(df):
    outlier = 3.0
    return df[abs(df['Bording_z']) < outlier], df[abs(df['Bording_z']) >= outlier]