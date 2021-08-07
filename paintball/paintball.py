import sys

class Player:
    def __init__(self, index):
        self.index = index
        self.neighbours = []
        self.visited = False
        self.target = None

    def __repr__(self):
        return f"Player({self.index}, {[x.index for x in self.neighbours]})"

def paintball(lines):
    n,m = [int(x) for x in lines[0].split()]
    players = [Player(x) for x in range(1, n+1)]
    for line in lines[1:]:
        p1, p2 = [int(x) for x in line.split()]
        players[p1-1].neighbours.append(players[p2-1])
        players[p2-1].neighbours.append(players[p1-1])

    result = dfs(players[0], players, 1)
    if not result:
        return "Impossible"
    shot_list = []
    for player in players:
        shot_list.append(str(player.target.index))
    return "\n".join(shot_list)

def dfs(player, players, depth):
    player.visited = True
    if depth == len(players):
        player.target = players[0]
        return True
    for neighbour in player.neighbours:
        found = False
        if not neighbour.visited:
            found = dfs(neighbour, players, depth+1)
        if found:
            player.target = neighbour
            return True
    player.visited = False
    return False



def main():
    lines = [line.strip() for line in sys.stdin]
    print(paintball(lines))
main()
