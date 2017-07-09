import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def load_data():
    global titanic
    titanic = pd.read_csv('titanic.csv')
    return titanic
load_data()

def draw_plot():
    proportions = []
    occurences = titanic['Sex'].value_counts()
    length = len(titanic['Sex'])
    proportions = list(occurences)
    labels = ['Males','Females']
    explode = (0,0.1)
    sizes = proportions
    fig, ax1 = plt.subplots(figsize = (6,6))
    ax1.pie(sizes, explode = explode, labels = labels, shadow = True, startangle=90)
    ax1.axis('equal')
    ax1.set_title("Sex Proportions")
    plt.show()
draw_plot()

def draw_historgram(titanic):
    fare = titanic.sort_values('Fare')

    fig, axis = plt.subplots(figsize=(10,6))
    axis.hist(titanic['Fare'],bins = np.arange(5,85))
    axis.set_title("Fare Paid")
    axis.set_xlabel("Fare")
    axis.set_ylabel("Frequency")
    plt.tight_layout()
    plt.show()
draw_historgram(titanic)
