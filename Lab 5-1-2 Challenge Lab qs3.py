# Lab 5-1-2 Challenge Lab question 3
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

INVALID_INPUT_MSG = "Integers only please."
PROGRAM_END_MESSAGE = "Bye."
ASTERISK_TO_PRINT = "*"
SPACE_SEPARATOR = " "
EXIT_INPUT = "0"

non_exit_input = True
# Loop Input Sequence
while non_exit_input:
	num_asterisks = input("Please enter the maximum number of asterisks to be displayed on one line: ").strip()
	# Input Validation
	if not num_asterisks.isdigit():
		print(INVALID_INPUT_MSG)
	
	# Input Exit Protocol
	elif num_asterisks == EXIT_INPUT:
		non_exit_input = False
		
	else:
		# Loop print Sequence
		# Loop sequence is reversed
		for amount in range(int(num_asterisks), 0, -1):
			print(f"{SPACE_SEPARATOR * (int(num_asterisks) - amount)}"\
			f"{ASTERISK_TO_PRINT * amount}")
print(PROGRAM_END_MESSAGE)
