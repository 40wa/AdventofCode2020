import re

# Assume data is an array of tuples containing the instructions
def fw_run(instrs, pos, accum, lookaheads=None):
    try:
        if type(instrs[pos]) == tuple:
            return (pos, accum)
    except IndexError as e:
        return (pos, accum)
    
    cmd, offset = re.findall('([a-z]+) ([+-][0-9]+)\n', instrs[pos])[0]
    offset = int(offset)
    instrs[pos] = (cmd, offset)

    if cmd == 'acc':
        return fw_run(instrs, pos + 1, accum + offset, lookaheads)
    elif cmd == 'jmp':
        if lookaheads is not None:
            lookaheads.add((pos + 1, accum))
        return fw_run(instrs, pos + offset, accum, lookaheads)
    elif cmd == 'nop':
        if lookaheads is not None:
            lookaheads.add((pos + offset, accum))
        return fw_run(instrs, pos + 1, accum, lookaheads)

def main():
    
    with open('data') as f: data = f.readlines()
    
    # Part One
    print("Part One")
    lookaheads = set()
    print(fw_run(data, 0, 0, lookaheads)[1])

    # Part Two
    print("Part Two")
    for l in lookaheads:
       res = fw_run(data, *l, set())
       if res[0] == len(data):
           print(res[1])
           break


if __name__=="__main__":
    main()
