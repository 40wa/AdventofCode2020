
DIVISOR = 20201227
def oneloop(x,s):
    return (x * s) % DIVISOR

def manyloops(s, ls):
    init = 1
    for _ in range(ls):
        init = oneloop(init, s)
    return init

def sieve(targ, sn, loopsize):
    init = 1
    for i in range(loopsize):
        init = oneloop(init, sn)
        #print(i+1, init)
        if init == targ:
            print(sn, i+1)

def locate(a):
    sn = 1
    loopsize = 100000
    
    ret = None
    while not ret:
        sn += 1
        ret = sieve(a, sn, loopsize)

    print("located: (loops:", ret, "(subject number:", sn)
    

def doublerun(a,b):
    a_seen = {a: 0}
    b_seen = {b: 0}
    
    a_init = 1
    b_init = 1
    ctr = 0
    while True:
        a_init = oneloop(a_init, a)
        b_init = oneloop(b_init, b)
        ctr += 1

        if (a_init in b_seen.keys()) or (b_init in a_seen.keys()):
            print("FOUND ", a_init, b_init)
            print(a_seen.get(b_init))
            print(b_seen.get(a_init))
            print(ctr)

            # Require verify

            break    
        else:
            a_seen[a_init] = ctr
            b_seen[b_init] = ctr
    

def main():
    test = [5764801, 17807724]
    data = [1614360, 7734663]
    
    print(sieve(data[0], 7, 100000000))
    #print(sieve(test[1], 11, 100000000))
    print(manyloops(data[1], 1182212))


if __name__=='__main__':
    main()
