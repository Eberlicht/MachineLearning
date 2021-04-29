import echtesML.Bevölkerung.Tools as tools
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline



if __name__=="__main__":

    data = tools.read(r"./Data/BevoelkerungsentwicklungDe.xlsx", "excel")
    data = tools.clean_data(data, ["Unnamed: 0","Insgesamt"], drop=False)
    dataY = tools.take_Numbers(data, items_to_pick=["Insgesamt"])
    dataX = tools.take_Numbers(data, items_to_pick=["Unnamed: 0"])
    reg = make_pipeline(PolynomialFeatures(10), Ridge())
    reg.fit(dataX, dataY)
    futureX = np.array([2019]) + np.arange(10)
    futureX = futureX.reshape(10,1)
    futureX = np.array(list(dataX) + list(futureX))
    plt.plot(dataX,dataY)
    plt.plot(futureX, reg.predict(futureX))
    plt.show()



















