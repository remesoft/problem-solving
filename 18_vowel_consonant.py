import re

for _ in range(int(input())):

    text = input()
    vowels = re.findall(r'[aeiouAEIOU]', text)
    consonants = re.findall(r'[^aeiouAEIOU\s]', text)

    vowel_string = ''.join(vowels)
    consonant_string = ''.join(consonants)

    print(vowel_string)
    print(consonant_string)