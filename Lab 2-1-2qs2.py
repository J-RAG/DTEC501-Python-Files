# Lab 2-1-2 question 2
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

print("Number conversion utility.")
data_value = input("Please enter a value: ")

integer_val = int(data_value, base=0)
print()
print(f"Decimal: {int(integer_val)}")
print(f"Binary: {bin(integer_val)}")
print(f"Octal: {oct(integer_val)}")
print(f"Hexadecimal: {hex(integer_val)}")