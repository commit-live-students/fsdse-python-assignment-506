import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    """
    Enter your code here
    """
    df = pd.read_csv('./files/titanic.csv')
    return df.columns

def draw_plot(titanic):
    """
    Enter your code here
    """
    counts = titanic['Sex'].value_counts()
    proportions = counts.apply(lambda x: round((float(x)/counts.sum())*100.1))
    exp = (0.1, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(list(props), explode=explode, labels=tuple(props.index.tolist()))
    ax1.axis('equal')  
    plt.title('Sex Proportion')
    plt.show()


def draw_historgram(titanic):
    """
    Enter your code here
    """
    data = titanic['Fare'].sort_values(ascending=False)
    plt.hist(data, 50)
    plt.title('Fair Paid Histogram')
    plt.xlabel('Fare')
    plt.ylabel('Frequency')
    plt.show()



titanic = load_data()
print(titanic)
draw_plot(titanic)
draw_historgram(titanic)
