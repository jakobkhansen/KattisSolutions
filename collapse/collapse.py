import sys

class Island:


    def __init__(self, num_goods_to_live, island_id):
        self.deliveries = {}
        self.received = {}
        self.num_to_live = num_goods_to_live
        self.id = island_id

    def add_receive(self, num_received, island_received_from):
        self.received[island_received_from] = num_received

    def add_delivery(self, num_delivered, island_delivered_to):
        self.deliveries[island_delivered_to] = num_delivered

    def getTotalReceived(self):
        return sum(filter(None, [self.received[x] for x in self.received.keys()]))

    def kill_island_deliveries(self, islands):
        killed_deliveries = []
        for delivery in self.deliveries.keys():
            if islands[delivery-1] != None:
                islands[delivery-1].received[self.id] = None
                killed_deliveries.append(delivery-1)

        islands[self.id-1] = None
        return killed_deliveries

    def determine_if_dead(self):
        return self.getTotalReceived() < self.num_to_live

    def __repr__(self):
        return "{} - {}".format(self.id, self.num_to_live)


def collapse(lines):
    n = int(lines[0].split()[0])
    islands = build_islands(lines[1:])


    return n-1 - determine_killed_islands(islands)


def build_islands(descriptions):

    # Build islands
    islands = []
    for i, description in enumerate(descriptions):
        nums = [int(x) for x in description.split()]
        islands.append(Island(nums[0], i+1))


    # Build trade routes
    for i, description in enumerate(descriptions):
        island = islands[i]
        nums = [int(x) for x in description.split()]

        delivery_pairs = [nums[i:i+2] for i in range(2, len(nums), 2)]

        for sender, num_received in delivery_pairs:
            island.received[sender] = num_received
            islands[sender-1].deliveries[island.id] = num_received

    return islands

def determine_killed_islands(islands):
    # Kill Incunababula
    killed = islands[0].kill_island_deliveries(islands)

    counter = 0
    while len(killed) > 0:
        new_killed = []

        for killed_island in killed:
            if islands[killed_island] != None and islands[killed_island].determine_if_dead():
                new_killed += islands[killed_island].kill_island_deliveries(islands)
                counter += 1
        killed = new_killed
    return counter

def print_islands(islands):
    print("ISLANDS:")
    print(islands)
    print("Deliveries: ")
    print(list(map(lambda x: "{}: {}".format(x.id, x.deliveries), islands)))

    print("Received: ")
    print(list(map(lambda x: "{}: {}".format(x.id, x.received), islands)))
    print()
def main():
    lines = [line.strip() for line in sys.stdin]
    print(collapse(lines))
main()
