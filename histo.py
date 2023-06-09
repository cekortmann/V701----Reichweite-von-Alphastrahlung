import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.stats import sem
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


n, N = np.genfromtxt('100Werte.txt', unpack=True, skip_header=1)

mean=np.mean(N)
sem=sem(N)
std=np.std(N)
var=std**2
print(mean,"+-",sem,"Varianz=",var)

x1=np.linspace(np.min(n),np.max(n))

gaus=np.random.normal(loc=mean,scale=std,size=10000)
poii=np.random.poisson(lam=mean,size=10000)

plt.grid()
plt.hist(N,bins=10,density=True,label="Verteilung der Messwerte")
plt.xlabel(r'Zählrate pro 10 Sekunden')
plt.ylabel(r'Relative Häufigkeit')
plt.hist(poii,bins=10,density=True,histtype="step",color="k",label="Poissonverteilung")
plt.hist(gaus,bins=10,density=True,histtype="step",color="r",label="Normalverteilung")
plt.legend(loc='best')

plt.savefig('build/histo.pdf', bbox_inches = "tight")