import sys

def toilet(lines):
    chars = lines[0]
    policies = [policy_one, policy_two, policy_three]
    adjustments = [policies[i](chars) for i in range(3)]
    return "\n".join(adjustments)

def policy_one(chars):
    adjustments = 0
    current = chars[0]
    preferred = 'U'
    for char in chars[1:]:
        if current != char:
            adjustments += 1
            current = char

        if current != preferred:
            adjustments += 1
            current = preferred 

    return str(adjustments)

def policy_two(chars):
    adjustments = 0
    current = chars[0]
    preferred = 'D'
    for char in chars[1:]:
        if current != char:
            adjustments += 1
            current = char

        if current != preferred:
            adjustments += 1
            current = preferred 

    return str(adjustments)

def policy_three(chars):
    current = chars[0]
    adjustments = 0

    for char in chars[1:]:
        if char != current:
            adjustments += 1
            current = char
    return str(adjustments)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(toilet(lines))
main()
