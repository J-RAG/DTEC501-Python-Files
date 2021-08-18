# Lab 8-2-1 question 3
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

MINIMUM_MARK = 0
MAXIMUM_MARK = 20

x = int(input("Enter your assessment mark: "))
if not (x < MINIMUM_MARK or x > MAXIMUM_MARK): 
    print("Your assessment mark is valid.")
else:
    print("Your assessment mark is not valid.")
