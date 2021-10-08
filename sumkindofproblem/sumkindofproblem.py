import sys

sys.stdin.readline()

for i, line in enumerate(sys.stdin):
    k, n = [int(x) for x in line.split()]
    print(f'{int(i+1)} {int((n*(n+1))/2)} {int(n**2)} {int(n*(n+1))}')
