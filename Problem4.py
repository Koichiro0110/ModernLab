#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:35:54 2023

@author: koichiro
"""

# Problem. 4
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import DataAnalysisTools as dat

# Problem. 4a
print("(a)")

data = pd.read_csv("DataProblem4.txt", comment="#")

data.columns = ["Resistance", "Runc", "Current", "Cunc"]
Resistance = data["Resistance"]
Runc = data["Runc"]
Current = data["Current"]
Cunc = data["Cunc"]

Resistance = np.sort(Resistance)
Runc = np.sort(Runc)
Current = np.sort(Current)
Cunc = np.sort(Cunc)

print(Resistance, Runc, Current, Cunc)

# Problem. 4b,4c
print("(b,c)")

# Now plot the data

Voltage = Resistance*Current

Vunc = Voltage*np.sqrt((Runc/Resistance)**2+(Cunc/Current)**2)

fig1 = plt.figure(figsize=(12,9))
ax = fig1.gca()
ax.errorbar(Resistance, Voltage, xerr = Runc, yerr = Vunc, label = "Data Points", color = 'blue', markersize = 5,
    linestyle = 'dashdot', linewidth = 1., elinewidth = 1., capsize = 3.5, marker = "o")

# Set the axes
ax.set_xlabel("Resistance [MΩ]", fontfamily = "serif", fontsize = 20)
ax.set_ylabel("Voltage [V]", fontfamily = "serif", fontsize = 20)
ax.set_title("Resistance vs Voltage",fontfamily = "serif", fontsize = 20)
ax.legend(fontsize = 15)

'''fit_values1 = dat.lineFit(Resistance, Voltage)
m1 = fit_values1[0]
b1 = fit_values1[1]
print(m1, b1)

ax.plot(Resistance, m1*Resistance+ b1, label = "Least-squared", color = "orange",
        marker = "", alpha = 0.9, linewidth=3)
'''
fit_values2 = dat.lineFitWt(Resistance, Voltage, Vunc)
m2 = fit_values2[0]
b2 = fit_values2[1]

ax.plot(Resistance, m2*Resistance + b2, label = "Chi-squared", color = "lime",
        marker = "", alpha = 0.9, linewidth=3)

ax.legend(fontsize = 15)

print("Chi-squared: m = {}, b = {}".format(m2, b2))

chi_sq2 = dat.fitQuality(Resistance,Voltage,Vunc,m2,b2)

print("Chi-squared: Q = {:4.3f}".format(chi_sq2))


# Problem. 4d
print("(d)")
print("Saved the figure.")
from matplotlib.backends.backend_pdf import PdfPages

pdf1 = PdfPages('OhmsLaw.pdf')
pdf1.savefig(fig1)
pdf1.close()

# Problem. 4e
print("(e)")
print("The fitting of the data clearly does not satisfy the law of Ω, which is evident from the distribution of each point in the data.",
      "This may simply be due to the inaccuracy of the measurement equipment or procedure we performed.")





