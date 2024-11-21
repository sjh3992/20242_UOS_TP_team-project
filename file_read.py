# file_read.py
# 날씨, 전철 이용객 csv 파일을 읽는 코드

import pandas as pd
import os

from week_filter import weekOnly, weekendOnly

def weather_read(weekends):
    df = pd.read_csv('weather.csv', index_col=False, encoding='CP949')
    df.drop(columns=['지점', '지점명'], inplace=True)
    df.columns = ['Date', 'Rain', 'Snow']
    df['Date'] = pd.to_datetime(df['Date'])

    # 날씨 정보 결측치를 0.0으로 조정
    date_range = pd.date_range(start='2024-01-01', end='2024-10-31')
    df = pd.merge(pd.DataFrame({'Date': date_range}), df, on='Date', how='left')
    df.fillna(0, inplace=True)

    return weekendOnly(df) if weekends else weekOnly(df)
    

def subway_read(weekends):
    os.chdir("./data_subway")
    df = pd.DataFrame()
    files = sorted(os.listdir())

    for file in files:
        if file.split(".")[1] == "csv":
            try:
                df = pd.concat([df, subway_process(pd.read_csv(file, index_col=False), weekends)])
            except UnicodeDecodeError:
                df = pd.concat([df, subway_process(pd.read_csv(file, index_col=False, encoding='CP949'), weekends)])
    
    return df

def subway_process(df, weekends):
    df.drop(columns=['등록일자'], inplace=True)
    df.columns = ['Date', 'Line', 'Station', 'Bording', 'Exiting']
    df['Date'] = pd.to_datetime(df['Date'].astype(str), format='%Y%m%d')
    df = weekendOnly(df) if weekends else weekOnly(df)
    df['Station'] = df['Station'].str.split('(').str[0].str.strip()
    df = df.groupby(['Date', 'Station']).agg({'Bording': 'sum', 'Exiting': 'sum'}).reset_index()
    df['Bording_index'] = df['Bording'] / df.groupby('Station')['Bording'].transform('mean') * 100
    df['Exiting_index'] = df['Exiting'] / df.groupby('Station')['Exiting'].transform('mean') * 100
    return df