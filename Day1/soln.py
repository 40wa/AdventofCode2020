"""
    AOC Day 1
"""

def twosum(sumval, data):
    complements = {(sumval - d) for d in data}
    for d in data:
        if d in complements:
            return d, sumval - d
    return None


# This is main
def main():
    """
        This is my main docstring. How useless!
    """
    # Load contents into list
    data = []
    with open('input') as ipt:
        for line in ipt:
            data.append(int(line))

    # Get twosum
    a, b = twosum(2020, data)
    print(a, b)
    if a in data:
        print("A present")
    if b in data:
        print("B present")
    print(a * b)
    
    # Get threesum
    valid = None
    data = sorted(data)
    for idx, d in enumerate(data):
        compl = 2020 - d
        
        ts = twosum(compl, data)
        if ts is not None:
            valid = [(d, *ts)]
            break

    print(valid[0])
    v = valid[0]
    for num in v:
        assert num in data

    print("Part2: Multiplied: ", v[0]*v[1]*v[2])

if __name__ == "__main__":
    print("LIVE")
    main()
