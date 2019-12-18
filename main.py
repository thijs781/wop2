import snelheid as snl
import traject as tj
import numpy as np
import matplotlib.pyplot as plt

def main():
    tijd = np.linspace(0, 10, 11)
    a, v, x , vf = snl.integreer(tijd)
    print('the speed at the end is')
    print(vf)
    x1,y1= tj.traject(vf)
    plt.plot(x1,y1)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
