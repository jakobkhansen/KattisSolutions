import sys

def guessthedatastructure(lines):
    index = 0

    while index < len(lines):
        numOps = int(lines[index])
        caseLines = lines[index+1:index+numOps+1]
        index += numOps+1

        case([(int(x.split(" ")[0]),int(x.split(" ")[1])) for x in caseLines])


def case(operations):
    # print(operations)
    results = [check_stack(operations), check_queue(operations), check_pqueue(operations)]

    if results.count(True) > 1:
        print("not sure")
    elif results.count(False) == 3:
        print("impossible")
    elif results[0]:
        print("stack")
    elif results[1]:
        print("queue")
    elif results[2]:
        print("priority queue")

def check_stack(operations):
    stack = []
    for op in operations:
        t,v = op

        if t == 1:
            stack.append(v)
        elif t == 2:
            try:
                out = stack.pop()
                if out != v:
                    return False
            except:
                return False
    return True

def check_queue(operations):
    queue = []
    for op in operations:
        t,v = op

        if t == 1:
            queue.append(v)
        if t == 2:
            try:
                out = queue.pop(0)
                if out != v:
                    return False
            except:
                return False
    return True

def check_pqueue(operations):
    pqueue = []

    for op in operations:
        t,v = op

        if t == 1:
            pqueue.append(v)
            pqueue.sort()
        if t == 2:
            try:
                out = pqueue.pop()
                if out != v:
                    return False
            except:
                return False
    return True

def main():
    lines = [line.strip() for line in sys.stdin]
    guessthedatastructure(lines)
main()
