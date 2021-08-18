# Lab 7-1-1 question 3
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

SPACE_SEPARATOR = "Gap"

MORSE_LANGUAGE = {
    "A" : ".-", 
    "B" : "-...", 
    "C" : "-.-.", 
    "D" : "-..", 
    "E" : ".", 
    "F" : "..-.", 
    "G" : "--.", 
    "H" : "....", 
    "I" : "..", 
    "J" : ".---", 
    "K" : "-.-", 
    "L" : ".-..", 
    "M" : "--", 
    "N" : "-.", 
    "O" : "---", 
    "P" : ".--.", 
    "Q" : "--.-", 
    "R" : ".-.", 
    "S" : "...", 
    "T" : "-", 
    "U" : "..-", 
    "V" : "...-", 
    "W" : ".--", 
    "X" : "-..-", 
    "Y" : "-.--", 
    "Z" : "--..", 
    "0" : "-----", 
    "1" : ".----", 
    "2" : "..---", 
    "3" : "...--", 
    "4" : "....-", 
    "5" : ".....", 
    "6" : "-....", 
    "7" : "--...", 
    "8" : "---..", 
    "9" : "----.", 
    "." : ".-.-.-", 
    "," : "--..--"
    }

sentence = input("Please enter the phrase to send: ").strip()
curr_pos = 0 # initialize loop
while curr_pos < len(sentence):
    # Check if character is in Morse Dictionary
    if sentence[curr_pos].upper() in MORSE_LANGUAGE:
        print(f"{sentence[curr_pos]} in morse is {MORSE_LANGUAGE[sentence[curr_pos].upper()]}")

    # Charcater not in Morse Dictionary        
    elif sentence[curr_pos] != " ": # Skip if the current character is a space
        print(f"{sentence[curr_pos]} is not available in morse.")

    # Print "Gap" only if the character before was not a space          
    elif sentence[curr_pos - 1] != " ":
        print(SPACE_SEPARATOR)
    curr_pos += 1


