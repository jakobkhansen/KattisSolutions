import sys

class SegmentTree:
    class Node:
        def __init__(self, rangeStart, rangeEnd, nodeSum=0):
            self.rangeStart = rangeStart
            self.rangeEnd = rangeEnd
            self.sum = nodeSum
            self.left = None
            self.right = None

        def add(self, value):
            self.sum += value

        def __repr__(self):
            if self.left == None:
                leftStart = "None"
                leftEnd = "None"
            else:
                leftStart = self.left.rangeStart
                leftEnd = self.left.rangeEnd

            if self.right == None:
                rightStart = "None"
                rightEnd = "None"
            else:
                rightStart = self.right.rangeStart
                rightEnd = self.right.rangeEnd

            representation = "[ {} {} ], sum = {}, ([ {} {} ], [ {} {} ])".format(
                self.rangeStart,
                self.rangeEnd,
                self.sum,
                leftStart,
                leftEnd,
                rightStart,
                rightEnd
            )
            return representation

    def __init__(self, n):
        self.root = self.constructTree(n)
        self.array = [0]*n

    def constructTree(self, n):
        return self._constructTreeRecursive(0, n-1)

    def _constructTreeRecursive(self, low, high):
        if low == high:
            return self.Node(low, high)

        mid = (low+high)//2
        current = self.Node(low, high)

        current.left = self._constructTreeRecursive(low, mid)
        current.right = self._constructTreeRecursive(mid+1, high)

        return current

    def flipBit(self, index):
        diff = None
        if self.array[index] == 1:
            diff = -1
            self.array[index] = 0
        else:
            diff = 1
            self.array[index] = 1

        self._flipBitRecursive(self.root, diff, index)

    def _flipBitRecursive(self, node, diff, index):
        if node == None or index < node.rangeStart or index > node.rangeEnd:
            return

        node.add(diff)

        self._flipBitRecursive(node.left, diff, index)
        self._flipBitRecursive(node.right, diff, index)

    def getSum(self, start, end):
        return self._getSumRecursive(self.root, start, end)

    def _getSumRecursive(self, current, start, end):
        if (current == None or current.rangeStart > end or current.rangeEnd < start):
            return 0

        if (current.rangeStart >= start and current.rangeEnd <= end):
            return current.sum

        leftSum = self._getSumRecursive(current.left, start, end)
        rightSum = self._getSumRecursive(current.right, start, end)

        return leftSum + rightSum

    def show(self):
        self._show(self.root)
    def _show(self,p):
        if  p==None:
            return
        print(p)
        self._show(p.left)
        self._show(p.right)

def main():
    firstLine = sys.stdin.readline()
    n = int(firstLine.split(" ")[0])

    segmentTree = SegmentTree(n)

    for line in sys.stdin:
        command = line
        command_split = command.split()
        command_type = command_split[0]

        if command_type == "F":
            i = int(command_split[1])
            i = i-1
            segmentTree.flipBit(i)

        else:
            num1 = int(command_split[1])
            num2 = int(command_split[2])
            print(segmentTree.getSum(num1-1, num2-1))
            # segmentTree.show()


def mainOld():
    firstLine = sys.stdin.readline()
    n = int(firstLine.split(" ")[0])

    memory = [0]*n

    for line in sys.stdin:
        command = line
        command_split = command.split()
        command_type = command_split[0]

        if command_type == "F":
            i = int(command_split[1])
            i = i-1
            memory[i] = (memory[i] + 1) % 2

        else:
            num1 = int(command_split[1])
            num2 = int(command_split[2])
            count = 0
            sum
            for i in range(num1-1, num2):
                count += memory[i]
            print(count)

main()
