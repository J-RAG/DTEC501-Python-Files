# Lab 2-1-1 question 7
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

MIDNIGHT = 24 #Rolls clock back to 0:00 if hours of day reaches or passes 24
HOUR_CONVERT = 60 #Used to append number of hours and convert minutes to appropiate format

print("Meeting time calculator.")
start_hours = int(input("Please enter the start time (hours): "))
start_minutes = int(input("Please enter the start time (minutes): "))
duration_minutes = int(input("Please enter the duration (minutes): ")) 

#arithmetic assignments
total_minutes = start_minutes + duration_minutes 
end_hours = (start_hours + (total_minutes // HOUR_CONVERT)) % MIDNIGHT  
end_minutes = total_minutes % HOUR_CONVERT

#output
print()
print(f"The current time is {start_hours:0>2d}:{start_minutes:0>2d}")
print(f"The meeting will end at {end_hours:0>2d}:{end_minutes:0>2d}")