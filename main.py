import os
import pandas as pd
import matplotlib.pyplot as plt

from file_read import weather_read, subway_read, climate_read
from analyze import rainfall

# csv 불러오기
weekends = False    # True: 주말/공휴일 분석, False: 평일 분석
climate = climate_read()
weather = weather_read(weekends)
subway = subway_read(weekends)

# 그래프 시각화 후 png 파일로 저장
os.chdir('../graph')
for stn in ['강남', '잠실', '서울역', '고속터미널', '홍대입구']:
    if not os.path.exists('./'+stn):
        os.mkdir('./'+stn)
    os.chdir('./'+stn)
    rainfall(pd.merge(subway[subway['Station']==stn], weather, on='Date'), stn)
    os.chdir('../')