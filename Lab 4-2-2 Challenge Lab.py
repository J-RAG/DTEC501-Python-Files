# Lab 4-2-2 Challenge Lab 
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

user_name = input("Please enter your first name: ").strip().title()
start_val = float(input(f"Hi {user_name}, please enter the start value: ").strip())
end_val = float(input("Please enter the end value: ").strip())
step_val = float(input("Please enter the step value: ").strip())
dec_place_val = int(input("Please enter the number of decimal places you want to be used: ").strip())

loop_counter = start_val

# check if step is incrementing/decrementing
if step_val > 0:
    # Step is incrementing, loop breaks if :
    # loop_counter is more than and not equal to end_val
    # if equal to end_val it will inclusively print the last value
    while loop_counter < end_val or loop_counter == end_val:
        print(f"{loop_counter:.{dec_place_val}f}")
        loop_counter += step_val
else:
    # Step is decerementing, loop breaks if :
    # loop_counter is less than and not equal to end_val
    # if equal to end_val it will inclusively print the last value
    while loop_counter > end_val or loop_counter == end_val:
        print(f"{loop_counter:.{dec_place_val}f}")
        loop_counter += step_val
