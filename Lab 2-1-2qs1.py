# Lab 2-1-2 question 1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

print("Decimal to binary, octal and hexadecimal conversion utility.")
decimal_val = int(input("Please enter a decimal value: "))
binary_val = bin(decimal_val)
octal_val = oct(decimal_val)
hexidecmal_val = hex(decimal_val)

#output
print()
print(f"Binary: {binary_val}")
print(f"Octal: {octal_val}")
print(f"Hexadecimal: {hexidecmal_val}")