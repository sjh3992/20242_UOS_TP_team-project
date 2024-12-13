import pandas as pd
import os

from file_read import weather_read, subway_read, climate_read
from visual import rain_visual

# csv 불러오기
weekends = False    # True: 주말/공휴일 분석, False: 평일 분석
climate = climate_read()
weather = weather_read(weekends)
subway = subway_read(weekends)

names = [['강남', 'Gangnam'], 
         ['잠실', 'Jamsil'], 
         ['서울역', 'Seoul Station'], 
         ['고속터미널', 'Express Bus Terminal'], 
         ['홍대입구', 'Hongik University']]

for stn, name in names:
    os.chdir("../graph")
    rain_visual(pd.merge(subway[subway['Station']==stn], weather, on='Date'), name)