
#########################################
# Problem 1

W = 2e-6
h = 2e-6
E = 150e9
L_b = 50e-6
L_d = 120e-6
L_c = 100e-6

I = W * h**3 / 12

k_b = 12 * E * I / (L_b**3)
k_d = 12 * E * I / (L_d**3)
k_c = 12 * E * I / (L_c**3)

k_side = (  ((((1/(2*k_c)) + (2/(k_b + k_d)))**(-1)  + 2*k_c)**(-1))   + (1/(2*k_c)) )**(-1)
k_total = k_side * 2

print(f'k_b: {k_b}, k_d: {k_d}, k_c: {k_c}')
print(f'Total Spring Constant for Problem 1: {k_total}')


###########################################
# Problem 2

k_c = 0.71 #N/m
k_cs = 0.49 #N/m
W = 2e-6
h = 2e-6
E = 150e9
L_c = 150e-6
L_cs = 170e-6

I = W * h**3 / 12

k_c = 12 * E * I / (L_c**3)
k_cs = 12 * E * I / (L_cs**3)

k_total = 2*k_c + ((1/(2*k_c)) + (1/(2*k_c)) + (1/(2*k_c)))**(-1)  +  ((1/k_cs) + (1 / ((2*k_c) + ((1/(2*k_c)) + (1/(2*k_c)) + (1/(2*k_c)))**(-1))))**(-1)


print(f'k_c: {k_c}, k_cs: {k_cs}')
print(f'Total Spring Constant for Problem 2: {k_total}')


