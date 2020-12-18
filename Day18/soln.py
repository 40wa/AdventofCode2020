import re

def repl_p1(line):
    tokend = line.replace(' ','')
    
    sf = [0]
    op = []

    def collapse(x,y): return lambda x,y: y
    
    opcodes = {'*': lambda x,y: x*y,
               '+': lambda x,y: x+y,
               'null': collapse }

    for c in tokend:
        if c.isdigit():
            c = int(c)
            sf[-1] = op.pop()(sf[-1],c) if (op and (op[-1] is not collapse)) else c
        elif c == '(':
            op.append(opcodes['null'])
            sf.append(0)
        elif c == ')':
            op.pop()
            if op and op[-1] is not collapse:
                l = sf.pop()
                sf[-1] = op.pop()(sf[-1],l)
            else:
                sf[-1] = sf.pop()
        else:
            op.append(opcodes[c])
   
    assert len(op) == 0
    return sf[0]

def repl_p2(line):
    tokend = line.replace(' ','').join(['(', ')'])
    
    sf = [0]
    op = []

    def collapse(x,y): return lambda x,y: y

    opcodes = {'*': lambda x,y: x*y,
               '+': lambda x,y: x+y,
               'null': collapse }

    for c in tokend:
        if c.isdigit():
            c = int(c)
            if op:
                if op[-1] == '*':
                    sf.append(c)
                elif op[-1] == '+':
                    sf[-1] = opcodes[op.pop()](sf[-1], c)
                else:
                    sf[-1] = c
            else:
                sf[-1] = c 

        elif c == '*':
            op.append('*')
        elif c == '+':
            op.append('+')
        elif c == '(':
            op.append('null')
            sf.append(0)
        elif c == ')':
            while op and (op[-1] == '*'):
                l = sf.pop()
                sf[-1] = opcodes[op.pop()](sf[-1], l)
            op.pop()
            c = sf.pop() 
            if op:
                if op[-1] == '*':
                    sf.append(c)
                elif op[-1] == '+':
                    sf[-1] = opcodes[op.pop()](sf[-1], c)
                else:
                    sf[-1] = c
            else:
                sf[-1] = c 

    assert len(op) == 0
    return sf[0]


def main():
    with open('data') as f: data = f.read().strip().split('\n')
    
    print("Part One")
    print(sum(repl_p1(d) for d in data))

    print("Part Two")
    print(sum(repl_p2(d) for d in data))

if __name__=="__main__":
    main()
