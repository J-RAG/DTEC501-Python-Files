# Lab 2-1-2 question 4
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

print("Octal addition calculator.")
first_octal = input("Enter the first octal number: ")
second_octal = input("Enter the second octal number: ")
print(f"{oct(int(first_octal, base=8))} + {oct(int(second_octal, base=8))} = {oct(int(first_octal, base=8) + int(second_octal, base=8))}")
