import sys

def betting():
    x = int(input())
    a = 100/x
    b = 100/(100-x)

    return "\n".join([str(x) for x in [a,b]])

print(betting())
