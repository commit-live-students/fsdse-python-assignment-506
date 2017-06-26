import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
--------------------------------------------------------------------------------
# Question 1:Create a dataframe with following data cleanup to make file redable
--------------------------------------------------------------------------------
def load_data():
    df = pd.read_csv("titanic.csv")
    # df.head(7)
    return df

load_data()

--------------------------------------------------------------------------------
# Question 2 : Create a pie chart presenting the male/female proportion.
--------------------------------------------------------------------------------
def draw_plot(df):

    proportions = []
    sum_instances = df['Sex'].value_counts()
    length = len(df['Sex'])
    proportions = list(sum_instances)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = ['Males','Females']
    explode = (0,0.1)
    sizes = proportions

    fig, ax1 = plt.subplots(figsize = (6,6))
    ax1.pie(sizes, explode = explode, labels = labels, shadow = True, startangle=90)
    ax1.axis('equal')    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Sex Proportions")
    plt.show()

--------------------------------------------------------------------------------
# Question 3: Create a histogram with the Fare paid
--------------------------------------------------------------------------------
def draw_histogram(df):

    sort_fare = df.sort_values('Fare')
    bins = np.arange(5,85)

    fig, axis = plt.subplots(figsize=(10,6))
    axis.hist(df['Fare'],bins=bins)
    axis.set_title("Fare Pay Histogram")
    axis.set_xlabel("Fare")
    axis.set_ylabel("Frequency")

    plt.tight_layout()
    plt.show()

# titanic = load_data()
# draw_historgram(df)
