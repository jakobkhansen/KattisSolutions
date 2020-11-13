import sys
from queue import Queue

class File:
    def __init__(self, name):
        self.name = name
        self.dependencies = []
        self.visited = False
        self.previous = None

    def add_dep(self, dep):
        if self == dep:
            return self
        self.dependencies.append(dep)

    def __str__(self):
        return "{}: {}".format(self.name, str([x.name for x in self.dependencies]))

    def __repr__(self):
        return "{}: {}".format(self.name, str([x.name for x in self.dependencies]))

def importspaghetti(lines):

    names = lines[1].split(" ")

    files = {}


    for name in names:
        files[name] = File(name)

    index = 2

    while index < len(lines):
        file_name = lines[index].split(" ")[0]
        file = files[file_name]

        numLines = int(lines[index].split(" ")[1])

        index +=1
        for i in range(numLines):
            imports = lines[index].split(" ")[1:]

            for imp in imports:
                impFileName = imp.split(",")[0]
                result = file.add_dep(files[impFileName])
                if result != None:
                    return result.name
            index += 1

    shortest_cycle = find_shortest_cycle(files)

    print(shortest_cycle)

def reset_visited(files):
    for file in files.values():
        file.visited = False
        file.previous = None


shortest_cycle_found = None
def find_shortest_cycle(files):
    # Check BFS from this file
    for file in files.values():

        find_shortest_cycle_for_file(file, [], 0)

        reset_visited(files)

    print(shortest_cycle_found)
    return shortest_cycle_found


def find_shortest_cycle_for_file(current, cycle, edge_count):
    global shortest_cycle_found
    current.visited = True

    for dependency in current.dependencies:
        if dependency.visited and shortest_cycle_found is not None and edge_count < len(shortest_cycle_found):
            print("Found cycle")
            shortest_cycle_found = cycle
            cycle.append(current)
            return True
        else:
            if find_shortest_cycle_for_file(dependency, cycle, edge_count + 1):
                cycle.append(current)
                return True





def main():
    lines = [line.strip() for line in sys.stdin]
    print(importspaghetti(lines))
main()
