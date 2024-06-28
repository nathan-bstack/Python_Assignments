def contains_vowel(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for char in s:
        if char in vowels:
            return True
    return False
string = "Hello World"
if contains_vowel(string):
    print("The string contains at least one vowel.")
else:
    print("The string does not contain any vowels.")