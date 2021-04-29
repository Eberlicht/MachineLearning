import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lin
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline






def read(path, dtype="csv"):
    data = eval("pd.read_" + dtype)(path)
    return data



def clean_data(dataframe,itemlist,drop=True,ax=1):
    if drop:
        dataframe = dataframe.drop(itemlist, axis=ax)


    else:
        dataframe = dataframe[itemlist]
    return dataframe

def take_Numbers(dataframe,items_to_pick):
    dataframe = np.array(dataframe[items_to_pick])
    return dataframe


def create_Plot(x,y,x_lbl="x",y_lbl="y",xstep=[], ystep=[],dpi=1080,grid=True,path=r".\ "):
    plt.plot(x,y)
    plt.xlabel(x_lbl)
    plt.ylabel(y_lbl)
    plt.xticks(xstep)
    plt.yticks(ystep)
    plt.grid(grid)
    plt.savefig(path, dpi=dpi)
    plt.show()

def LinReg(dataX, dataY,Time_to_begin,Time_into_future):
    reg = lin.LinearRegression()
    reg.fit(dataX, dataY)
    futureX = np.array([Time_to_begin]) + np.arange(Time_into_future)
    futureX = futureX.reshape(Time_into_future, 1)
    futureX = np.array(list(dataX) + list(futureX))
    plt.plot(dataX, dataY)
    plt.plot(futureX, reg.predict(futureX))
    plt.show()




def PolyReg(dataX,dataY,Time_to_begin,Time_into_future,Degree):
    reg = make_pipeline(PolynomialFeatures(Degree), Ridge())
    reg.fit(dataX, dataY)
    futureX = np.array([Time_to_begin]) + np.arange(Time_into_future)
    futureX = futureX.reshape(Time_into_future,1)
    futureX = np.array(list(dataX) + list(futureX))
    plt.plot(dataX,dataY)
    plt.plot(futureX, reg.predict(futureX))
    plt.show()










































