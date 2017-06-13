import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    fh = open('./files/titanic.csv')
    df = pd.read_csv(fh)
    return df

def draw_plot(titanic):
    proportions = []
    for i in titanic.Sex.value_counts():
        proportions.append(i)
    plt.pie(proportions, labels=["Males", "Females"], autopct='%1.1f%%', explode=(0, 0.125), shadow=True, startangle=90)
    plt.title("Sex Proportions")
    plt.show()

def draw_historgram(titanic):
    fair_value = titanic.Fare.copy()
    fair_value.sort_values(inplace=True)
    fair_value.hist(bins=30)
    plt.xlabel('Fare')
    plt.ylabel('Frequency')
    plt.title('Fare Paid Histogram')
    plt.show()
