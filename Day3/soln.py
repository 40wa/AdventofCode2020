from functools import reduce

def slopecount(terrain, rgrad, dgrad):
    treectr = 0
    xpos = 0
    terrain = terrain[::dgrad]
    for t in terrain:
        treectr += t[xpos]
        xpos = (xpos + rgrad) % len(terrain[0])
    return treectr

def main():
    # Get input
    data = open('data').read().split()

    # Process data into int array
    procfield = lambda c: 1 if (c == '#') else 0
    terrain = [[procfield(c) for c in d] for d in data]

    # Part One
    print("Part One:")
    ylim = len(terrain)
    xlim = len(terrain[0])
    #print(ylim, xlim)

    treectr = 0
    xpos = 0
    for t in terrain:
        treectr += t[xpos]
        xpos = (xpos + 3) % xlim

    print(treectr)

    # Part Two
    print("Part Two:")
    # We have generalised the slope counter
    grads = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    calcd = [slopecount(terrain, *g) for g in grads]
    res = reduce(lambda x,y: x*y, calcd, 1)
    print(res)

if __name__=="__main__":
    main()
