import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data(pth):
    df = pd.read_csv(pth)
    return df



def draw_plot(titanic):
    m,f = titanic['Sex'].value_counts().values
    m_i = int(m)
    f_i = int(f)
    val = [m_i,f_i]
    labels = ['Male','Female']
    explode = (0.2,0.2)
    plt.pie(val,explode=explode,labels=labels,shadow=True)
    plt.show()


def draw_historgram(titanic):
    """
    Enter your code here
    """

ds = load_data('files/titanic.csv')
draw_plot(ds)
# titanic = load_data()
# draw_historgram(titanic)
