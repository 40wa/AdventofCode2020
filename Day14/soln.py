import re
from itertools import product
from itertools import combinations_with_replacement

# val is int
def apply_mask(mask, val):
    placeval = 1
    accum = 0
    bin_repr = bin(val)

    for i in range(1, len(bin_repr) - 1):
        if mask[-i] == 'X':
            accum += int(bin_repr[-i]) * placeval
        else:
            accum += int(mask[-i]) * placeval
        placeval *= 2
    
    for j in range(i+1, 37):
        if mask[-j] == '1':
            accum += placeval
        placeval *= 2

    return accum

def apply_memmask(mask, memloc):
    placeval = 1
    accum = 0
    bin_repr = bin(memloc)

    floaters = []
    for i in range(1, len(bin_repr) - 1):
        if mask[-i] == '0':
            accum += int(bin_repr[-i]) * placeval
        elif mask[-i] == '1':
            accum += int(mask[-i]) * placeval
        else:
            floaters.append(placeval)
        placeval *= 2
    for j in range(i+1, 37):
        if mask[-j] == '1':
            accum += int(mask[-j]) * placeval
        elif mask[-j] == 'X':
            floaters.append(placeval)
        placeval *= 2
    
    return accum, floaters

def init_prog(instrs, memory):
    grabber = re.compile('^mem\[([0-9]+)\] = ([0-9]+)$')
    mask = None
    for i in instrs:
        if i.startswith('ma'):
            mask = i[7:]
        else:
            res = grabber.findall(i)
            memloc = int(res[0][0])
            val = int(res[0][1])

            memory[memloc] = apply_mask(mask, val)
        
def init_memmask(instrs, memory):
    grabber = re.compile('^mem\[([0-9]+)\] = ([0-9]+)$')
    mask = None
    for i in instrs:
        if i.startswith('ma'):
            mask = i[7:]
        else:
            res = grabber.findall(i)
            memloc = int(res[0][0])
            val = int(res[0][1])
            
            mskd = apply_memmask(mask, memloc)
            for c in list(product(range(0,2), repeat = len(mskd[1]))):
                newloc = mskd[0] + sum([x*y for x,y in zip(c, mskd[1])])
                memory[newloc] = val

def main():
    with open('data') as f: data = f.read().strip().split('\n')
   
    print("Part One")
    memory = dict()
    init_prog(data, memory)
    print(sum(memory.values()))

    print("Part Two")
    memory = dict()
    init_memmask(data, memory)
    print(sum(memory.values()))

if __name__=="__main__":
    main()
