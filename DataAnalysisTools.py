#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 19:14:11 2023

@author: koichiro Takahashi
"""
# Problem. 0

import numpy as np

# Problem. 1
# Problem. 1a
# Problem. 1a,i

def mean(xdata):
    N = len(xdata)
    mean = 1/N*np.sum(xdata)
    return mean

def statisticalUncertainty(xdata):
    
    N = len(xdata)
    best = mean(xdata)
    difference = xdata - best
    unc = np.sqrt(1/(N*(N-1))*np.sum(difference**2))
    return unc

# Problem. 1a,ii
def totalUncertainty(xdata, typeBUnc=0.0):
    typeAUnc = statisticalUncertainty(xdata)
    Unc_tot = 2*np.sqrt((typeAUnc)**2 + (typeBUnc)**2)
    return Unc_tot

# Problem. 1b
# Problem. 1b,i
def reportMeasurement(xdata, typeBUnc=0.0):
    return(mean(xdata),totalUncertainty(xdata, typeBUnc))
    
# Problem. 1b,ii
def relativeUncertainty(xdata, typeBUnc=0.0):
    Unc_relative = totalUncertainty(xdata, typeBUnc)/np.abs(mean(xdata))
    return Unc_relative

# Problem. 1c
# Problem. 1c,i
def discrepancy(xbest1, dx1, xbest2, dx2):
    disc = np.abs(xbest1 - xbest2)
    criterion = np.abs(dx1 + dx2)
    agreement = disc < criterion
    return (disc, criterion, agreement)

# Problem. 1c,ii
def combineMeasurements(xresults, dxresults):
    w = np.array([1/(i**2) for i in dxresults])
    x_best_combined = np.sum(w*np.array(xresults))/(np.sum(w))
    dx_total_combined = 1/(np.sqrt(np.sum(w)))
    return (x_best_combined, dx_total_combined)

# Problem. 2b
def lineFit(x,y):
    x = np.array(x)
    y = np.array(y)
    Ex = mean(x)
    Ey = mean(y)
    N = len(x)
    Exx = 1/N*np.sum(x**2)
    Exy = 1/N*np.sum(x*y)
    m = (Exy - Ex*Ey)/(Exx - Ex**2)
    b = (Exx*Ey - Ex*Exy)/(Exx - Ex**2)
    return (m,b)

# Problem. 2e
def relativeError(xmeasured, xaccepted):
    Rel = np.abs((xmeasured - xaccepted)/xaccepted)
    return Rel

# Problem. 3a
def lineFitWt(x,y,dy):
    x = np.array(x)
    y = np.array(y)
    dy = np.array(dy)
    w = np.array([1/(i**2) for i in dy])
    m_w = (np.sum(w)*np.sum(w*x*y) - np.sum(w*x)*np.sum(w*y))/(np.sum(w)*np.sum(w*x**2) - (np.sum(w*x))**2)
    b_w = (np.sum(w*x**2)*np.sum(w*y) - np.sum(w*x)*np.sum(w*x*y))/(np.sum(w)*np.sum(w*x**2) - (np.sum(w*x))**2)
    dm_w = np.sqrt(np.sum(w)/(np.sum(w)*np.sum(w*x**2) - (np.sum(w*x))**2))
    db_w = np.sqrt(np.sum(w*x**2)/(np.sum(w)*np.sum(w*x**2) - (np.sum(w*x))**2))
    return(m_w, b_w, dm_w, db_w)

# Problem. 3b
def fitQuality(x,y,dy,m,b):
    x = np.array(x)
    y = np.array(y)
    dy = np.array(dy)
    N = len(x)
    Q = 1/(N-2)*np.sum( ((y - m*x - b)/dy)**2 )
    return Q
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        