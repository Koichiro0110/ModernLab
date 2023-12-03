#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 15:35:26 2023

@author: koichiro
"""

# Problem. 3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import DataAnalysisTools as dat

# Problem. 3c
print("(c)")

data = pd.read_csv("Data_sample.txt", comment="#")

data.columns = ["time", "velocity", "uncertainty"]
time = data["time"]
velocity = data["velocity"]
uncertainty = data["uncertainty"]

# Now plot the data
fig1 = plt.figure(figsize=(12,9))
ax = fig1.gca()
ax.errorbar(time, velocity, yerr = uncertainty, label = "Data Points", color = 'blue', markersize = 5,
    linestyle = 'dashdot', linewidth = 1., elinewidth = 1., capsize = 3.5, marker = "o")

# Set the axes
ax.set_xlabel("Time [s]", fontfamily = "serif", fontsize = 20)
ax.set_ylabel("Velocity [m/s]", fontfamily = "serif", fontsize = 20)
ax.set_title("Velocity vs Time",fontfamily = "serif", fontsize = 20)
ax.legend(fontsize = 15)

fit_values1 = dat.lineFit(time, velocity)
m1 = fit_values1[0]
b1 = fit_values1[1]

ax.plot(time, m1*time + b1, label = "Least-squared", color = "orange",
        marker = "", alpha = 0.9, linewidth=3)

fit_values2 = dat.lineFitWt(time, velocity, uncertainty)
m2 = fit_values2[0]
b2 = fit_values2[1]

ax.plot(time, m2*time + b2, label = "Chi-squared", color = "lime",
        marker = "", alpha = 0.9, linewidth=3)

ax.legend(fontsize = 15)

print("least-squared: m = {:4.3f}, b = {:4.3f}".format(m1, b1))
print("Chi-squared: m = {:4.3f}, b = {:4.3f}".format(m2, b2))

chi_sq1 = dat.fitQuality(time,velocity,uncertainty,m1,b1)
chi_sq2 = dat.fitQuality(time,velocity,uncertainty,m2,b2)

print("least-squared: Q = {:4.3f}".format(chi_sq1))
print("Chi-squared: Q = {:4.3f}".format(chi_sq2))

print("Why weighting the data gives a steeper or less steep slope than the fit without weighting:",
     "In the uncertainty weighted method, the slope is larger because it is computed to be closer to data points with smaller uncertainties, such as t = 7.5, 10, etc.")

# Problem. 3d
print("(d)")

dm2 = fit_values2[2]
db2 = fit_values2[3]
print("Chi-squared: m = {:4.3f} ± {:4.3f}, b = {:4.3f} ± {:4.3f}".format(m2, dm2, b2, db2))

from matplotlib.backends.backend_pdf import PdfPages

pdf1 = PdfPages('TimeVsVelocity.pdf')
pdf1.savefig(fig1)
pdf1.close()





