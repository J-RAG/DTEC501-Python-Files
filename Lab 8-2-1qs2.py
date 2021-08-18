# Lab 8-2-1 question 2
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

MINIMUM_MARK = 0
MAXIMUM_MARK = 30

# ValueError Line 8: Occur if input is not a pure number and leading/trailing spaces were not removed
x = int(input("Enter your assessment mark: "))
# NameError line 11: constant/variable names are case sensitive, minumum_mark is not defined.
# Unused Constant (line 5 and line 11): MAXIMUM_MARK is not used in this Code
# LogicalError line 11: Conditional only validates the cases where test data is either 0 or 30.
if x >= MINIMUM_MARK and x <= MAXIMUM_MARK:
    print("Your assessment mark is valid.")
else:
    print("Your assessment mark is not valid.")
