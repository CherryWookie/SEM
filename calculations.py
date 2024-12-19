import numpy as np

# Constants
d = 1.6e-3  # Dielectric thickness in meters (converted from mm)
sigma = 5.9e7  # Conductivity of copper in S/m
t = 35e-6  # Metallization layer thickness in meters (converted from micrometers)
epsilon_r_prime = 4.2  # Relative permittivity
tan_d = 0.018  # Dielectric loss tangent
Z_0 = 50  # Characteristic impedance in ohms
w = 3.124e-3  # Strip width in meters (converted from mm)
f_0 = 1e9  # Frequency in Hz
c = 3e8  # Speed of light in m/s
mu_0 = 4 * np.pi * 1e-7  # Permeability of free space in H/m
omega = 2 * np.pi * f_0  # Angular Frequency
k_0 = omega / c     # K_0 obvi

# Surface resistance (R_s)
R_s = np.sqrt(omega * mu_0 / (2 * sigma))

# Effective permittivity (epsilon_eff)
epsilon_eff = ((epsilon_r_prime + 1) / 2) + ((epsilon_r_prime - 1) / 2) * (1 / np.sqrt(1 + ((12 * d) / w)))
epsilon_eff = 3.626

# Calculate Alphas
alpha_d = (k_0 * epsilon_r_prime * (epsilon_eff - 1) * tan_d) / (2 * np.sqrt(epsilon_eff) * (epsilon_r_prime - 1))
# alpha_d = (k_0 * epsilon_r_prime * (epsilon_eff - 1) * tan_d) / (2 * np.sqrt(epsilon_eff) * (epsilon_r_prime + 1))
alpha_c = (R_s / (Z_0 * w))

# Total attenuation (alpha_total)
alpha_total = alpha_d + alpha_c

# Convert to dB/m
alpha_d_db = alpha_d * 8.686
alpha_c_db = alpha_c * 8.686
alpha_total_db = alpha_total * 8.686

# Print values
print(epsilon_eff)
print(k_0)
print(R_s)
print(f"Alpha_D (Dielectric loss): {alpha_d:.6f} Nepers/m ({alpha_d_db:.6f} dB/m)")
print(f"Alpha_C (Conductor loss): {alpha_c:.6f} Nepers/m ({alpha_c_db:.6f} dB/m)")
print(f"Total Alpha: {alpha_total:.6f} Nepers/m ({alpha_total_db:.6f} dB/m)")


