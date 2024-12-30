import numpy as np
import matplotlib.pyplot as plt

# Define the renormalization function numerically
def R_b_numeric(p):
    return p**4 - 4*p**3 + 4*p**2

# Create values of p for the plot
p_values = np.linspace(0, 1.5, 500)
R_values = R_b_numeric(p_values)

# Plot R_b(p) and the y = p line
plt.figure(figsize=(8, 6))
plt.plot(p_values, R_values, label=r"$R_b(p)$", color='blue')
plt.plot(p_values, p_values, label=r"$y = p$", color='red', linestyle='--')

# Mark the fixed points on the plot
fixed_points_numeric = [0, 1, 0.382, 2.618]
for fp in fixed_points_numeric:
    if 0 <= fp <= 1.1:  
        plt.scatter(fp, fp, color='green', label=f"Fixed Point: {fp:.3f}")

# Annotate flow directions
plt.arrow(0.2, 0.2, -0.1, 0, head_width=0.05, head_length=0.05, fc='black', ec='black')
plt.arrow(0.8, 0.8, 0.1, 0, head_width=0.05, head_length=0.05, fc='black', ec='black')

# Labels and legend
plt.title("Flow in $p$-Space", fontsize=14)
plt.xlabel("$p$", fontsize=12)
plt.ylabel("$R_b(p)$", fontsize=12)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid(True)
plt.show()


