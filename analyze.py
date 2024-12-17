# analyze.py
# 상관관계 분석 코드

import pandas as pd
import scipy.stats as stats

from visual import rain_visual, snow_visual, temp_visual, wind_visual, sun_visual, time_visual

# z-score 방식 이상치 제거
def outlier(df):
    outlier = 3.0
    return df[abs(df['Bording_z']) < outlier], df[abs(df['Bording_z']) >= outlier]

# pearsonr 상관계수 분석
def pear(x, y, i):
    statistic, pvalue = stats.pearsonr(x, y)
    print(i+": ",
          "\033[91m"+str(statistic)+"\033[0m" if abs(statistic)<0.1 else "\033[92m"+str(statistic)+"\033[0m",
          "\033[92m"+str(pvalue)+"\033[0m" if pvalue<0.05 else "\033[91m"+str(pvalue)+"\033[0m", sep=', ')

# 강우량에 따른 상관관계 분석
def rainfall(df, stn):
    df, df_out = outlier(df)

    for i in ['10분최다강수량', '1시간최다강수량', '일강수량', '강수계속시간']:
        pear(df['Bording_z'], df[i], i)
        rain_visual(df, df_out, stn, i)
    
    for i in ['일최심신적설', '일최심적설', '합계3시간신적설']:
        pear(df['Bording_z'], df[i], i)
        snow_visual(df, df_out, stn, i)

def temp(df, stn):
    df, df_out = outlier(df)

    for i in ['평균기온', '최고기온', '최저기온', '평균기온평년차', '최고기온평년차', '최저기온평년차']:
        pear(df['Bording_z'], df[i], i)
        temp_visual(df, df_out, stn, i)

def wind(df, stn):
    df, df_out = outlier(df)

    for i in ['최대순간풍속', '최대풍속', '평균풍속', '풍정합']:
        pear(df['Bording_z'], df[i], i)
        wind_visual(df, df_out, stn, i)

def sun(df, stn):
    df, df_out = outlier(df)

    for i in ['1시간최다일사량', '합계일사량']:
        pear(df['Bording_z'], df[i], i)
        sun_visual(df, df_out, stn, i)

def time(df, stn):
    df, df_out = outlier(df)

    for i in ['합계일조시간', '안개계속시간']:
        pear(df['Bording_z'], df[i], i)
        time_visual(df, df_out, stn, i)