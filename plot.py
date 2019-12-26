import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from matplotlib.ticker import AutoMinorLocator
def plot(df,headers):
    fig, ax = plt.subplots(constrained_layout=True, figsize=(16, 7))

    years = mdates.YearLocator()   # every year
    months = mdates.MonthLocator(interval=3)  # every 3 months
    years_fmt = mdates.DateFormatter('%Y')

    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)
    ax.xaxis.set_minor_locator(months)

    ax.tick_params(axis="x", labelsize=12, labelrotation=40)
    ax.tick_params(axis="y", labelsize=12)

    x_data=mdates.datestr2num(df['Dates'][-300:])
    ax.set_xlim(x_data[0],x_data[-1])
    ax.grid(alpha=0.3)
    ax.set_xlabel('Dates',fontweight='bold',fontsize='x-large')
    ax.set_ylabel('Inflation',fontweight='bold',fontsize='x-large')
    ax.set_title('Inflation over time, Argentina',fontweight='bold',fontsize='xx-large')

    ax.plot(x_data, df['Inflation'][-300:],"ob",markersize=1)
    plt.show()