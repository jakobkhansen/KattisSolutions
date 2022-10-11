import sys

def flowlayout():
    m = int(input())
    while m != 0:
        recs = []
        for rec in sys.stdin:
            w,h = [int(x) for x in rec.split()]
            if w == -1 and h == -1:
                break
            recs.append((w,h))

        max_w = 0
        max_h = 0

        i = 0
        while i < len(recs):
            width_left = m
            curr_w = 0
            best_h = 0
            while i < len(recs) and width_left >= recs[i][0]:
                w,h = recs[i]
                curr_w += w
                best_h = max(best_h, h)
                width_left -= w
                i += 1

            max_w = max(max_w, curr_w)
            max_h += best_h

        print(f"{max_w} x {max_h}")
        m = int(input())

            


flowlayout()
