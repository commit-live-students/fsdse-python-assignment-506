import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Create a dataframe with following data cleanup to make this file redable.
Create a function load_data to read CSV file and convert CSV data to dataframe.
Return dataframe.
"""
def load_data():
    df = pd.read_csv("titanic.csv")
    return df

"""
Create a pie chart presenting the male/female proportion.
create a function draw_plot.
Sum the instances of males and females
Put them into a list called proportions
Create a pie chart
Set plot title to Sex Proportion
Draw plot object. Image should match with the file provided inside files directory with name draw_plot
"""
def draw_plot(titanic):
    proportions = []
    sum_instances = titanic['Sex'].value_counts()
    length = len(titanic['Sex'])
    proportions = list(sum_instances)
    labels = ['Males','Females']
    explode = (0,0.1)
    sizes = proportions
    fig, ax1 = plt.subplots(figsize = (6,6))
    ax1.pie(sizes, explode = explode, labels = labels, shadow = True, startangle=90)
    ax1.axis('equal')
    ax1.set_title("Sex Proportions")
    plt.show()

"""
Create a histogram with the Fare paid
create a function draw_histogram.
Sort the fare value
Create bins interval using numpy
Set the title and labels
Draw plot object. Image should match with the file provided inside files directory with name draw_histogram
"""
def draw_historgram(titanic):
    sort_fare = titanic.sort_values('Fare')
    bins = np.arange(5,85)
    fig, axis = plt.subplots(figsize=(10,6))
    axis.hist(titanic['Fare'],bins=bins)
    axis.set_title("Fare Pay Histogram")
    axis.set_xlabel("Fare")
    axis.set_ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# titanic = load_data()
# draw_historgram(titanic)
