# Author: Michael Austin
# Date: 06/07/2018
# Data: NASA Solar and Lunar Eclipse CSVs
# Purpose: 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
Fields (lunar.csv): Catalog Number,Calendar Date,Eclipse Time,Delta T (s),Lunation Number,Saros Number,Eclipse Type,Quincena Solar Eclipse,Gamma,Penumbral Magnitude,Umbral Magnitude,Latitude,Longitude,Penumbral Eclipse Duration (m),Partial Eclipse Duration (m),Total Eclipse Duration (m)
"""
dfLunar = pd.read_csv('data/lunar.csv')

"""
Fields (solar.csv): Catalog Number,Calendar Date,Eclipse Time,Delta T (s),Lunation Number,Saros Number,Eclipse Type,Gamma,Eclipse Magnitude,Latitude,Longitude,Sun Altitude,Sun Azimuth,Path Width (km),Central Duration
"""
dfSolar = pd.read_csv('data/solar.csv')

print(dfLunar.head())
print('------------------------------------------------------------------------')
print(dfSolar.head())