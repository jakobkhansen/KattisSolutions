# Note to self: You should add all movies to queue and do bfs only once, works better
import sys
from queue import Queue

class Movie:
    def __init__(self, id, quality=sys.maxsize):
        self.id = id
        self.quality = quality
        self.edges = []

    def set_quality_if_better(self, new_quality):
        if self.quality == sys.maxsize or self.quality > new_quality:
            self.quality = new_quality
            return True
        return False

    def __repr__(self):
        return "id={}, quality={}, edges={}".format(self.id, self.quality, [x.id for x in self.edges])

    def __lt__(self, other):
        if self.quality == other.quality:
            return self.id < other.id
        return self.quality > other.quality

def horror(lines):
    n,h,l = [int(x) for x in lines[0].split(" ")]
    movies = {int(x):Movie(int(x)) for x in range(n)}
    bad_movies = [movies[int(x)] for x in lines[1].split(" ")]

    for bad_movie in bad_movies:
        bad_movie.set_quality_if_better(0)

    for edge in lines[2:]:
        x,y = [int(x) for x in edge.split(" ")]
        movie1,movie2 = movies[x],movies[y]
        movie1.edges.append(movie2)
        movie2.edges.append(movie1)

    for bad_movie in bad_movies:
        bfs(bad_movie, bad_movies)

    worst_movie = min(movies.values())
    return worst_movie.id
    

def bfs(start, bad_movies):
    visited = {x:True for x in bad_movies}
    queue = Queue()
    queue.put(start)
    while not queue.empty():
        current = queue.get()
        for edge in current.edges:
            if not visited.get(edge, False) and edge.set_quality_if_better(current.quality + 1): 
                queue.put(edge)
                visited[edge] = True




def main():
    lines = [line.strip() for line in sys.stdin]
    print(horror(lines))
main()
