import sys

def whichbase(lines):
    lines = lines[1:]
    return_string = ""
    for line in lines:
        return_string += line[0] + " "
        decimal = line.split(" ")[1]
        try:
            octal = int(decimal, 8)
        except:
            octal = 0
        try:
            hexa = int(decimal, 16)
        except:
            hexa = 0
        array = [octal, int(decimal), hexa]
        return_string += " ".join([str(x) for x in array]) + "\n"
    return return_string.strip()

def main():
    lines = [line.strip() for line in sys.stdin]
    print(whichbase(lines))
main()
