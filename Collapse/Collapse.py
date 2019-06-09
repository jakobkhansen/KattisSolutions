import sys

class Island:
    def __init__(self, threshold, alive):
        self._threshold = threshold
        self._alive = alive
        self._current = 0
        self._pairs = {}

    def send_goods(self, island, amount):
        if self._alive:
            island._receive_goods(amount)

    def _receive_goods(self, amount):
        if self._alive:
            self._current += amount

    def get_alive(self):
        return self._alive

    def eval_death(self):
        if self._current < self._threshold:
            self._alive = False
        self._current = 0

    def __repr__(self):
        return "Island(self, {}, {})".format(self._threshold, self._alive)

    def create_pairs(self, pairs):
        self._pairs = pairs

    def get_pairs(self):
        return self._pairs


def create_islands(lines):
    lines = lines[1:]
    islands = []

    # Create islands
    for line in lines:
        words = line.split(" ")

        threshold = int(words[0])
        alive = int(words[1]) != 0
        islands.append(Island(threshold, alive))


    # Create pairs
    for line_index in range(len(lines)):
        pairs = {}
        words = lines[line_index].split(" ")[2:]

        for i in range(0, len(words), 2):
            pairs[islands[int(words[i])-1]] = int(words[i+1])

        islands[line_index].create_pairs(pairs)

    return islands

def simulate_islands(islands):

    # Number of lunar cycles
    for _ in range(50):
        for island in islands:
            for pair_island in island.get_pairs():
                pair_island.send_goods(island, island.get_pairs()[pair_island])

        for island in islands:
            island.eval_death()

    # Evaluate surviving islands
    counter = 0
    for island in islands:
        if island.get_alive():
            counter += 1
    return counter

def main():
    lines = [lines.strip() for lines in sys.stdin]

    islands = create_islands(lines)
    numSurvivors = simulate_islands(islands)
    print(numSurvivors)

main()
