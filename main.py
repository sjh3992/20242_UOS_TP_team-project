import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

from file_read import weather_read, subway_read

# csv 불러오기
weekends = False    # True: 주말/공휴일 분석, False: 평일 분석
weather = weather_read(weekends)
subway = subway_read(weekends)

# Pearsonr 상관관계 분석
names = [['강남', 'Gangnam'], ['잠실', 'Jamsil'], ['서울역', 'Seoul Station'], ['고속터미널', 'Express Bus Terminal'], ['홍대입구', 'Hongik University']]
i=1
outlier = 3.0

for name_k, name in names:
    df = pd.merge(subway[subway['Station'] == name_k], weather, on='Date')
    df = df[abs(df['Bording_z']) < outlier]
    statistic, pvalue = stats.pearsonr(df['Bording_index'], df['Rain'])
    print(name, statistic, pvalue)

    plt.subplot(2, 3, i)
    plt.title(name)
    plt.plot(df['Rain'], df['Bording_index'], 'kx')
    plt.xlabel('Rain[mm]')
    plt.ylabel('Passenger index')
    plt.grid()
    plt.axhline(df[df['Rain'] < 1.0]['Bording_index'].mean(), linestyle='--', color='green', label='<1.0mm')
    plt.axhline(df[(df['Rain']>=1.0) & (df['Rain']<10.0)]['Bording_index'].mean(), linestyle='--', color='blue', label='1.0mm~10.0mm')
    plt.axhline(df[df['Rain']>=10.0]['Bording_index'].mean(), linestyle='--', color='red', label='>=10.0mm')

    i += 1

plt.show()