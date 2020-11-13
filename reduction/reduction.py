import sys

def reduction(lines):
    retStr = []
    numCases = int(lines[0])

    index = 1
    for case in range(numCases):
        N,M,L = [int(x) for x in lines[index].split(" ")]
        index += 1
        min_prices = []
        for l in range(L):
            name = lines[index].split(":")[0]
            one_price = int(lines[index].split(":")[1].split(",")[0])
            half_price = int(lines[index].split(":")[1].split(",")[1])
            agency = (name, one_price, half_price)

            min_prices.append(find_min_price(agency, N, M))

            index += 1

        min_prices.sort(key=lambda x: x[0])
        min_prices.sort(key=lambda x: x[1])
        retStr.append("Case {}\n".format(case+1) + "\n".join(["{} {}".format(x,y) for x,y in min_prices]))

    return "\n".join(retStr)




def find_min_price(agency, N, M):
    cheapestPrice = 0
    remainingWork = N

    while remainingWork > M:
        remainingAfterOne = remainingWork - 1
        remainingAfterHalf = remainingWork // 2

        if remainingAfterHalf < M:
            remainingWork = remainingAfterOne
            cheapestPrice += agency[1]

        else:
            countOnesForHalveOrComplete = min(round(remainingWork / 2), remainingWork - M)
            priceOnes = countOnesForHalveOrComplete*agency[1]
            if (priceOnes < agency[2]):
                remainingWork -= countOnesForHalveOrComplete
                cheapestPrice += priceOnes
            else:
                remainingWork = remainingWork // 2
                cheapestPrice += agency[2]

    return (agency[0], cheapestPrice)









def main():
    lines = [line.strip() for line in sys.stdin]

    if int(lines[0]) != 0:
        print(reduction(lines))
main()
