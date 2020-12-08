import re

def iter_run(instrs, posacc, lookaheads=None):
    pos,accum = posacc[0], posacc[1]
    try:
        if type(instrs[pos]) == tuple:
            return (1, pos, accum)
    except IndexError as e:
        return (2, pos, accum)

    cmd, offset = re.findall('([a-z]+) ([+-][0-9]+)\n', instrs[pos])[0]
    offset = int(offset)
    instrs[pos] = (cmd, offset)


    if cmd == 'acc':
        return (0, pos + 1, accum + offset)
    elif cmd == 'jmp':
        if lookaheads is not None:
            lookaheads.add((pos + 1, accum))
        return (0, pos + offset, accum)
    elif cmd == 'nop':
        if lookaheads is not None:
            lookaheads.add((pos + offset, accum))
        return (0, pos + 1, accum)

def other():
    
    # Part One
    print("Part One")
    with open('data') as f: data = f.readlines()

    posacc = [0,0]
    cpu = (0,0,0)
    lookahead = set()
    while cpu[0] != 1:
        cpu = iter_run(data, posacc, lookahead)
        posacc[0],posacc[1] = cpu[1], cpu[2]

    print(cpu[2])

    # Part Two
    print("Part Two")
    for l in lookahead:
        cpu = (0,*l)
        posacc = [l[0], l[1]] 
        while cpu[0] == 0:
            cpu = iter_run(data, posacc)
            posacc[0],posacc[1] = cpu[1], cpu[2]

        if cpu[0] == 2:
            print(cpu[2])
            break

if __name__=="__main__":
    other()
