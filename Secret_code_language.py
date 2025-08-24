# Author: Sahil
# I am going to create a program capable to perform converting an English word into a code word and also
# capable to decode the coded word based on the user input
# Rules:
#   - If the length of the entered string is less or equal to 3 then remove the first letter and append it to
#     the end 
#   - Else print the given word in the reverse order
# You have to ask the user to encode or decode the input

import random
import string

def encode(word):
    if len(word) >= 3:
        # Move first letter to the end
        word = word[1:] + word[0]
        # Add random 3 letters at the start and at the end
        random_start = ''.join(random.choices(string.ascii_lowercase, k=3))
        random_end = ''.join(random.choices(string.ascii_lowercase, k=3))
        word = random_start + word + random_end
        return word
    else:
        # Simply reverse the string if word is short
        return word[::-1]

def decode(encoded):
    if len(encoded) > 6:
        # Remove the starting and ending extra letters
        core = encoded[3:-3]
        # Move the end letter back to where it was
        original_word = core[-1] + core[:-1]
        return original_word
    else:
        return encoded[::-1]

# Main Program
select = input("Do you want to encode or decode (E or D)? ").strip().upper()
if select == "E":
    word = input("Enter the word you want to encode: ")
    print(f"The encoded word is :: {encode(word)}")
elif select == "D":
    Dec = input("Enter the word for decoding: ")
    print(f"The original word after decoding is :: {decode(Dec)}")
else:
    print("Wrong input! Please ensure that you entered E or D.")
