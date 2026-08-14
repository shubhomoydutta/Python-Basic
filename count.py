a = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowels_count = 0
consonants_count = 0
digits_count = 0
special_chars_count = 0
for char in a:
    if char.isdigit():
        digits_count += 1
    elif char.isalpha():
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
    elif not char.isspace():  # Excludes spaces from special characters
        special_chars_count += 1

print(f"Vowels: {vowels_count}")
print(f"Consonants: {consonants_count}")
print(f"Digits: {digits_count}")
print(f"Special Characters: {special_chars_count}")