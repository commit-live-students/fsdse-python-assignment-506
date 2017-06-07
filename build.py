import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np


def load_data():
    """
    Enter your code here
    """
    titanic_data = pd.read_csv("./files/titanic.csv")
    return titanic_data


def draw_plot(titanic):
    """
    Enter your code here
    """
    total = titanic['Sex'].count()

    female_data = titanic['Sex']
    female = female_data[female_data.str.contains('female')].count()

    proportions = []
    proportions.append((float(female)/float(total))*100)
    proportions.append((float(total - female)/float(total))*100)
    return proportions



def draw_historgram(titanic):
    """
    Enter your code here
    """
    titanic.sort_values("Fare", inplace=True, ascending=False)
    print titanic.head()


titanic = load_data()
draw_plot(titanic)
draw_historgram(titanic)
