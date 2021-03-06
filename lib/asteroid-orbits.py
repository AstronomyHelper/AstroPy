# Author: Michael Austin
# Date: 06/05/2018
# Data: NASA Asteroid Orbits CSV
# Purpose: Plot orbits and correlate to develop a prediction service

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Data frames of the CSVs
"""
Fields for Orbits: Name, Object Classification, Epoch (TDB), Orbit Axis (AU),
Orbit Eccentricity, Orbit Inclination (deg), Perihelion Argument (deg),
Node Longitude (deg), Mean Anomoly (deg), Perihelion Distance (AU),
Aphelion Distance (AU), Orbital Period (yr), Minimum Orbit Intersection Distance (AU), Orbital Reference, Asteroid Magnitude
"""

dfOrbit = pd.read_csv('data/orbits.csv')

# Diameter of the points in scatterplot 
area = 9

# Max is: 33.2
#Absolute magnitude (H): visual magnitude an observer would record if the asteroid were placed 1 AU away, and 1 AU from the Sun and at a zero phase angle.
max_mag = np.amax(dfOrbit['Asteroid Magnitude'])
# Min is: 9.45
min_mag =  np.amin(dfOrbit['Asteroid Magnitude'])

# Max is: 0.7069
max_OID = np.amax(dfOrbit['Minimum Orbit Intersection Distance (AU)'])
# Min is: 0.0
min_OID = np.amin(dfOrbit['Minimum Orbit Intersection Distance (AU)'])

#Prints data head to terminal. 
#print(dfOrbit.head(10))


plt.scatter(dfOrbit['Minimum Orbit Intersection Distance (AU)'], dfOrbit['Asteroid Magnitude'], s=area, c='blue', alpha=0.5)

plt.title('Orbital Scatterplot')
plt.xlabel('Magnitude')
plt.ylabel('Mean Orbital Distance')

plt.show()


print(max_mag)
print(min_mag)
print('---------------------------------------------------------------------------------------')
print(max_OID)
print(min_OID)