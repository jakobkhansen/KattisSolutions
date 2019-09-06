import sys
import math

def cursethedarkness(lines):
    num_cases = int(lines[0][0])
    lines = lines[1:]

    string_array = []
    for i in range(num_cases):
        book = [float(x) for x in lines[0].split(" ")]
        num_candles = int(lines[1])
        candles = []
        for j in range(num_candles):
            candles.append([float(x) for x in lines[2+j].split(" ")])

        candle_found = False
        for candle in candles:
            distance = math.sqrt( ((book[0]-candle[0])**2)+((book[1]-candle[1])**2) )
            if distance <= 8:
                candle_found = True
        if candle_found:
            string_array.append("light a candle")
        else:
            string_array.append("curse the darkness")

        lines = lines[2+num_candles:]

    return "\n".join(string_array)

def main():
    lines = [line.strip() for line in sys.stdin]
    print(cursethedarkness(lines))
main()
