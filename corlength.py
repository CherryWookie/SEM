import matplotlib.pyplot as plt
import numpy as np

# Fixed point/ P_c Value
p_c = 0.382
nu = 1
min = 1 # minimum b value
max = 10 # maximum b value

# Correlation length for nu = 1 and different b values
def calc_clength(p, p_c, b):
    return np.abs(p - p_c)**(-nu) / b

# Create Values
p_vals = np.linspace(0.25, .5, 500)

# Different values of b
b_values = np.arange(min,max+1)
clength_vals_list = [calc_clength(p_vals, p_c, b) for b in b_values]

# Plot correlation length vs prob for each b
plt.figure(figsize=(8, 6))

# Plot each value of b
for b, clength_vals in zip(b_values, clength_vals_list):
    plt.plot(p_vals, clength_vals, label=r"$b = %d$" % b)

# Plot vertical line for p_c
plt.axvline(p_c, color='red', linestyle='--', label=f"$p_c = {p_c}$")

# Plot limits and labels
plt.title("Correlation Length vs. Occupation Probability $p$ for $\\nu = 1$", fontsize=14)
plt.xlabel("$p$", fontsize=12)
plt.ylabel(r"Correlation Length $\xi$", fontsize=12)
plt.ylim(0, 250)  # Adjust the y-limits for better visualization
plt.legend()
plt.grid(True)
plt.show()
