from functools import reduce

class MovingSummer:
    def __init__(self, initial):
        self.circbuf = [set([i]) for i in initial]
        self.currnums = initial
        self.circidx = 0
        
        # Compute pairwise sums and store
        for i, val in enumerate(initial):
            self.circbuf[i] = {self.currnums[i] + self.currnums[j] for j in range(i)}

    def update(self, newnum):
        # is newnum seen before?
        seenflag = False
        for idx,nums in enumerate(self.circbuf):
            if newnum in nums:
                seenflag = True
                break

        if not seenflag:
            return newnum

        # compute new sums
        newsums = set()
        for currnum in self.currnums:
            newsums.add(newnum + currnum)

        self.circbuf[self.circidx] = newsums
        self.currnums[self.circidx] = newnum
        self.circidx = (self.circidx + 1) % len(self.currnums)


def main():

    with open('data') as f: data = f.read().split()
    data = [int(d) for d in data]

    print("Part One")
    ms = MovingSummer(data[:26])
    for d in data[26:]:
        ret = ms.update(d)
        if ret is not None:
            print(ret)
            break

    print("Part Two")
    window = [0,2]
    interval_sum = data[0] + data[1]

    while interval_sum != ret:
        if interval_sum < ret:
            interval_sum += data[window[1]]
            window[1] += 1
        elif interval_sum > ret:
            interval_sum -= data[window[0]]
            window[0] += 1
    
    r = [data[i] for i in range(*window)]
    print(min(r) + max(r))

if __name__=="__main__":
    main()
