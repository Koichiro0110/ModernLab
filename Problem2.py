#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:50:47 2023

@author: koichiro
"""

# Problem. 2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import DataAnalysisTools as dat

# Problem. 2a
print("(a)")
print("Plotted")
data = pd.read_csv("millikan.txt", comment="#")

data.columns = ["Frequency", "Voltage"]
Frequency = data["Frequency"]
Voltage = data["Voltage"]


# Make a plot.
fig1 = plt.figure(figsize = (12,9))
ax = fig1.gca()

ax.plot(Frequency, Voltage, label = "Data Points", color = "blue",
        markersize=10, marker = "o",)

# Set the axes.
ax.set_xlabel("Frequency [Hz]", fontfamily = "serif", fontsize = 20)
ax.set_ylabel("Voltage [V]", fontfamily = "serif", fontsize = 20)
ax.set_title("Millikan's Experiment", fontfamily = "serif", fontsize = 30)
ax.legend(fontsize = 15)

# Problem. 2c
print("(c)")
print("Plotted")

# Make a plot.
fig2 = plt.figure(figsize = (12,9))
ax = fig2.gca()

ax.plot(Frequency, Voltage, label = "Data Points", color = "blue",
        markersize=10, marker = "o",)

# Set the axes.
ax.set_xlabel("Frequency [Hz]", fontfamily = "serif", fontsize = 20)
ax.set_ylabel("Voltage [V]", fontfamily = "serif", fontsize = 20)
ax.set_title("Millikan's Experiment", fontfamily = "serif", fontsize = 30)
ax.legend(fontsize = 15)
fit_values = dat.lineFit(Frequency, Voltage)
m = fit_values[0]
b = fit_values[1]
ax.plot(Frequency, m*Frequency + b, label = "Fitting function", color = "orange",
        marker = "", alpha = 0.9, linewidth=3)
ax.legend(fontsize = 15)
print("m = {:4.2f}e-15, b = {:4.2f}".format(fit_values[0]*1e15, fit_values[1]))

# Problem. 2d
print("(d)")

unit_charge = 1.602176634e-19
Planck_measured = m*unit_charge
print("Measured Planck's constant = {:4.3}".format(Planck_measured))

# Problem. 2e
print("(e)")

Planck_accepted = 6.62607015e-34
Percent_error = 100*dat.relativeError(Planck_measured, Planck_accepted)
print("The percent error = {:4.3}%".format(Percent_error))

















