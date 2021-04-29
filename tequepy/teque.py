import sys


class Deque:
    def __init__(self):
        self.arr = [0]*(10**6)
        self.length = 0
        self.l = int(len(self.arr)/2)
        self.r = int(len(self.arr)/2)

    def push_first(self, value):
        if self.l == self.r:
            self.r += 1
        self.arr[self.l] = value
        self.l -= 1
        self.length += 1

    def push_last(self, value):
        if self.l == self.r:
            self.l -= 1
        self.arr[self.r] = value
        self.r += 1
        self.length += 1

    def get(self, index):
        i = self.l + index + 1
        return self.arr[i]

    def remove_last(self):
        value = self.arr[self.r-1]
        self.r -= 1
        self.length -= 1
        return value

    def remove_first(self):
        value = self.arr[self.l+1]
        self.l += 1
        self.length -= 1
        return value

    def __repr__(self) -> str:
        return "{}".format(str(self.arr[self.l+1:self.r]))

left = Deque()
right = Deque()

def teque():
    commands = {
        "push_back":pushBack,
        "push_front":pushFront,
        "push_middle":pushMiddle,
        "get":get
    }


    sys.stdin.readline()

    for command in sys.stdin:
        commandSplit = command.split(" ")
        commandFunction = commands[commandSplit[0]]

        commandFunction(int(commandSplit[1]))
        # print(left, right)



def pushBack(value):
    right.push_last(value)
    rearrange()


def pushFront(value):
    left.push_first(value)
    rearrange()

def pushMiddle(value):
    if left.length < right.length:
        left.push_last(right.remove_first())
        right.push_first(value)
    else:
        left.push_last(value)
    rearrange()

def get(index):
    if index >= left.length:
        print(right.get(index-left.length))
    else:
        print(left.get(index))
    
def rearrange():
    if (left.length  - right.length) >= 2:
        right.push_first(left.remove_last())
    elif (right.length - left.length) >= 2:
        left.push_last(right.remove_first())


def main():
    teque()
main()
