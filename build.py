import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    global df
    df = pd.read_csv("/home/ram/Desktop/Boks/titanic.csv")
    df = pd.DataFrame(df)
    return df

def draw_plot(titanic):
    male = df.Sex.value_counts().male
    female = df.Sex.value_counts().female

    labels = ['Male', 'Female']
    proportions = [male, female]
    explode = (0, 0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode)
    plt.title("Sex Proportion")
    plt.show()
    return

def draw_historgram(titanic):
    fares = df.Fare.sort_values()
    plt.hist(fares)
    plt.title("Fare Payed Histogram")
    plt.xlabel("Fare")
    plt.ylabel("Frequency")
    plt.show()
    return


# titanic = load_data()
# draw_historgram(titanic)
