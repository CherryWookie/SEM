import numpy as np
p = 0.382 # p_c
b = 2

nu = np.log(b) / np.log((4*p**3) - (12*p**2) + (8*p))
print(nu)