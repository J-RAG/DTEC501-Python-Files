# Lab 3-1-1 question 7
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

case_lower = input("Please enter a word whose letters are all lower case: ")
case_upper = input("Please enter a word whose letters are all upper case: ")

case_result_low = str(case_lower == case_lower.lower()).lower()
case_result_upp = str(case_upper == case_upper.upper()).lower()

print(f"It is {case_result_low} that {case_lower} is in all lower case letters.")
print(f"It is {case_result_upp} that {case_upper} is in all upper case letters.")
