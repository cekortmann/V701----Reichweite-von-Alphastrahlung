import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import pandas as pd
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)         # Abweichung:       stds(fehlerarray) = errarray


p, N, chann, E, Nmax, x = np.genfromtxt('Abstand3cm.txt', unpack=True, skip_header=1)



plt.plot(x, N, 'xr', markersize=6 , label = 'Messdaten', alpha=0.5)
#plt.plot(xx, g(xx, *para), '-b', linewidth = 1, label = 'Ausgleichsfunktion', alpha=0.5)
plt.xlabel(r'$x \, / \, \mathrm{m}$')
plt.ylabel(r'$Zählrate$')                 # legend position
plt.grid(True)                          # grid style
#plt.xlim(22, 40)
#plt.ylim(-0.05, 1.05)
p1, N1, chann1, E1, Nmax1, x1 = np.genfromtxt('Abstand3cmshort.txt', unpack=True, skip_header=1)

def näherung(a,b,x):
    return -a*x-b

params = curve_fit(näherung,x1,N1)
a_fit = params[0][0]
b_fit = params[0][1]
h=np.linspace(0.0185,0.026,10)
plt.plot(h, näherung(h,a_fit,b_fit), 'orange', linewidth = 1, label = 'Ausgleichskurve', alpha=0.5)

print('a_fit', a_fit)
print('b_fit', b_fit)
#x,y = np.genfromtxt('avg3.txt', unpack=True, skip_header=0)
#h1=np.linspace(0.0001,0.037,10)
#plt.plot(y, x , 'orange', linewidth = 1, label = 'Mittelwert der Reichweiten', alpha=0.5)
#print('a_fit', a_fit)
#print('b_fit', b_fit)
plt.legend(loc="best")

plt.savefig('build/3cmeffLaeng.pdf', bbox_inches = "tight")