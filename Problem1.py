#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 18:15:52 2023

@author: koichiro
"""

# Problem. 1d
print("(1d)")
import DataAnalysisTools as dat

# Problem. 1d, i
print("(i)")
data1 = dat.reportMeasurement([72.2,77.6,82.4,86.3,88.9], 0.3)
data2 = dat.reportMeasurement([80.1,81.45,81.5,81.34,82.01], 0.05)

print("data set 1: x_best ± dx_total = {:8.1f} ±{:8.1f} cm".format(data1[0],data1[1]))
print("data set 2: x_best ± dx_total = {:8.2f} ±{:8.2f} cm".format(data2[0],data2[1]))


# Problem. 1d, ii
print("(ii)")
percentage1 = dat.relativeUncertainty([72.2,77.6,82.4,86.3,88.9], 0.3)
percentage2 = dat.relativeUncertainty([80.1,81.45,81.5,81.34,82.01], 0.05)

print("data set 1: Relative Uncertainty = {:8.3f}".format(percentage1))
print("data set 2: Relative Uncertainty = {:8.3f}".format(percentage2))

# Problem. 1d, iii
print("(iii)")
agreement = dat.discrepancy(data1[0],data1[1],data2[0],data2[1])
print(agreement)

# Problem. 1d, iii
print("(iv)")
xresults = [data1[0],data2[0]]
dxresults = [data1[1],data2[1]]
print(xresults, dxresults)
combined = dat.combineMeasurements(xresults, dxresults)
print(combined)


