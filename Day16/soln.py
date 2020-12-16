import re
from math import prod
from functools import reduce

# intervals without classes
def inintervals(target, intervals):
    return target * int(all((not (i[0] <= target <= i[1]) for i in intervals)))

# intervals with classes
def failintervals(row, classes):
    return any(all(not ((iv[0] <= r <= iv[1]) or (iv[2] <= r <= iv[3])) for iv in classes) for r in row)

def main():
    with open('data') as f: data = f.read().split('\n\n')
   
    print("Part One")
    f = re.compile('([0-9]+)-([0-9]+)')
    intervals = reduce(lambda x,y: x + [(int(y[0]), int(y[1]))], f.findall(data[0]), [])

    others = re.findall('[0-9]+', data[2])
    print(reduce(lambda x,y: inintervals(int(y), intervals) + x, others, 0))
    
    print("Part Two")
    g = re.compile('([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)')
    classes = [[int(c) for c in cl] for cl in g.findall(data[0])]

    others_raw = [[int(r) for r in row.split(',')] for row in data[2].strip().split('\n')[1:]]
    clean = filter(lambda r: not failintervals(r, classes), others_raw)

    exclusions = [[i, set()] for i in range(len(classes))]
    for row in clean:
        for i,r in enumerate(row):
            for j,c in enumerate(classes):
                if not ((c[0] <= r <= c[1]) or (c[2] <= r <= c[3])):
                    exclusions[j][1].add(i)
     
    exclusions = sorted(exclusions, key=lambda x: -len(x[1]))
    total = {i for i in range(20)}
    result = [None] * 20
    for i,e in enumerate(exclusions):
        diff = total.difference(e[1])
        m = diff.pop()
        result[e[0]] = m
        for j in range(i, len(exclusions)):
            exclusions[j][1].add(m)

    mytick = [int(x) for x in data[1].split()[2].split(',')]
    mytickarranged = [mytick[i] for i in result]
    print(prod(mytickarranged[:6]))


if __name__=='__main__':
    main()
