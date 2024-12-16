import numpy as np

Z_0 = 50 # Ohms
Z_L = 100 # Ohms

Gamma = (Z_L - Z_0)/ (Z_L + Z_0)

print(f'Reflection Coefficient: {Gamma}')

