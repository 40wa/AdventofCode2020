import time

def parse(rules):
    ret = dict()
    for r in rules:
        s = r.split(':')
        if s[1][1] == '"':
            v = s[1][2]
        elif len(s[1].split('|')) == 1:
            v = tuple([int(n) for n in s[1].split()])
        else:
            v = [tuple([int(n) for n in r.split()]) for r in s[1].split('|')]
        ret[int(s[0])] = v
    return ret 

def eval_prod(rule, t, idx, ctx):
    accum = 0
    for r in rule:
        inter = check(r, t, idx, ctx)
        if inter != 0:
            idx += inter
            accum += inter
        else:
            return 0
    return accum

def eval_sum(rule, t, idx, ctx):
    for r in rule:
        ret = check(r, t, idx, ctx)
        if ret:
            return ret
    return 0

def eval_base(rule, t, idx=0, ctx=None):
    if len(t) - idx >= len(rule):
        return all((t[idx+i] == rule[i] for i in range(len(rule)))) * len(rule)
    else:
        return 0

# 0: 2 3 | 3 2 encoded as (0, [(2,3),(3,2)])
# ctx is db of rules
def check(rule, t, idx=0, ctx=None):
    if isinstance(rule, tuple):
        return eval_prod(rule, t, idx, ctx)
    elif isinstance(rule, list):
        return eval_sum(rule, t, idx, ctx)
    elif isinstance(rule, str):
        return eval_base(rule, t, idx, ctx)
    elif isinstance(rule, int):
        return check(ctx[rule], t, idx, ctx)

def all_strings(rule, ctx):
    if isinstance(rule, tuple):
        ret = None
        for r in rule:
            res = all_strings(r, ctx)
            if not ret:
                ret = res
            else:
                tmp = set()
                for s in ret:
                    for a in res:
                        tmp.add(s+a)
                ret = tmp
        return ret
    if isinstance(rule, list):
        ret = set()
        for r in rule:
            ret = ret.union(all_strings(r, ctx))
        return ret
    if isinstance(rule, int):
        return all_strings(ctx[rule], ctx)
    if isinstance(rule, str):
        return {rule}


def check_p2(t, sctr=0):
    for w in v_42:
        if t.startswith(w):
            res = check_p2(t[len(w):], sctr + 1)
            if res:
                return res

    toggle = True
    lctr = 0
    while toggle:
        if len(t) == 0 and sctr > lctr and lctr > 0:
            return True
        toggle = False
        for w in v_31:
            if t.endswith(w):
                lctr += 1
                t = t[:len(t) - len(w)]
                toggle = True
                break

    return False

with open('data') as f: data = f.read().split('\n\n')
ctx = parse(data[0].split('\n'))
ipts = data[1].split()
v_42 = all_strings(42, ctx)
v_31 = all_strings(31, ctx)

def main():
    
    print('Part One')
    tic = time.time()
    ret = sum(int(check(0, d, 0, ctx) == len(d)) for d in ipts)
    toc = time.time()
    print(ret)
    print('elapsed: ', toc - tic)

    print('Part Two')
    tic = time.time()
    ret = sum(int(check_p2(d)) for d in ipts)
    toc = time.time()
    print(ret)
    print('elapsed: ', toc - tic)

if __name__=='__main__':
    main()
