import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    filename = "files/titanic.csv"
    df = pd.read_csv(filename)
    return df

def draw_plot(df):
    female_count = df.groupby(by="Sex").size().female
    male_count = df.groupby(by="Sex").size().male

    plt.figure(1, figsize=(6,6))

    labels = ["Male", "Famale"]
    sizes = [male_count, female_count]
    colors = ['blue', 'red']
    explode=(0, 0.05)
    plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90, explode=explode)
    plt.title('Sex Proportion')

    #plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


def draw_histogram(df):
    sorted_fare = df["Fare"].sort_values()
    plt.hist(sorted_fare, bins='auto')
    plt.xlabel("Fare")
    plt.ylabel("Frequency")
    plt.title("Fare Payed Histogram")
    plt.grid(True)

    plt.show()

draw_histogram(df)


# titanic = load_data()
# draw_historgram(titanic)
