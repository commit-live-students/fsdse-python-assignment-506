import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    df = pd.read_csv('titanic.csv')
    return df
df = pd.read_csv('files/titanic.csv')

def draw_plot(df):
    sum_instances = df['Sex'].value_counts()
    print sum_instances
    proportions = list(sum_instances)
    #print proportions
    labels = ['Males','Females']
    explode = (0,0.1)
    sizes = proportions
    fig, ax1 = plt.subplots(figsize = (6,6))
    ax1.pie(sizes, explode = explode, labels = labels,colors=['b','r'],autopct='%.2f', shadow = True, startangle=90)
    ax1.axis('equal')
    ax1.set_title("Sex Proportions")
    plt.show()

def draw_histogram(df):
    fare_value = df.sort_values('Fare')
    #print fare_value
    fig, axis = plt.subplots(figsize=(10,6))
    axis.hist(df['Fare'],bins=np.arange(0,90))
    axis.set_title("Fare Pay Histogram")
    axis.set_xlabel("Fare")
    axis.set_ylabel("Frequency")
    plt.tight_layout()
    plt.show()


# titanic = load_data()
# draw_historgram(titanic)
