import echtesML.Bevölkerung.Tools as tools
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lin



if __name__=="__main__":
    data = tools.read(r"./Data/BevoelkerungsentwicklungDe.xlsx", "excel")
    data = tools.clean_data(data, ["Unnamed: 0","Insgesamt"], drop=False)
    dataY = tools.take_Numbers(data, items_to_pick=["Insgesamt"])
    dataX = tools.take_Numbers(data, items_to_pick=["Unnamed: 0"])
    reg = lin.LinearRegression()
    reg.fit(dataX, dataY)
    futureX = np.array([2019]) + np.arange(20)
    futureX = futureX.reshape(20,1)
    futureX = np.array(list(dataX) + list(futureX))
    plt.plot(dataX,dataY)
    plt.plot(futureX, reg.predict(futureX))
    plt.show()

























