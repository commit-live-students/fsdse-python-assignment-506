import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    """
    Load of the data
    """
    titanic_data = pd.read_csv("./files/titanic.csv")
    return titanic_data


def draw_plot(titanic):
    """
    Solution of plotting
    """
    total = titanic['Sex'].count()

    female_data = titanic['Sex']
    female = female_data[female_data.str.contains('female')].count()
    male = total - female

    proportions = []
    proportions.append(female)
    proportions.append(male)
    print proportions

    # Data to plot
    labels = 'male', 'Female'
    colors = ['gold', 'yellow']
    explode = (0.1, 0)  # explode 1st slice

    # Plot
    plt.pie(proportions, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()

def draw_historgram(titanic):
    """
    To draw the pattern
    """
    titanic.sort_values("Fare", inplace=True, ascending=False)


titanic = load_data()
draw_plot(titanic)
draw_historgram(titanic)
