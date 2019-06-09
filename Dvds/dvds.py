import sys

def sortDvds(linjer):
    numInput = int(linjer[0])
    linjer = linjer[1:]
    orderString = ""
    for i in range(numInput):
        order = linjer[1]

        orderString += str(numSort(order)) + "\n"

        linjer = linjer[2:]

    return orderString

def numSort(order):
    orderList = [int(dvd) for dvd in order.split(" ")]
    numOps = 0


    while orderList != []:
        orderList = rmSorted(orderList)

        for dvd in orderList:
            if dvd == (orderList[len(orderList)-1] + 1):
                orderList.remove(dvd)
                orderList.append(dvd)
                numOps += 1

    return numOps

def rmSorted(liste):
    listeSorted = liste.copy()
    listeSorted.sort()
    for num in reversed(range(len(liste))):
        if liste[num:] == listeSorted[num:]:
            return liste[num+1:]

    return liste

def main():
    linjer = [linje.strip() for linje in sys.stdin]

    ans = sortDvds(linjer).rstrip()
    print(ans)

    
#    testArray = [1,2,3,2,5]
#    testSorted = testArray.copy()
#    testSorted.sort()
#    print(rmSorted(testArray, testSorted))

main()
