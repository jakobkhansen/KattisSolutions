import sys

def toilet(lines):
    chars = lines[0]
    policies = [policy_one, policy_two, policy_three]
    adjustments = [policies[i](chars) for i in range(3)]
    return "\n".join(adjustments)

def policy_one(chars):
    start = chars[0]
    adjustments = 0
    if start == 'D':
        adjustments += 1
    for char in chars[2:]:
        if char == 'D':
            adjustments += 2
    return str(adjustments)

def policy_two(chars):
    start = chars[0]
    adjustments = 0
    if start == 'U':
        adjustments += 1
    for char in chars[2:]:
        if char == 'U':
            adjustments += 2
    return str(adjustments)

def policy_three(chars):
    current = chars[0]
    adjustments = 0

    for char in chars:
        if char != current:
            adjustments += 1
            current = char
    return str(adjustments)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(toilet(lines))
main()
