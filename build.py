import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    df = pd.read_csv("/home/nikhil/Desktop/titanic.csv")
    return df


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
