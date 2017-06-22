import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    return pd.read_csv("titanic.csv")
    
def draw_plot(titanic):
    male_count = int(titanic['Sex'].value_counts()['male'])
    female_count = int(titanic['Sex'].value_counts()['female'])
    proportions = [male_count , female_count]
    fig1, axis = plt.subplots()
    axis.pie(proportions,labels=['Male','Female'])
    plt.show()

def draw_historgram(titanic):
    titanic=titanic.sort_values('Fare')
    fig, axis = plt.subplots()
    axis.hist(titanic['Fare'],bins=17)
    plt.show()
draw_historgram(load_data())print draw_plot(load_data())

# titanic = load_data()
# draw_historgram(titanic)
