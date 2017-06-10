import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    titanic = pd.read_csv('./files/titanic.csv')
    #print titanic_csv.head()
    #return titanic_csv

### all trials
    #test = titanic_csv['Sex'].value_counts()
    #print test
    #proportions = []
    #test = titanic_csv['Sex'].value_counts()
    #proportions = pd.Series(test).tolist()
    #print proportions

load_data()

def draw_plot(titanic):
    proportions = []
    test = titanic['Sex'].value_counts()
    proportions = pd.Series(test).tolist()
    #print proportions
    labels = 'Males','Females'
    explode = (0, 0.1)
    fig, axes = plt.subplots()
    axes.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, colors=['b','r'])
    axes.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    axes.set_title('Sex_Proportions')

    plt.show()

#draw_plot(titanic)

def draw_historgram(titanic):
    b = np.arange(0,700,100)
    fare = titanic['Fare'].tolist()
    fare.sort()
    ax.set_xlabel('Fare')
    ax.set_ylabel('Frequency')
    ax.set_title('Fare Paid Histogram')
    ax.set_ylim(ymax = 350, ymin = 0)
    ax.hist(fare,bins=b)

    plt.show()
# titanic = load_data()
# draw_historgram(titanic)
