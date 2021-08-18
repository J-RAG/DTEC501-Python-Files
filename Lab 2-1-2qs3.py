# Lab 2-1-3 
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

print("Multi-base addition calculator.")
first_val = input("Enter the first number: ")
firstbase_val = int(input("Enter the base of the first number: "))
second_val = input("Enter the second number: ")
secondbase_val = int(input("Enter the base of the second number: "))

#Arithmetic Assignment
final_sum = int(first_val, base=firstbase_val) + int(second_val, base=secondbase_val)

#output
print()
print(f"{first_val} base {firstbase_val} + {second_val} base {secondbase_val} = {bin(final_sum)}")
print(f"{first_val} base {firstbase_val} + {second_val} base {secondbase_val} = {oct(final_sum)}")
print(f"{first_val} base {firstbase_val} + {second_val} base {secondbase_val} = {final_sum} base 10.")
print(f"{first_val} base {firstbase_val} + {second_val} base {secondbase_val} = {hex(final_sum)}")
