# week_filter.py
# 평일 또는 주말/공휴일의 데이터만 솎아내는 코드

import pandas as pd

def holidayList():
    holiday = ['20240101','20240209', '20240212', '20240301',
               '20240410', '20240506', '20240515', '20240606',
               '20240815', '20240916', '20240917', '20240918',
               '20241001', '20241003', '20241009'
               ]
    return pd.to_datetime(holiday)

def weekOnly(df):
    return df[(df['Date'].dt.dayofweek < 5) & (~df['Date'].isin(holidayList()))]

def weekendOnly(df):
    return df[(df['Date'].dt.dayofweek > 4) | (df['Date'].isin(holidayList()))]
