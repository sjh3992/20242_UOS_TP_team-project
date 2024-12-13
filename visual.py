# visual.py
# 시각화 코드

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

from outlier import outlier

def rain_visual(df, name):
    df, df_out = outlier(df)

    statistic, pvalue = stats.pearsonr(df['Bording_z'], df['Rain'])
    print(name, statistic, pvalue, sep=', ', end='\n')

    plt.title(name)
    plt.xlabel('Rain[mm]')
    plt.ylabel('Passenger z-score')
    plt.grid()
    plt.axhline(df[df['Rain'] < 1.0]['Bording_z'].mean(), linestyle='--', color='green', label='<1.0mm')
    plt.axhline(df[(df['Rain']>=1.0) & (df['Rain']<10.0)]['Bording_z'].mean(), linestyle='--', color='blue', label='1.0mm~10.0mm')
    plt.axhline(df[df['Rain']>=10.0]['Bording_z'].mean(), linestyle='--', color='red', label='>=10.0mm')
    plt.plot(df['Rain'], df['Bording_z'], 'kx')
    plt.plot(df_out['Rain'], df_out['Bording_z'], 'rx')
    plt.savefig(name + '_rain.png')