# Lab 8-2-1 question 1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz


first_name = input("Enter your first name: ")
first_name = first_name.title()
# LogicalError: lstrip only removes leading spaces
# Test data with Trailing spaces will not be removed
# strip() will fix this
first_name = first_name.strip()
print(f"[{first_name}]")
