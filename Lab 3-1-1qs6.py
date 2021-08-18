# Lab 3-1-1 question 6
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

case_input = input("Please enter a word that starts with a capital\
 letter and with subsequent letters in lower case: ")

case_result = str(case_input == case_input.capitalize()).lower()


print(f"It is {case_result} that {case_input} starts with a capital letter and all\
 subsequent letters are in lower case.")
