import math
# Assign values
a = 12
b = 12
# Calculate LCM using GCD
lcm = (a * b) // math.gcd(a, b)
# Print the result
print(f"The LCM of {a} and {b} is: {lcm}")