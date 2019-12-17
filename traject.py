import numpy as np
import matplotlib.pyplot as plt
hoek = 3.63 * np.pi / 180
x = np.linspace(0,8,1001)
y = np.zeros(len(x))
g = 9.81

def traject(v):

    for i in range(len(x)):
        if x[i]< 1.22:
            y[i] = 0
        elif x[i] < 1.22+4.89:
            y[i] = x[i] *0.31/4.89 -0.31/4.89 *1.22
            n= i
        else:
            y[i] = np.tan(hoek) * x[i-n] - x[i-n]**2 *g/(2* v**2 * (np.cos(hoek)**2)) + 0.31
            if y[i]>=0.2 and y[i]<=0.22:
                print('the car jumps :')
                print(x[i]-6.1)
                break
    return x,y

