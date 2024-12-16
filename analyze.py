# analyze.py
# 상관관계 분석 코드

import os
import pandas as pd
import scipy.stats as stats

from visual import rain_visual, snow_visual

# z-score 방식 이상치 제거
def outlier(df):
    outlier = 3.0
    return df[abs(df['Bording_z']) < outlier], df[abs(df['Bording_z']) >= outlier]

# 강우량에 따른 상관관계 분석
def rainfall(df, stn):
    df, df_out = outlier(df)

    for i in ['10분최다강수량', '1시간최다강수량', '일강수량']:
        statistic, pvalue = stats.pearsonr(df['Bording_z'], df[i])
        print(i+": ", statistic, pvalue, pvalue<0.05, sep=', ')
        rain_visual(df, df_out, stn, i)
    
    for i in ['일최심신적설', '일최심적설', '합계3시간신적설']:
        statistic, pvalue = stats.pearsonr(df['Bording_z'], df[i])
        print(i+": ", statistic, pvalue, pvalue<0.05, sep=', ')
        snow_visual(df, df_out, stn, i)