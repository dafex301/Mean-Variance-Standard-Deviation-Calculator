import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import numpy as np
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=0)

# Clean data
df = df[
    (df['value'] <= (df['value'].quantile(0.975))) &
    (df['value'] >= (df['value'].quantile(0.025)))]
df.index = pd.to_datetime(df.index)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20,8))
    plt.plot(df.index, df['value'], color='r')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    grouped_df = df_bar.groupby([df.index.year, df.index.month])['value'].agg(np.mean).rename_axis(['year', 'month'])
    grouped_df = grouped_df.reset_index()

    # Draw bar plot
    df_bar = pd.pivot_table(grouped_df, values='value', index='year', columns='month')
    ax = df_bar.plot(kind='bar')
    fig = ax.get_figure()
    fig.set_size_inches(12, 8)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(figsize=(20,8))
    plt.subplot(1,2,1)
    ax = sns.boxplot(x="year", y="value", data=df_box)
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.title('Year-wise Box Plot (Trend)')

    plt.subplot(1,2,2)
    ax = sns.boxplot(x="month", y="value", data=df_box, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
