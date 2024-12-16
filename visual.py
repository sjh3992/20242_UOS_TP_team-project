# visual.py
# 시각화 코드

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

from outlier import outlier

# 10분 최다 강수량에 따른 상관관계 분석
def min_rain_visual(df, name):
    df, df_out = outlier(df)

    statistic, pvalue = stats.pearsonr(df['Bording_z'], df['10분최다강수량'])
    print("10분최다강수량 ", statistic, pvalue, sep=', ', end='\n')

    plt.title(name + ' Rain(10min)')
    plt.xlabel('Rain[mm]')
    plt.ylabel('Passenger z-score')
    plt.xlim([float(df['10분최다강수량'].max())*(-0.1), float(df['10분최다강수량'].max())*1.1])
    plt.grid()
    plt.axhline(df[df['10분최다강수량'] < 1.0]['Bording_z'].mean(), linestyle='--', color='green', label='<1.0mm')
    plt.axhline(df[(df['10분최다강수량']>=1.0) & (df['10분최다강수량']<10.0)]['Bording_z'].mean(), linestyle='--', color='blue', label='1.0mm~10.0mm')
    plt.axhline(df[df['10분최다강수량']>=10.0]['Bording_z'].mean(), linestyle='--', color='red', label='>=10.0mm')
    plt.plot(df['10분최다강수량'], df['Bording_z'], 'kx')
    plt.plot(df_out['10분최다강수량'], df_out['Bording_z'], 'rx')
    plt.savefig(name + '_10분최다강수량.png')
    plt.cla()

# 1시간 최다 강수량에 따른 상관관계 분석
def hour_rain_visual(df, name):
    df, df_out = outlier(df)

    statistic, pvalue = stats.pearsonr(df['Bording_z'], df['1시간최다강수량'])
    print("1시간최다강수량 ", statistic, pvalue, sep=', ', end='\n')

    plt.title(name + ' Rain(1h)')
    plt.xlabel('Rain[mm]')
    plt.ylabel('Passenger z-score')
    plt.xlim([float(df['1시간최다강수량'].max())*(-0.1), float(df['1시간최다강수량'].max())*1.1])
    plt.grid()
    plt.axhline(df[df['1시간최다강수량'] < 1.0]['Bording_z'].mean(), linestyle='--', color='green', label='<1.0mm')
    plt.axhline(df[(df['1시간최다강수량']>=1.0) & (df['1시간최다강수량']<10.0)]['Bording_z'].mean(), linestyle='--', color='blue', label='1.0mm~10.0mm')
    plt.axhline(df[df['1시간최다강수량']>=10.0]['Bording_z'].mean(), linestyle='--', color='red', label='>=10.0mm')
    plt.plot(df['1시간최다강수량'], df['Bording_z'], 'kx')
    plt.plot(df_out['1시간최다강수량'], df_out['Bording_z'], 'rx')
    plt.savefig(name + '_1시간최다강수량.png')
    plt.cla()

# 일강수량에 따른 상관관계 분석
def day_rain_visual(df, name):
    df, df_out = outlier(df)

    statistic, pvalue = stats.pearsonr(df['Bording_z'], df['일강수량'])
    print("일강수량 ", statistic, pvalue, sep=', ', end='\n')

    plt.title(name + 'Rain')
    plt.xlabel('Rain[mm]')
    plt.ylabel('Passenger z-score')
    plt.xlim([float(df['일강수량'].max())*(-0.1), float(df['일강수량'].max())*1.1])
    plt.grid()
    plt.axhline(df[df['일강수량'] < 1.0]['Bording_z'].mean(), linestyle='--', color='green', label='<1.0mm')
    plt.axhline(df[(df['일강수량']>=1.0) & (df['일강수량']<10.0)]['Bording_z'].mean(), linestyle='--', color='blue', label='1.0mm~10.0mm')
    plt.axhline(df[df['일강수량']>=10.0]['Bording_z'].mean(), linestyle='--', color='red', label='>=10.0mm')
    plt.plot(df['일강수량'], df['Bording_z'], 'kx')
    plt.plot(df_out['일강수량'], df_out['Bording_z'], 'rx')
    plt.savefig(name + '_일강수량.png')
    plt.cla()

# 일최심신적설에 따른 상관관계 분석
def new_snow_visual(df, name):
    df, df_out = outlier(df)

    statistic, pvalue = stats.pearsonr(df['Bording_z'], df['일최심신적설'])
    print("일최심신적설 ", statistic, pvalue, sep=', ', end='\n')

    plt.title(name + 'Rain')
    plt.xlabel('Snow[cm]')
    plt.ylabel('Passenger z-score')
    plt.xlim([float(df['일최심신적설'].max())*(-0.1), float(df['일최심신적설'].max())*1.1])
    plt.grid()
    plt.axhline(df[df['일최심신적설'] < 1.0]['Bording_z'].mean(), linestyle='--', color='green', label='<1.0cm')
    plt.axhline(df[(df['일최심신적설']>=1.0) & (df['일최심신적설']<10.0)]['Bording_z'].mean(), linestyle='--', color='blue', label='1.0cm~10.0cm')
    plt.axhline(df[df['일최심신적설']>=10.0]['Bording_z'].mean(), linestyle='--', color='red', label='>=10.0cm')
    plt.plot(df['일최심신적설'], df['Bording_z'], 'kx')
    plt.plot(df_out['일최심신적설'], df_out['Bording_z'], 'rx')
    plt.savefig(name + '_일최심신적설.png')
    plt.cla()

# 일최심적설에 따른 상관관계 분석
def snow_visual(df, name):
    df, df_out = outlier(df)

    statistic, pvalue = stats.pearsonr(df['Bording_z'], df['일최심적설'])
    print("일최심적설 ", statistic, pvalue, sep=', ', end='\n')

    plt.title(name + 'Rain')
    plt.xlabel('Snow[cm]')
    plt.ylabel('Passenger z-score')
    plt.xlim([float(df['일최심적설'].max())*(-0.1), float(df['일최심적설'].max())*1.1])
    plt.grid()
    plt.axhline(df[df['일최심적설'] < 1.0]['Bording_z'].mean(), linestyle='--', color='green', label='<1.0cm')
    plt.axhline(df[(df['일최심적설']>=1.0) & (df['일최심적설']<10.0)]['Bording_z'].mean(), linestyle='--', color='blue', label='1.0cm~10.0cm')
    plt.axhline(df[df['일최심적설']>=10.0]['Bording_z'].mean(), linestyle='--', color='red', label='>=10.0cm')
    plt.plot(df['일최심적설'], df['Bording_z'], 'kx')
    plt.plot(df_out['일최심적설'], df_out['Bording_z'], 'rx')
    plt.savefig(name + '_일최심적설.png')
    plt.cla()