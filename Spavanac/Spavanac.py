import sys

def Spavanac(linjer):
    time = int(linjer[0].split(" ")[0])
    minutt = int(linjer[0].split(" ")[1]) 


    if minutt - 45 < 0:
        minutt = minutt + 15
        time = time - 1
    else:
        minutt = minutt - 45

    if time < 0:
        time = time + 24
    
    return str(time) + " " + str(minutt)




def main():
    linjer = [linje for linje in sys.stdin]

    print(Spavanac(linjer))
main()
