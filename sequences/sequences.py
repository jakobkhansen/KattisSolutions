import sys

MOD = 1000000007
powers = [1]

def sequences(lines):
    bitstring = lines[0]
    q_right = 0
    zeros_right = 0
    inversions = 0


    for bit in reversed(bitstring):
        if bit == '?':
            inversions *= 2
            z = zeros_right * mod(q_right)
            q = 0 if q_right == 0 else q_right*mod(q_right-1)
            inversions = (inversions + z + q) % MOD
            q_right += 1
        elif bit == '0':
            zeros_right += 1
        elif bit == '1':
            z = zeros_right * mod(q_right)
            q = 0 if q_right == 0 else q_right*mod(q_right-1)
            inversions = (inversions + z + q) % MOD

    return inversions

def mod(num):
    while num >= len(powers):
        powers.append((powers[-1]*2) % MOD)

    return powers[num] % MOD
    # return 0 if num == 0 else (2**(num-1)) % MOD

def main():
    lines = [line.strip() for line in sys.stdin]
    print(sequences(lines))
main()
