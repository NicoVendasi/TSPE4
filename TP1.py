# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:04:13 2020

@author: Karine
"""


import numpy as np
import matplotlib.pyplot as plt

# Points de mesure
c, pH = [0.100, 4.00e-2, 2.00e-2, 1.0e-2, 5.0e-3, 2.00e-2, 1.00e-2], [1.03, 1.41, 1.68, 2.08, 2.25, 1.70, 1.99]

# Trace les points expémimentaux 
plt.xlabel('Concentration en quantite de matiere c (mol/L)')
plt.ylabel('pH de la solution')
plt.title('Evolution du pH en fonction de la concentration en ion H3O+')
plt.scatter(x=c, y=pH, marker='+', label='Mesures')

# Trace du modele
cth = np.arange(1e-4, 1, 0.0001)
pHth = -np.log10(cth)
plt.plot(cth, pHth, color='red', label='Modelisation')

plt.legend()
plt.show()
