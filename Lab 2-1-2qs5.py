# Lab 2-1-2 question 5
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

print("Hexadecimal addition calculator.")
first_hexa = input("Enter the first hexadecimal number: ")
second_hexa = input("Enter the second hexadecimal number: ")
print(f"{hex(int(first_hexa, base=16))} + {hex(int(second_hexa, base=16))} = {hex(int(first_hexa, base=16) + int(second_hexa, base=16))}")
