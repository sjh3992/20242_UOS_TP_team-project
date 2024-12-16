# visual.py
# 시각화 코드

import pandas as pd
import matplotlib.pyplot as plt

# 강수량 분석 시각화
def rain_visual(df, df_out, stn, head):
    # df: |z|<3.0, df_out: |z|>=3.0, stn: 역명, head: 분석헤더명
    plt.title(stn + head)
    plt.xlabel('Rain[mm]')
    plt.ylabel('Passenger z-score')
    plt.xlim([float(df[head].max())*(-0.1), float(df[head].max())*1.1])
    plt.grid()
    plt.axhline(df[df[head] < 1.0]['Bording_z'].mean(), linestyle='--', color='green', label='<1.0mm')
    plt.axhline(df[(df[head]>=1.0) & (df[head]<10.0)]['Bording_z'].mean(), linestyle='--', color='blue', label='1.0mm~10.0mm')
    plt.axhline(df[df[head]>=10.0]['Bording_z'].mean(), linestyle='--', color='red', label='>=10.0mm')
    plt.plot(df[head], df['Bording_z'], 'kx')
    plt.plot(df_out[head], df_out['Bording_z'], 'rx')
    plt.savefig(stn + '_' + head + '.png')
    plt.cla()

# 적설량 분석 시각화
def snow_visual(df, df_out, stn, head):
    # df: |z|<3.0, df_out: |z|>=3.0, stn: 역명, head: 분석헤더명
    plt.title(stn + head)
    plt.xlabel('Snow[cm]')
    plt.ylabel('Passenger z-score')
    plt.xlim([float(df[head].max())*(-0.1), float(df[head].max())*1.1])
    plt.grid()
    plt.axhline(df[df[head] < 0.5]['Bording_z'].mean(), linestyle='--', color='green', label='<0.5cm')
    plt.axhline(df[(df[head]>=0.5) & (df[head]<5.0)]['Bording_z'].mean(), linestyle='--', color='blue', label='0.5cm~5.0cm')
    plt.axhline(df[df[head]>=5.0]['Bording_z'].mean(), linestyle='--', color='red', label='>=5.0cm')
    plt.plot(df[head], df['Bording_z'], 'kx')
    plt.plot(df_out[head], df_out['Bording_z'], 'rx')
    plt.savefig(stn + '_' + head + '.png')
    plt.cla()