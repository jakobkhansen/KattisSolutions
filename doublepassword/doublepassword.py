import sys

def doublepassword():
    pass1 = input()
    pass2 = input()

    possible = 1

    for i in range(4):
        if pass1[i] != pass2[i]:
            possible *= 2
    return possible

print(doublepassword())
