import sys

class File:
    def __init__(self, name) -> None:
        self.name = name

        # Files which depend on this file
        self.dependees = []
        self.inEdges = 0
        self.to_be_compiled = False

    def __repr__(self) -> str:
        return f'File({self.name}, {[x.name for x in self.dependees]}, {self.inEdges}, {self.to_be_compiled})'

def builddeps(lines):
    n = int(lines[0])
    files = {}
    for i in range(1, n+1):
        filename = lines[i].split(':')[0]
        files[filename] = File(filename)

    for i in range(1, n+1):
        filename = lines[i].split(':')[0]
        for dependency in lines[i].split(':')[1].split():
            files[dependency].dependees.append(files[filename])

    start_name = lines[-1].strip()
    topsort(files, start_name)

def topsort(files, start_name):

    for file in files.values():
        for dependee in file.dependees:
            dependee.inEdges += 1

    start_node = files[start_name]
    queue = []

    for file in files.values():
        if file.inEdges == 0:
            queue.append(file)
    start_node.to_be_compiled = True

    # visited = {}
    # visited[start_node] = True

    # print(files)
    while len(queue) != 0:
        current = queue.pop()
        if current.to_be_compiled:
            print(current.name)

        for dependee in current.dependees:
            # print(dependee)
            dependee.inEdges -= 1

            if current.to_be_compiled:
                dependee.to_be_compiled = True

            if dependee.inEdges == 0:
                # visited[dependee] = True
                queue.append(dependee)





def main():
    lines = [line.strip() for line in sys.stdin]
    builddeps(lines)
main()
