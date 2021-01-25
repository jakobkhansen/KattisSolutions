def find_divisors(n):
    divisors = []
    maxi = int((n**(0.5)+1))
    print(maxi)
    for i in range(1, maxi+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)
    return sorted(list(set(divisors)))

print(find_divisors(102))
