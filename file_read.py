# file_read.py
# 날씨, 전철 이용객 csv 파일을 읽는 코드

import pandas as pd
import os

from week_filter import weekOnly, weekendOnly

# 평년기온 파일 불러오기
def climate_read():
    df = pd.read_csv('climate.csv', index_col=False)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# 기상관측자료 파일 불러오기
def weather_read(weekends):
    df = pd.read_csv('weather.csv', index_col=False)
    df['Date'] = pd.to_datetime(df['Date'])

    # 날씨 정보 결측치를 0.0으로 조정
    date_range = pd.date_range(start='2020-01-01', end='2024-12-10')
    df = pd.merge(pd.DataFrame({'Date': date_range}), df, on='Date', how='left')
    df.fillna(0, inplace=True)

    return weekendOnly(df) if weekends else weekOnly(df)

# 전철 탑승객 자료 파일 불러오기
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

# 전철 탑승객 데이터 전처리
def subway_process(df, weekends):
    df.drop(columns=['등록일자'], inplace=True)     # '등록일자' 열은 불필요하므로 삭제
    df.columns = ['Date', 'Line', 'Station', 'Bording', 'Exiting']  # 헤더명 변경
    df['Date'] = pd.to_datetime(df['Date'].astype(str), format='%Y%m%d')    # pd.datetime 형식으로 type 변경
    df = weekendOnly(df) if weekends else weekOnly(df)  # 평일/휴일 필터링
    df = df.groupby(['Date', 'Station']).agg({'Bording': 'sum', 'Exiting': 'sum'}).reset_index()    # 환승역끼리 이용객 수 합산
    df['Station'] = df['Station'].str.split('(').str[0].str.strip() # 부역명 제거
    df['Bording_z'] = df.groupby('Station')['Bording'].transform(lambda x: (x - x.mean()) / x.std())    # 승차인원 z값
    df['Exiting_z'] = df.groupby('Station')['Exiting'].transform(lambda x: (x - x.mean()) / x.std())    # 하차인원 z값
    return df