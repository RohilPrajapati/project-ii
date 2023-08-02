import sympy as sp


# # Define the variables and the equation
x, y, z = sp.symbols('x y z')
equation = y**3-y-2-x
# y**3-y-2-x

# print(result)

# Rearrange the equation to solve for 'z'
reversed_equation = sp.solve(equation, y)

# Print the reversed equation
print("Reversed equation:", reversed_equation)
# test_equ = [-(-1/2 - sqrt(3)*I/2)*(-27*x/2 + sqrt((-27*x - 54)**2 - 108)/2 - 27)**(1/3)/3 - 1/((-1/2 - sqrt(3)*I/2)*(-27*x/2 + sqrt((-27*x - 54)**2 - 108)/2 - 27)**(1/3)), -(-1/2 + sqrt(3)*I/2)*(-27*x/2 + sqrt((-27*x - 54)**2 - 108)/2 - 27)**(1/3)/3 - 1/((-1/2 + sqrt(3)*I/2)*(-27*x/2 + sqrt((-27*x - 54)**2 - 108)/2 - 27)**(1/3)), -(-27*x/2 + sqrt((-27*x - 54)**2 - 108)/2 - 27)**(1/3)/3 - 1/(-27*x/2 + sqrt((-27*x - 54)**2 - 108)/2 - 27)**(1/3)]