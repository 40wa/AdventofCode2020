import math
from functools import reduce

def main():
    with open('data') as f: data = f.read().split()
    
    print("Part One")
    start = int(data[0]) 
    timetable = set(((int(d) if d.isdigit() else None) for d in data[1].split(',')))
    if None in timetable: timetable.remove(None)

    calcd = min((t - (start % t), t) for t in timetable)
    print(calcd[0] * calcd[1])

    print("Part Two")
    system = []
    for i,val in enumerate(data[1].split(',')):
        if val.isdigit():
            system.append((int(val) - i, int(val)))

    M = reduce(lambda x,y: x*y, [s[1] for s in system], 1)

    acc = 0
    for r,p in system:
        m = M // p
        y = pow(m, -1, p)
        acc += r * m * y

    print(acc % M)

if __name__=="__main__":
    main()
