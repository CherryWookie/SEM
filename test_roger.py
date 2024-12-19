import math
import pandas as pd

# Constants
c = 3e8  # Speed of light (m/s)
d = 1.28e-3  # Substrate height (m)
w = 1.2e-3  # Microstrip width (m)
epsilon_r = 10.2  # Dielectric constant
tan_delta = 0.0022  # Loss tangent
sigma = 5.8e7  # Conductivity of copper (S/m)
mu_0 = 4 * math.pi * 1e-7  # Permeability of free space (H/m)

# Resonance frequencies (Hz)
frequencies = [485.1e6, 971.9e6, 1455.5e6]

# Effective permittivity (ε_eff) calculation
d_over_w = d / w
epsilon_eff = (epsilon_r + 1) / 2 + (epsilon_r - 1) / 2 * (1 / math.sqrt(1 + 12 * d_over_w))

# Helper function for characteristic impedance (Z_0)
def characteristic_impedance(epsilon_eff, w, d):
    if w / d <= 1:
        return 60 / math.sqrt(epsilon_eff) * math.log(8 * d / w + w / (4 * d))
    else:
        return 120 * math.pi / (math.sqrt(epsilon_eff) * (w / d + 1.393 + 0.667 * math.log(w / d + 1.444)))

# Initialize results
results = []

for f in frequencies:
    # Calculate k_0 (free-space wavenumber)
    k_0 = 2 * math.pi * f / c
    
    # Calculate α_d (dielectric loss attenuation)
    alpha_d = (k_0 * epsilon_r * (epsilon_eff - 1) * tan_delta) / (2 * math.sqrt(epsilon_eff) * (epsilon_r - 1))
    
    # Calculate R_s (surface resistivity)
    omega = 2 * math.pi * f
    R_s = math.sqrt(omega * mu_0 / (2 * sigma))
    
    # Calculate Z_0 (characteristic impedance)
    Z_0 = characteristic_impedance(epsilon_eff, w, d)
    
    # Calculate α_c (conductor loss attenuation)
    alpha_c = R_s / (Z_0 * w)
    
    # Total attenuation (α)
    alpha_total = alpha_d + alpha_c  # Nepers per meter
    
    # Convert attenuation to dB/m
    alpha_dB_per_m = alpha_total * 8.686  # 1 Np/m = 8.686 dB/m
    
    # Store results
    results.append({
        'frequency': f,
        'k_0': k_0,
        'alpha_d': alpha_d,
        'alpha_c': alpha_c,
        'alpha_total': alpha_total,
        'alpha_dB_per_m': alpha_dB_per_m
    })

# Display results in detail
print(epsilon_eff, results)

# Extracting reported results from the first report (from earlier processing)

# Let's assume these are stored in a table format and convert them into comparable lists.

# Results inferred from earlier processing:

reported_results = [

    {'frequency': 485.1e6, 'alpha_dB_per_m': 0.929},  # Approx. values for comparison

    {'frequency': 971.9e6, 'alpha_dB_per_m': 1.468},

    {'frequency': 1455.5e6, 'alpha_dB_per_m': 1.807}    

]



# Creating DataFrame for comparison

corrected_df = pd.DataFrame(results)

reported_df = pd.DataFrame(reported_results)



# Renaming columns for clarity

corrected_df.rename(columns={'alpha_dB_per_m': 'Calculated (dB/m)'}, inplace=True)

reported_df.rename(columns={'alpha_dB_per_m': 'Reported (dB/m)'}, inplace=True)



# Merging the two DataFrames on frequency for comparison

comparison_df = pd.merge(corrected_df[['frequency', 'Calculated (dB/m)']], 

                         reported_df, 

                         on='frequency')



# Adding a percentage difference column for scientific comparison

comparison_df['Difference (%)'] = ((comparison_df['Calculated (dB/m)'] - comparison_df['Reported (dB/m)']) / 

                                    comparison_df['Reported (dB/m)']) * 100



print(comparison_df)
