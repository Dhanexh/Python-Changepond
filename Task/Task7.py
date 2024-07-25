#take Example of your name and print the name without vowel

# vowels = ['a','e','i','o','u']
vowels = 'aeiou'
name="dhanesh"
consonants = [i for i in name if i not in vowels]
print(consonants)