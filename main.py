import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

from file_read import weather_read, subway_read

# csv 불러오기
weekends = False    # True: 주말/공휴일 분석, False: 평일 분석
weather = weather_read(weekends)
subway = subway_read(weekends)

# Pearsonr 상관관계 분석
name = '홍대입구'
statistic, pvalue = stats.pearsonr(subway[subway['Station'] == name]['Bording'], weather['Rain'])
print(name, statistic, pvalue)

'''
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

'''

'''
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
plt.grid()
plt.show()
'''