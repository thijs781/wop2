import numpy as np
import matplotlib.pyplot as plt

u_veer0 = 0.3
k_veer = 200
massa_car = 1.5
overbrenging = 1 / 24
mu_dynamisch = 0.45
x_rempunt = 6.1
rho = 1.2
oppervlak_car = 0.140
cw_car = 0.9
cr = 0.03
g = 9.81
hoek = 3.63 * np.pi / 180
x0 = 0
v0 = 0


def f_aandrijving(X):
    u_veer = u_veer0 - X * overbrenging
    if u_veer > 0:
        f_veer = u_veer * k_veer
        f_aandrijf = f_veer * overbrenging
        return f_aandrijf
    else:
        return 0


# def f_rem(X,V):
#     if X > x_rempunt and V > 0:
#         return massa_car*mu_dynamisch*g #alle wielen blokkeren
#     else:
#         return 0


def f_wrijving(X, V):
    f_luchtvrijving = 0.5 * rho * oppervlak_car *cw_car* V ** 2
    if V > 0 and X < x_rempunt:
        f_lagers = cr * massa_car * g
    else:
        f_lagers = 0
    return f_luchtvrijving + f_lagers


def versnelling(X, V):
    som_krachten = f_aandrijving(X) - Fz_X(X) - f_wrijving(X, V)
    return som_krachten / massa_car


def Fz_X(X):
    if X > 1.22 and X < 6.1:
        return massa_car * g * np.sin(hoek)
    else:
        return 0


def integreer(tijdspan):
    vf = 0
    a = np.zeros(len(tijdspan))
    v = np.zeros(len(tijdspan))
    x = np.zeros(len(tijdspan))
    x[0] = x0
    v[0] = v0
    delta_t = tijdspan[1] - tijdspan[0]
    for n in range(len(tijdspan)):
        a[n] = versnelling(x[n], v[n])
        if n < len(tijdspan) - 1:
            v[n + 1] = v[n] + delta_t * a[n]
            x[n + 1] = x[n] + delta_t * v[n]
        if x[n] > 6.1:
            vf = v[n]
            break

    return a, v, x, vf


tijd = np.linspace(0, 10, 101)
a, v, x, vf = integreer(tijd)

plt.plot(tijd, x, label='positie')
plt.plot(tijd, v, label='snelheid')
plt.plot(tijd, a, label='versnelling')
plt.xlabel('tijd [s]')
plt.legend()
plt.grid()
plt.show()
