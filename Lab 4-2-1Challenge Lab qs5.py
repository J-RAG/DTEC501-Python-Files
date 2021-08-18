# Lab 4-2-1 Challenge Lab question 5
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

user_name = input("Please enter your first name: ").strip().capitalize()
inner_loop_start = int(input(f"Hi {user_name}, please enter the start value for the inner loop: ").strip())
inner_loop_end = int(input("Please enter the end value for the inner loop: ").strip())
outer_loop_start = int(input("Please enter the start value for the outer loop: ").strip()) 
outer_loop_end = int(input("Please enter the end value for the outer loop: ").strip())

# outer loop sequence 
for outer_val in range(outer_loop_start, outer_loop_end + 1):
    # inner loop sequence
    for inner_val in range(inner_loop_start, inner_loop_end + 1):
        # outer loop will not increment until inner loop is finished
        print(f"{outer_val} {inner_val}")
