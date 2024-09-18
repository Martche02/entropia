from sympy import symbols, integrate, sqrt, log
from sympy.abc import alpha

# Define the symbols
A, B, C = symbols('A B C')

# Define the integrand
integrand = 1/sqrt(B+C)*log( ( (A+B)*alpha**2 -2*B*alpha +2*B+3*C +2*sqrt(B+C)*sqrt((A+B)*alpha**2-2*(B+2*C)*alpha+B+C) ) /(alpha**2-2*C*alpha+C+2*sqrt(B+C)*sqrt(alpha**2-2*alpha+C)))

# Compute the integral
integral = integrate(integrand, (alpha, 0, 1))

# Print the result
print(integral)