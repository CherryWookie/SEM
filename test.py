# Redefining constants and recalculations since the state was reset
# Random Calculation Test for the SEM Homework. Not important anymore and probably not accurate anyway

# Constants
mu = 0.42e-3  # Dynamic viscosity in Pa.s
h = 20e-6     # Height of the microchannel in m

# Segment properties
segments = [
    {"L": 2e-2, "w": 200e-6},  # Segment 1
    {"L": 2e-2, "w": 120e-6},  # Segment 2
    {"L": 1e-2, "w": 40e-6},   # Segment 3
]

# Function to calculate resistance
def calculate_resistance(L, w, h, mu):
    correction_factor = 1 - 0.63 * (h / w)
    R = (12 * mu * L) / (w * h**3 * correction_factor)
    return R

# Calculate resistances for each segment
resistances = [calculate_resistance(seg["L"], seg["w"], h, mu) for seg in segments]

# Total resistance (series connection)
R_total = sum(resistances)

# Pressure difference
delta_P = 15e3  # Pressure difference in Pa

# Flow rate
Q = delta_P / R_total  # Flow rate in m^3/s

# Convert flow rate to uL/min
Q_uL_min = Q * 1e9 * 60  # m^3/s to uL/min

resistances, R_total, Q_uL_min

print(resistances, R_total,Q_uL_min)