# visual.py
# 시각화 코드

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

from outlier import outlier

def min_rain_visual(df, name):
    df, df_out = outlier(df)

    statistic, pvalue = stats.pearsonr(df['Bording_z'], df['10분최다강수량'])
    print("10분최다강수량 ", statistic, pvalue, sep=', ', end='\n')

    plt.title(name)
    plt.xlabel('Rain[mm]')
    plt.ylabel('Passenger z-score')
    plt.grid()
    plt.axhline(df[df['10분최다강수량'] < 1.0]['Bording_z'].mean(), linestyle='--', color='green', label='<1.0mm')
    plt.axhline(df[(df['10분최다강수량']>=1.0) & (df['10분최다강수량']<10.0)]['Bording_z'].mean(), linestyle='--', color='blue', label='1.0mm~10.0mm')
    plt.axhline(df[df['10분최다강수량']>=10.0]['Bording_z'].mean(), linestyle='--', color='red', label='>=10.0mm')
    plt.plot(df['10분최다강수량'], df['Bording_z'], 'kx')
    plt.plot(df_out['10분최다강수량'], df_out['Bording_z'], 'rx')
    plt.savefig(name + '_10분최다강수량.png')
    plt.cla()

def hour_rain_visual(df, name):
    df, df_out = outlier(df)

    statistic, pvalue = stats.pearsonr(df['Bording_z'], df['1시간최다강수량'])
    print("1시간최다강수량 ", statistic, pvalue, sep=', ', end='\n')

    plt.title(name)
    plt.xlabel('Rain[mm]')
    plt.ylabel('Passenger z-score')
    plt.grid()
    plt.axhline(df[df['1시간최다강수량'] < 1.0]['Bording_z'].mean(), linestyle='--', color='green', label='<1.0mm')
    plt.axhline(df[(df['1시간최다강수량']>=1.0) & (df['1시간최다강수량']<10.0)]['Bording_z'].mean(), linestyle='--', color='blue', label='1.0mm~10.0mm')
    plt.axhline(df[df['1시간최다강수량']>=10.0]['Bording_z'].mean(), linestyle='--', color='red', label='>=10.0mm')
    plt.plot(df['1시간최다강수량'], df['Bording_z'], 'kx')
    plt.plot(df_out['1시간최다강수량'], df_out['Bording_z'], 'rx')
    plt.savefig(name + '_1시간최다강수량.png')
    plt.cla()

def day_rain_visual(df, name):
    df, df_out = outlier(df)

    statistic, pvalue = stats.pearsonr(df['Bording_z'], df['일강수량'])
    print("일강수량 ", statistic, pvalue, sep=', ', end='\n')

    plt.title(name)
    plt.xlabel('Rain[mm]')
    plt.ylabel('Passenger z-score')
    plt.grid()
    plt.axhline(df[df['일강수량'] < 1.0]['Bording_z'].mean(), linestyle='--', color='green', label='<1.0mm')
    plt.axhline(df[(df['일강수량']>=1.0) & (df['일강수량']<10.0)]['Bording_z'].mean(), linestyle='--', color='blue', label='1.0mm~10.0mm')
    plt.axhline(df[df['일강수량']>=10.0]['Bording_z'].mean(), linestyle='--', color='red', label='>=10.0mm')
    plt.plot(df['일강수량'], df['Bording_z'], 'kx')
    plt.plot(df_out['일강수량'], df_out['Bording_z'], 'rx')
    plt.savefig(name + '_일강수량.png')
    plt.cla()