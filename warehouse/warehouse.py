import sys

def warehouse(lines):
    numCases = int(lines[0].split(" ")[0])
    retString = []
    lines = lines[1:]

    for i in range(numCases):
        waresNum = int(lines[0].split(" ")[0]) 
        retString.append(sortWares(lines[1:waresNum+1]))
        lines = lines[waresNum+1:]





    return "\n".join(retString)
            
def sortWares(wares):
    waresList = {}

    for ware in wares:
        ware_name = ware.split(" ")[0]
        ware_amount = int(ware.split(" ")[1])
        waresList[ware_name] = waresList.get(ware_name, 0) + ware_amount

    uniques = len(waresList)

    ware_sorted = [(waresList[k], k) for k in sorted(waresList, key=waresList.get, reverse=True)]
    name_sorted = sorted(["{} {}".format(ware, name) for ware,name in ware_sorted])
    string = [" ".join(reversed(x.split(" "))) for x in name_sorted]
    return str(uniques) + "\n" + "\n".join(string)




def main():
    lines = [line.strip() for line in sys.stdin]
    print(warehouse(lines))
main()
