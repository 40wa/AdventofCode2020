# Accum is a dictionary
def diffs(data, accum, all_diffs):
    prev = 0
    for d in data: 
        diff = d - prev
        all_diffs.append(diff)
        if diff not in accum.keys(): accum[diff] = 0
        accum[diff] += 1
        prev = d
    
    # Account for final adapter
    if 3 not in accum.keys(): accum[diff] = 0
    accum[3] += 1
    all_diffs.append(3)

def combinate_rec(data, idx, trellis):
    if trellis[idx]:
        return trellis[idx]

    i = 1
    lookaheads = []
    while (i <= 3) and (idx + i < len(trellis)) and (data[idx + i] - data[idx] <= 3):
        lookaheads.append(idx + i)
        i += 1

    if lookaheads:
        ret = sum((combinate_rec(data, r, trellis) for r in lookaheads))
    else:
        ret = 1

    trellis[idx] = ret
    return ret

def main():
    with open('data') as f: data = f.read().split()
    
    data = [int(d) for d in data]

    print("Part One")
    data = sorted(data)
    accum = dict()
    all_diffs = []
    diffs(data, accum, all_diffs)
    print(accum[1] * accum[3])

    print("Part Two")
    data.append(data[-1] + 3)
    trellis = [None] * len(data)
    combinate_rec(data, 0, trellis)
    print(sum(trellis[:3]))

if __name__=="__main__":
    main()
