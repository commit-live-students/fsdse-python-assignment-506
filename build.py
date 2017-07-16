import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    """
    Enter your code here
    """
    df = pd.read_csv("titanic.csv")
    return df

def draw_plot(titanic):
    """
    Enter your code here
    """
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
    """
    Enter your code here
    """
    titanic_fare = titanic.sort_values(by='Fare')
    bins = np.arange(1,100)
    plt.hist(titanic_fare['Fare'],bins)
    plt.xlabel('frequency')
    plt.ylabel('Fare')
    plt.title('Fare pay histogram')
    plt.show()

# titanic = load_data()
# draw_historgram(titanic)
