import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats

# 공휴일
holiday = []
holiday.extend(['20240101', '20240209', '20240212', '20240301'])
holiday.extend(['20240410', '20240506', '20240515', '20240606'])
holiday.extend(['20240815', '20240916', '20240917', '20240918'])
holiday.extend(['20241001', '20241003', '20241009'])

# 날씨 csv 불러오기
weather = pd.read_csv('weather.csv', index_col=False, encoding='CP949')
weather = weather.drop(columns=['지점', '지점명'])
weather.columns = ['Date', 'Rain', 'Snow']
weather['Date'] = pd.to_datetime(weather['Date'])

# 날씨 정보 결측치를 0.0으로 조정
date_range = pd.date_range(start='2024-01-01', end='2024-10-31')
df = pd.DataFrame({'Date': date_range})
weather = pd.merge(df, weather, on='Date', how='left')
weather.fillna(0, inplace=True)

# 승하차량 csv 불러오기
os.chdir("./data_subway")
subway = pd.DataFrame()
files = sorted(os.listdir())

for file in files:
    if file.split(".")[1] == "csv":
        try:
            subway = pd.concat([subway, pd.read_csv(file, index_col=False)])
        except UnicodeDecodeError:
            subway = pd.concat([subway, pd.read_csv(file, index_col=False, encoding='CP949')])

subway = subway.drop(columns=['등록일자'])
subway.columns = ['Date', 'Line', 'Station', 'Bording', 'Exiting']
subway['Date'] = pd.to_datetime(subway['Date'].astype(str), format='%Y%m%d')
subway['Station'] = subway['Station'].str.split('(').str[0].str.strip()
subway = subway.groupby(['Date', 'Station']).agg({'Bording': 'sum', 'Exiting': 'sum'}).reset_index()

# 평일만 추출 (월요일=0, 화요일=1, ..., 금요일=4)
subway = subway[subway['Date'].dt.dayofweek < 5]
subway = subway[~subway['Date'].isin(pd.to_datetime(holiday))]
weather = weather[weather['Date'].dt.dayofweek < 5]
weather = weather[~weather['Date'].isin(pd.to_datetime(holiday))]

# 상관관계 분석

gangnam = pd.merge(subway[subway['Station']=='강남'], weather, on='Date')
jamsil = pd.merge(subway[subway['Station']=='잠실'], weather, on='Date')
seoul = pd.merge(subway[subway['Station']=='서울역'], weather, on='Date')
express = pd.merge(subway[subway['Station']=='고속터미널'], weather, on='Date')
hongik = pd.merge(subway[subway['Station']=='홍대입구'], weather, on='Date')

print("강남역", stats.pearsonr(gangnam['Bording'], gangnam['Rain']), sep='\n', end='\n')
print("잠실역", stats.pearsonr(jamsil['Bording'], jamsil['Rain']), sep='\n', end='\n')
print("서울역", stats.pearsonr(seoul['Bording'], seoul['Rain']), sep='\n', end='\n')
print("고속터미널역", stats.pearsonr(express['Bording'], express['Rain']), sep='\n', end='\n')
print("홍대입구역", stats.pearsonr(hongik['Bording'], hongik['Rain']), sep='\n', end='\n')

g = pd.DataFrame({'Date': gangnam['Date'], 'Bording': (gangnam['Bording'] / gangnam.loc[0]['Bording']) * 100, 'Rain': gangnam['Rain']})
j = pd.DataFrame({'Bording': (jamsil['Bording'] / jamsil.loc[0]['Bording']) * 100, 'Rain': jamsil['Rain']})
s = pd.DataFrame({'Bording': (seoul['Bording'] / seoul.loc[0]['Bording']) * 100, 'Rain': seoul['Rain']})
e = pd.DataFrame({'Bording': (express['Bording'] / express.loc[0]['Bording']) * 100, 'Rain': express['Rain']})
h = pd.DataFrame({'Bording': (hongik['Bording'] / hongik.loc[0]['Bording']) * 100, 'Rain': hongik['Rain']})

merged = pd.concat([g, j, s, e, h])

plt.plot(merged['Rain'], merged['Bording'], 'kx')
plt.axhline(merged[merged['Rain']<1.0]['Bording'].mean(), linestyle='--', color='green', label='<1.0mm')
plt.axhline(merged[(merged['Rain']>=1.0) & (merged['Rain']<10.0)]['Bording'].mean(), linestyle='--', color='blue', label='1.0mm~10.0mm')
plt.axhline(merged[merged['Rain']>=10.0]['Bording'].mean(), linestyle='--', color='red', label='>=10.0mm')
plt.xlabel('Rain[mm]')
plt.ylabel('Passenger(2024-01-02 is 100)')
plt.legend()
plt.xticks(range(0, 200, 5))
plt.yticks(range(0, 200, 5))
plt.xlim(-1, merged['Rain'].max()+1)
plt.ylim(merged[merged['Bording'] > 80]['Bording'].min()-1, merged[merged['Bording'] < 135]['Bording'].max()+1)
plt.grid()
plt.show()

print(merged['Rain'].max()+1)