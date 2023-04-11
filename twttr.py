vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
word = input("Enter some text: ")
for vowel in vowels:
    word = word.replace(vowel, "")
print("New text: ", word)