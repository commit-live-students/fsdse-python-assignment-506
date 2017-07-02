import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    df = pd.read_csv('titanic.csv')
    return df

def draw_plot(titanic):
    counts = df['Sex'].value_counts()
    # print counts
    proportions = list(counts)
    # female = df[df['Sex'] == 'female'].count()
    explode = (0, 0.1)
    fig, axes1 = plt.subplots(figsize = (6,6))
    axes1.pie(proportions,explode=explode,labels=['Male', 'Females'], colors=['b','r'], autopct='%1.1f%%', shadow=True, startangle=90)
    axes1.axis('equal')
    axes1.set_title('Sex_Proportions')
    plt.show()


def draw_historgram(titanic):
    fare = df.sort_values('Fare')
    fig, axes1 = plt.subplots(figsize = (10,6))
    axes1.hist(df['Fare'], bins = np.arange(0,90))
    axes1.set_xlabel('Fare')
    axes1.set_ylabel('Frequency')
    axes1.set_title('Fare Payed Histogram')
    plt.tight_layout()
    plt.show()


# titanic = load_data()
# draw_historgram(titanic)
