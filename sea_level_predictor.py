import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    #print(df.describe())
    #print(df.info())
    #print(df["CSIRO Adjusted Sea Level"])
    #print(df.sample(50).sort_values(by="Year"))
    


    # Create scatter plot
    plt.figure(figsize=(15, 7))
    plt.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level", marker="*")


    # Create first line of best fit
    res = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    print(f"R-squared: {res.rvalue**2:.7f}")
    extended_years = np.arange(1880, 2051, 1)
    print('resint', res.intercept)
    plt.plot(extended_years, res.intercept + res.slope*extended_years, 'm', label="Avg + predict 1880 ~ 2050")

    
    # Create second line of best fit
    short_df = df[df["Year"] >= 2000]
    #print(short_df)
    res = linregress(x=short_df["Year"], y=short_df["CSIRO Adjusted Sea Level"])
    print(f"R-squared: {res.rvalue**2:.7f}")
    shortened_years = np.arange(2000, 2051, 1)
    print('resint', res.intercept)
    plt.plot(shortened_years, res.intercept + res.slope*shortened_years, 'c', label="Avg + predict 2000 ~ 2050")


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()