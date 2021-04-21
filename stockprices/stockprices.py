import sys
from queue import PriorityQueue

def stockprices(lines):
    cases = int(lines[0])
    index = 1
    for i in range(cases):
        num_orders = int(lines[index])
        # print(lines[index+1:index+num_orders+1])
        buy = []
        sell = []
        curr_stock = -1

        for action in lines[index+1:index+num_orders+1]:
            action = action.split(" ")
            num_shares = int(action[1])
            price = int(action[-1])

            pqueue = buy if action[0] == "buy" else sell
            pqueue.append([num_shares, price])

            pqueue.sort(key=lambda x: x[1])
            # print(buy)
            # print(sell)
            while len(buy) > 0 and len(sell) > 0 and buy[-1][1] >= sell[0][1]:
                available_to_sell = sell[0][0]
                want_to_buy = buy[-1][0] if available_to_sell > buy[-1][0] else available_to_sell
                buy[-1][0] -= want_to_buy
                sell[0][0] -= want_to_buy

                curr_stock = sell[0][1]
                if buy[-1][0] <= 0:
                    buy.pop()
                if sell[0][0] <= 0:
                    sell.pop(0)
            curr_stock_out = "-" if curr_stock == -1 else str(curr_stock)
            curr_ask_out = "-" if len(sell) == 0 else str(sell[0][1])
            curr_bid_out = "-" if len(buy) == 0 else str(buy[-1][1])

            print("{} {} {}".format(curr_ask_out, curr_bid_out, curr_stock_out))







        index += num_orders + 1


def main():
    lines = [line.strip() for line in sys.stdin]
    stockprices(lines)
main()
