# Lab 3-1-1 question 5
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

LOWERCASE_S = "s"

user_phrase = input(f"Please enter a word that ends with {LOWERCASE_S}: ").strip()
is_uppercasez = str(user_phrase.lower().endswith(LOWERCASE_S)).lower()

print(f"It is {is_uppercasez} that {user_phrase} ends with {LOWERCASE_S}.")

