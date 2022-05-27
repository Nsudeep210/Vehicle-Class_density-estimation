import csv
import pandas as pd
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
vals=[]
index=count()
    
def animate(i):
    data=pd.read_csv('density.csv')
    vals.append(next(index))
    y=data['data']
    x=data['data2']
    plt.cla()
    plt.plot(x, y, label='Channel 2',color='red')
    plt.xlabel("Time-->(in deciseconds)")
    plt.ylabel("Trafific Density")
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()
