# Lab 5-1-2 Challenge Lab question 1
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz
APLHA_INPUT_MSG = "Integers only please."
PROGRAM_END_MESSAGE = "Bye."
ASTRISKS_TO_PRINT = "*"
EXIT_INPUT = "0"

non_exit_input = True
# Loop Input Sequence
while non_exit_input:
	num_asterisks = input("Please enter the maximum number of asterisks to be displayed on one line: ").strip()
	# Input Validation
	if not num_asterisks.isdigit():
		print(APLHA_INPUT_MSG)
	
	# Input Exit Protocol
	elif num_asterisks == EXIT_INPUT:
		non_exit_input = False
		
	else:
		# Loop print Sequence
		for amount in range(1, int(num_asterisks) + 1):
			print(f"{ASTRISKS_TO_PRINT * amount}")
print(PROGRAM_END_MESSAGE)