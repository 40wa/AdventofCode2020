import re
from functools import reduce

def parse(data):
    ret = []
    for line in data:
        tmp = line.split('(')
        foods = tmp[0].strip().split()
        allergens = tmp[1].strip(')').replace(',',' ').split()[1:]

        ret.append((set(allergens), set(foods)))

    return ret

def find_benign(data):
    parsed = parse(data)

    allfoods = reduce(lambda x,y: y.union(x), [p[1] for p in parsed])
    allallergens = reduce(lambda x,y: y.union(x), [p[0] for p in parsed])

    result = dict()
    
    found = True
    while found:
        found = False
        # Do a pass
        for i,p in enumerate(parsed):
            if p and (len(p[0]) == 1):
                if len(p[1]) == 1:
                    # Done, remove it
                    allergen = list(p[0])[0]
                    food = list(p[1])[0]
                    for j,q in enumerate(parsed):
                        if (j != i) and q and q[0].issuperset(p[0]):
                            q[0].difference_update(p[0])
                        if (j != i) and q:
                            q[1].difference_update(p[1])

                    found = True
                    result[allergen] = food
                    parsed[i] = None
                else:
                    # Find and purge
                    for j,q in enumerate(parsed):
                        if (j != i) and q and q[0].issuperset(p[0]):
                            p[1].intersection_update(q[1])
                            found = True
    
    culprits = {v for k,v in result.items()}
    nonculprits = allfoods.difference(culprits)

    ret = reduce(lambda x,y: x + sum((int(f in nonculprits) for f in y[1])), parse(data), 0)
    return (ret, result)
    

def main():
    with open('data') as f: data = f.read().strip().split('\n')
    
    print("Part One")
    res = find_benign(data)
    print(res[0])
    
    print("Part Two")
    print(','.join([p[1] for p in sorted(list(res[1].items()))]))


if __name__=='__main__':
    main()
