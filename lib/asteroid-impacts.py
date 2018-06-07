# Author: Michael Austin
# Date: 06/06/2018
# Data: NASA Asteroid Impacts CSV
# Purpose Plot impacts and magnitudes; correlate to develop a prediction service

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfImpacts = pd.read_csv('data/impacts.csv')

"""
Fields for impacts.csv: Name, Period Start, Period End, Possible Impacts,
Cumulative Impact Probability, Asteroid Velocity, Asteroid Magnitude, Asteroid Diameter (km),
Cumulative Palermo Scale, Maximum Palermo Scale, Maximum Torino Scale 
"""

max_vel= np.amax(dfImpacts['Asteroid Velocity'])
min_vel= np.amax(dfImpacts['Asteroid Velocity'])

#Prints data head to terminal. Commented out at the moment. 
#print(dfImpacts.head(10))

#Displays the ASteroid Velocity as a function of Magnitude, measured as the albedo of the asteroid. Visualized with a scatterplot. 
#Albedo: ratio of the light received by a body to the light reflected by that body. Albedo values range from 0 (pitch black) to 1 (perfect reflector).
plt.scatter(dfImpacts['Asteroid Velocity'], dfImpacts['Asteroid Magnitude'], s=9, c='red', alpha=0.5)
plt.title('Asteroid Velocities Compared to Magnitudes')
plt.xlabel('Magnitude')
plt.ylabel('Velocity')
plt.show()