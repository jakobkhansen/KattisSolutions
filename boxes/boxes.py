class Box:
    def __init__(self, index):
        self.index = index
        self.children = []

    def count(self, used):
        if not used.get(self.index, False):
            used[self.index] = True
            local_count = 1
            for child in self.children:
                local_count += child.count(used)
            return local_count
        return 0

    def __repr__(self):
        children = [x.index for x in self.children]
        return "(index={},children={})".format(self.index, children)


def boxes():
    num_boxes = int(input())
    boxes = {}
    for i in range(num_boxes):
        boxes[i+1] = Box(i+1)

    for i,index in enumerate([int(x) for x in input().split(" ")]):
        if index != 0:
            boxes[index].children.append(boxes.get(i+1))

    num_queries = int(input())
    for i in range(num_queries):
        used = {}
        nums = [int(x) for x in input().split(" ")[1:]]
        curr_boxes = [boxes[x] for x in nums]
        num_boxes = [x.count(used) for x in curr_boxes]
        print(sum(num_boxes))

boxes()

