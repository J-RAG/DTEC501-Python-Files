# Lab 2-2-1 question 6
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

user_phrase = input("Please enter the phrase to change: ")

#clear spaces#
user_phrase = user_phrase.replace(" ", "")


#replace phase#

#'s' to '5'
user_phrase = user_phrase.replace("s", "5")

#'e' to '3'
user_phrase = user_phrase.replace("e", "3")

#'i' to '1'	(one)
user_phrase = user_phrase.replace("i", "1")

#'o' to '0' (zero)
user_phrase = user_phrase.replace("o", "0")

#'a' to '@'
user_phrase = user_phrase.replace("a", "@")

#Output#
print(f"The modified phrase is: {user_phrase}")