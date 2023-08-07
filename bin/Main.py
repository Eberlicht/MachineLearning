import echtesML.Bevölkerung.Tools as tools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


if __name__ =="__main__":
    data = tools.read(path=r".\Data\BevoelkerungsentwicklungDe.xlsx", dtype="excel")
    data = tools.clean_data(data,["maennlich","weiblich"])
    x = tools.take_Numbers(data,["Unnamed: 0"])
    y = tools.take_Numbers(data, ["Insgesamt"])
    xstep = np.arange(10)*2+2000
    ystep = 8e7+np.arange(10)*1e6
    tools.create_Plot(x,y,x_lbl="Jahr",y_lbl="Einwohner Anzahl",xstep=xstep, ystep=ystep,dpi=1080,grid=True,path=r".\ ")


# justin ist Jenz
a = input("Welchen namen trägt Justin?")
if a == "Jenz":
    print("Korrekt")
else:
    print("Nein, er heißt Jenz")



































