import re
import time

def gen_twoway(data, fw_bag, bw_bag, bagger):
    for l in data.split('\n'):
        if re.match('.*no other.*', l):
            continue 
        l = bagger.findall(l)
        if l[0][1] not in fw_bag.keys():
            fw_bag[l[0][1]] = set()
        for i in range(1,len(l)):
            fw_bag[l[0][1]].add(l[i])
            if l[i][1] not in bw_bag.keys():
                bw_bag[l[i][1]] = set()
            bw_bag[l[i][1]].add(l[0][1])

def get_containers(bw_bag, target, seen):
    containers = bw_bag.get(target)
    if containers:
        for c in containers:
            if c not in seen:
                seen.add(c)
                get_containers(bw_bag, c, seen)

def count_contained(fw_bag, target, memo):
    if target in memo.keys():
        return memo[target]

    contained = fw_bag.get(target)
    if contained:
        ret = sum((int(b[0]) * (1 + count_contained(fw_bag, b[1], memo)) for b in contained))
        memo[target] = ret 
        return ret
    else:
        return 0

def main():
    
    # Part One
    print("Part One")
    p1_a = time.perf_counter()
    with open('data') as f: data = f.read().strip()
    bagger = re.compile('([0-9]*)\s*([a-z]+ [a-z]+) bags*')
    fw_bag,bw_bag = dict(),dict()
    gen_twoway(data, fw_bag, bw_bag, bagger)
    seen = set()
    get_containers(bw_bag, 'shiny gold', seen)
    p1_b = time.perf_counter()
    print(len(seen))
    print("time elapsed: ", p1_b - p1_a)


    # Part Two
    print("Part Two")
    p2_a = time.perf_counter()
    cc = count_contained(fw_bag, 'shiny gold', dict())
    p2_b = time.perf_counter()
    print(cc)
    print('time elapsed: ', p2_b - p2_a)

if __name__=="__main__":
    main()
