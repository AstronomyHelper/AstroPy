# Author: Michael Austin
# Date: 06/05/2018
# Data: NASA Asteroid Impacts and Orbits CSVs
# Purpose Plot impacts and orbits and correlate to develop a prediction service

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Data frames of the CSVs
"""
Fields for Orbits: Name, Object Classification, Epoch (TDB), Orbit Axis (AU),
Orbit Eccentricity, Orbit Inclination (deg), Perihelion Argument (deg),
Node Longitude (deg), Mean Anomoly (deg), Perihelion Distance (AU),
Aphelion Distance (AU), Orbital Period (yr), Minimum Orbit Intersection Distance (AU), Orbital Reference, Asteroid Magnitude

Fields for impacts.csv: Name, Period Start, Period End, Possible Impacts,
Cumulative Impact Probability, Asteroid Velocity, Asteroid Magnitude, Asteroid Diameter (km),
Cumulative Palermo Scale, Maximum Palermo Scale, Maximum Torino Scale 
"""

dfOrbit = pd.read_csv('data/orbits.csv')
dfImpacts = pd.read_csv('data/impacts.csv')

#Prints data head to terminal. 
print(dfImpacts.head())
print()
print(dfOrbit.head())