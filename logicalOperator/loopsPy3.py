# lists = ["geeks", "for", "geeks"]
# for index in range(len(lists)):
#     print(lists[index])


# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)