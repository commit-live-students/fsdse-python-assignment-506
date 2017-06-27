import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    """
    Enter your code here
    """
    data=pd.read_csv("titanic.csv")
    return data

def draw_plot(titanic):
    """
    Enter your code here
    """
    male_mask = titanic_data['Sex'] == 'male'
    males = titanic_data[male_mask]['Sex'].value_counts()
    females = titanic_data[~male_mask]['Sex'].value_counts()
    proportions = [males,females]
    plt.pie(proportions, labels = ['Males','Females'], colors = ['blue','red'], startangle=90, autopct='%1.1f%%', explode = (0.1, 0))
    plt.axis('equal')
    plt.title('Sex Proportion')
    plt.show()

def draw_historgram(titanic):
    """
    Enter your code here
    """
    fares = sorted(titanic['Fare'])
    plt.hist(fares, bins = 100, range=(0,600))
    plt.title("Fare Payed Histogram")
    plt.xlabel("Fare")
    plt.ylabel("Frequency")
    plt.show()
# titanic = load_data()
# draw_historgram(titanic)
