word = str(input("Enter a word: "))
new_Word = ""
new_Word = word.replace(" ", "")

vowel_counter = 0
consonant_counter = 0

for letter in word.lower():
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowel_counter = vowel_counter+1
    else:
        consonant_counter = consonant_counter+1

print("Vowels: ", + str(vowel_counter))
print("Consonant: ", + str(consonant_counter))


