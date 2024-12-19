import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Constants
Z0 = 50  # Characteristic impedance (Ohms)
ZL = 75 + 1j*50  # Load impedance (Ohms)
beta = 2 * np.pi  # Assume wavelength λ = 1 for simplicity

# Step 1: Normalize load impedance
zL = ZL / Z0

# Step 2: Reflection coefficient at the load
Gamma_L = (zL - 1) / (zL + 1)

# Function to find length l1 where input impedance has real part Z0
def find_l1(l1):
    Gamma_in = Gamma_L * np.exp(-1j * 2 * beta * l1)  # Reflection coefficient at distance l1
    Zin = Z0 * (1 + Gamma_in) / (1 - Gamma_in)  # Input impedance
    return Zin.real - Z0  # Real part must equal Z0

# Solve for l1 using fsolve
l1_initial_guess = 0.1  # Initial guess for l1
l1_solution = fsolve(find_l1, l1_initial_guess)[0]

# Find the input impedance at l1
Gamma_in = Gamma_L * np.exp(-1j * 2 * beta * l1_solution)
Zin_at_l1 = Z0 * (1 + Gamma_in) / (1 - Gamma_in)

# Step 3: Stub admittance required to cancel out susceptance
B_stub_required = -Zin_at_l1.imag / Z0  # Normalize susceptance

# Function to find l2 for open-circuited stub
def find_l2(l2):
    B_stub = np.tan(beta * l2)  # Susceptance of open-circuited stub
    return B_stub - B_stub_required

# Solve for l2 using fsolve
l2_initial_guess = 0.1  # Initial guess for l2
l2_solution = fsolve(find_l2, l2_initial_guess)[0]

# Results
print(f"Required l1 (series line length): {l1_solution:.4f} λ")
print(f"Required l2 (stub length): {l2_solution:.4f} λ")
