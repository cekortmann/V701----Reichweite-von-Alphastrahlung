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
                                  std_devs as stds)

p, N, chann, E, Nmax, x = np.genfromtxt('Abstand4.5cm.txt', unpack=True, skip_header=1)



plt.plot(x, N, 'xr', markersize=6 , label = 'Messdaten', alpha=0.5)
#plt.plot(xx, g(xx, *para), '-b', linewidth = 1, label = 'Ausgleichsfunktion', alpha=0.5)
plt.xlabel(r'$x \, / \, \mathrm{m}$')
plt.ylabel(r'$Zählrate$')
plt.legend(loc="best")                  # legend position
plt.grid(True)                          # grid style
#plt.xlim(22, 40)
#plt.ylim(-0.05, 1.05)
def näherung(a,b,x):
    return a*x+b

#para1, pcov1 = curve_fit(näherung, x, N)
#a,b,c,d,e= para1
#pcov1 = np.sqrt(np.diag(pcov1))
#fa, fb, fc ,fd,fe = pcov1
#ua = ufloat(a, fa) 
#ub = ufloat(b, fb)
#uc = ufloat(c, fc)
#ud = ufloat(d,fd)
#ue = ufloat(e,fe)
#print("ua",ua)
#print("ub",ub)
#print("uc",uc)
#print("ud",ud)
#print("ue",ue)
plt.plot(x, näherung(x,*para1), 'orange', linewidth = 1, label = 'Ausgleichskurve', alpha=0.5)

p1, N1, chann1, E1, Nmax1, x1 = np.genfromtxt('Abstand4.5cmshort.txt', unpack=True, skip_header=1)
params = curve_fit(näherung,x1,N1)
a_fit = params[0][0]
b_fit = params[0][1]
h=np.linspace(0.02,0.0285,10)
plt.plot(h, näherung(h,a_fit,b_fit), 'orange', linewidth = 1, label = 'Ausgleichskurve', alpha=0.5)


plt.legend(loc="best")
plt.savefig('build/4.5cmeffLaeng.pdf', bbox_inches = "tight")

