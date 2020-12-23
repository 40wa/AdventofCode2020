import time

# Naive list based soln
def step(curr_idx, cups):

    # Cut out the 3
    active = cups[curr_idx]
    if curr_idx < len(cups) - 3:
        shunt = cups[curr_idx + 1:curr_idx + 4]
        removed = cups[:curr_idx + 1] + cups[curr_idx + 4:]
    else:
        shunt = cups[curr_idx + 1:] + cups[:(curr_idx + 4) % len(cups)]
        removed = cups[(curr_idx + 4) % len(cups):curr_idx + 1]

    # Find next active
    search = (active - 1) % len(cups)
    if search == 0: search = len(cups)
    found = False
    while not found:
        for i,v in enumerate(removed):
            if v == search:
                splice_loc = i
                found = True
                break
        if found:
            break
        search = (search - 1) % len(cups)
        if search == 0: search = len(cups)
        
    # Splice in the 3
    spliced = removed[:splice_loc + 1] + shunt + removed[splice_loc+1:]
    return next(((i+1) % len(spliced)) for i,v in enumerate(spliced) if v==active), spliced

class CircularLL:
    def __init__(self, iterable):
        self.contents = iterable
        # All forward links
        self.curr = 0
        self.num_locs = {num:idx for idx,num in enumerate(self.contents)}
        self.fw = {i:(i+1)%len(iterable) for i in range(len(iterable))}

    def grab_three(self):
        # Return the index of the start of the three
        # and cut it out of the LL
        # also figure out the target for destination label
        idx = self.curr
        threes_idx_a = self.fw[idx]
        b_iter_old,b_iter = None, self.fw[idx]
        threeset = set()
        for i in range(3):
            b_iter_old = b_iter
            threeset.add(self.contents[b_iter])
            b_iter = self.fw[b_iter]
        self.fw[idx] = b_iter 

        # Figure out destination label
        curr_label = self.contents[idx]
        dest_label = curr_label - 1 if curr_label > 1 else len(self.contents)

        while dest_label in threeset:
            dest_label = dest_label - 1 if dest_label > 1 else len(self.contents)
        
        # Figure out destination idx
        splice_idx = self.num_locs[dest_label]
        
        return splice_idx, threes_idx_a,b_iter_old

    def splice(self, splice_idx, threes_idx_a, threes_idx_b):
        # Stitch the threes back into the order
        self.fw[threes_idx_b] = self.fw[splice_idx]
        self.fw[splice_idx] = threes_idx_a

    def step_curr(self):
        self.curr = self.fw[self.curr]

    def __str__(self):
        fwdump = [0] * len(self.fw.values())
        for idx,v in self.fw.items(): fwdump[idx] = v
        return "(CL" + ",\n".join([str(self.contents), str(fwdump)]) + ")"

    def show_circuit(self):
        idx_iter = self.curr
        ret = [self.contents[idx_iter]]
        idx_iter = self.fw[idx_iter]
        while idx_iter != self.curr:
            ret.append(self.contents[idx_iter])
            idx_iter = self.fw[idx_iter]
        print('showing', ret)

    def dump_after_one(self):
        one_idx = self.curr
        while self.contents[one_idx] != 1:
            one_idx = self.fw[one_idx]

        ret = [self.contents[self.fw[one_idx]], self.contents[self.fw[self.fw[one_idx]]]]
        return ret

def main():

    print("Part One")
    cups = [3,8,9,1,2,5,4,6,7]
    data = [3,6,4,2,9,7,5,8,1]
    #cups = data
    new_cups = cups.copy()
    
    tic = time.time() 
    ctr = 0
    curr_idx,cups = 0,cups
    while ctr < 100:
        #print(ctr+1, curr_idx, cups)
        curr_idx,cups = step(curr_idx, cups)
        ctr += 1

    toc = time.time()
    print(ctr+1, curr_idx, cups)
    print("elapsed", toc - tic)

    print("Part Two")
    test = [3,8,9,1,2,5,4,6,7]
    actual = [3,6,4,2,9,7,5,8,1]
    data = actual 
    for i in range(len(data), 1000000):
        data.append(i+1)

    tic = time.time() 
    cl = CircularLL(data)

    for i in range(10000000):
        #if i % 100 == 0:
            #print(i)
        cl.splice(*cl.grab_three())
        cl.step_curr()
    
    res = cl.dump_after_one()
    toc = time.time()
    print(res[0] * res[1])
    print('elapsed', toc - tic)


if __name__=='__main__':
    main()
