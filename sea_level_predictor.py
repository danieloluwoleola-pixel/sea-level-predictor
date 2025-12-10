# sea_level_predictor.py
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read the data
    df = pd.read_csv('epa-sea-level.csv')        # works if CSV is in same folder
    # or: df = pd.read_csv('data/epa-sea-level.csv') if you put it in a subfolder

    # Create scatter plot
    plt.figure(figsize=(14, 8))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='steelblue', s=30, alpha=0.8)

    # Line 1: using all data
    result_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(df['Year'].min(), 2051)
    plt.plot(years_all, result_all.slope * years_all + result_all.intercept,
             color='red', linewidth=2, label='Fit 1880–present')

    # Line 2: only 2000+
    df_recent = df[df['Year'] >= 2000]
    result_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    plt.plot(years_recent, result_recent.slope * years_recent + result_recent.intercept,
             color='green', linewidth=2, label='Fit 2000–present')

    # Labels & style
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Save and return
    plt.savefig('sea_level_plot.png')
    plt.show()          # this will pop up the plot in PyCharm!
    return plt.gcf()