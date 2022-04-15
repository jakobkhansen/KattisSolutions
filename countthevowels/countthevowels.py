import sys

def countthevowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = input()
    ctr = 0
    for letter in text:
        if letter.lower() in vowels:
            ctr += 1
    return ctr

print(countthevowels())
