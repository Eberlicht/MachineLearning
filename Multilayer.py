import numpy as np
import random as rd
import matplotlib.pyplot as plt
import math
import time as time




# Netz mit drei Layer
# L = 1/2(Y-y)^2
# y = w*z2 + b
# z2 = sigmoid(y_1)
# y1 = w2*z1 +b2
# z1 = sigmoid(y_2)
# y2 = w3*x + b3

test = []

def random():
    return np.random.random()



def random1():
    a = np.random.random()
    b = a
    if a < 0.5:
        b = 0
    else:
        b = 1
    test.append(b)
    return b


def Sigmoid(n):
    Sigmoid = 1/(1 + np.exp(-n))
    return Sigmoid


def Ableitung_Sig(n):
    AbSig = Sigmoid(n)*(1-Sigmoid(n))
    return AbSig




def Ableitung_W(Y,y,z2):
    out1 = (y-Y)*z2
    return out1




def Ableitung_W2(Y,y,w,y1,z1):
    out2 = (y-Y)*w*Ableitung_Sig(y1)*z1
    return out2




def Ableitung_W3(Y,y,y1,y2,w,w2,x):
    delta = y-Y
    out3 = delta*w*Ableitung_Sig(y1)*w2*Ableitung_Sig(y2)*x
    return out3



def Ableitung_B(Y,y):
    out4 = (y-Y)
    return out4





def Ableitung_B2(Y,y,y1,w):
    out5 = (y-Y)*w*Ableitung_Sig(y1)
    return out5




def Ableitung_B3(Y,y,y1,y2,w):
    out6 = (y-Y)*w*Ableitung_Sig(y1)*Ableitung_Sig(y2)
    return out6


def loss(Y,y):
    return 0.5*(Y-y)**2


def neuron(w,x,b):
    y3 = (w * x) + b

    return y3
"""
i=0
while i < 10000000:
    random()
    i = i+1

einsen = []
nullen = []

for a in test:
    if test[a] == 1:
        einsen.append(test[a])
    else:
        nullen.append(test[a])






print("die Anzahl von Einsen ist :{}".format(len(einsen)))
#print(einsen)
print("die Anzahl von Nullen ist :{}".format(len(nullen)))
#print(nullen)


#plt.plot(np.arange(len(test)),test)
#plt.xlabel("epochen")
#plt.ylabel("fehler")
#plt.show()

"""







w = random1()
bias = random1()
w2 = random1()
bias2 = random1()
w3 = random1()
bias3 = random1()
losses = []
stepsize = 1e-2

x = [1,1,0,0,1,0,0,1] #dumm dumm ein

y = [1,1,0,0,1,0,0,1] #dumm dumm aus

start = time.time()

for epochs in range(100000):
    ls = 0

    for i in range(len(x)):

        y2 = neuron(w,x[i],bias)

        z2 = Sigmoid(y2)

        y1 = neuron(w2,z2,bias2)

        z1 = Sigmoid(y1)

        y_ = neuron(w3,z1,bias3)

        ls += (loss(y[i],y_))


        w = w - Ableitung_W(y[i],y_,z2) * stepsize

        bias = bias - Ableitung_B(y[i],y_) * stepsize

        w2 = w2 - Ableitung_W2(y[i],y_,w,y1,z1) * stepsize

        bias2 = bias2 - Ableitung_B2(y[i],y_,y1,w) * stepsize

        w3 = w3 - Ableitung_W3(y[i],y_,y1,y2,w,w2,x[i]) * stepsize

        bias3 = bias3 - Ableitung_B3(y[i],y_,y1,y2,w) * stepsize


    losses.append((ls)/len(x))

end = time.time()
print(end-start)
plt.plot(np.arange(len(losses)),losses)
plt.xlabel("epochen")
plt.ylabel("fehler")
plt.show()



for i in x:
    y2 = neuron(w, x[i], bias)

    z2 = Sigmoid(y2)

    y1 = neuron(w2, z2, bias2)

    z1 = Sigmoid(y1)

    y_ = neuron(w3, z1, bias3)

    print("x:{} y:{}".format(i,y_))



















































