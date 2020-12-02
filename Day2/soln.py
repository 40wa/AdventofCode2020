
def validcheck(a,b, targletter, targstring):
    ctr = 0 
    for l in targstring:
        if l == targletter:
            ctr += 1
        if ctr > b:
            return False
    if ctr < a:
        return False
    else:
        return True

def dumbcheck(a,b, targletter, targstring):
    letterctr = 0
    for l in targstring:
        if l == targletter:
            letterctr += 1

    return (letterctr >= a) and (letterctr <= b)

def idxcheck(a,b, targletter, targstring):
    try:
        lcheck = (targstring[a-1] == targletter)
        rcheck = (targstring[b-1] == targletter)
    except Exception as e:
        print("dump state: " + str((a,b,targletter,targstring)))
        print(e)
        raise
    # Return xor
    return (lcheck and not rcheck) or (rcheck and not lcheck)

def main():
    data = open('data').read().split('\n')
    data = data[:-1]
    
    retctr = 0
    
    # Part One
    print("Part One:")
    for d in data:
        sep = d.split(' ')
        digits = sep[0].split('-')
        okrange = (int(digits[0]), int(digits[1]))
        a,b = sorted(okrange)
        targletter = sep[1][0]
        targstring = sep[-1]

        v = validcheck(a,b, targletter, targstring)
        if v:
            retctr += 1
        #print(v, a,b, targletter, targstring)
    print(retctr)

    # Part Two
    print("Part Two:")
    retctr = 0 
    for d in data:
        sep = d.split(' ')
        digits = sep[0].split('-')
        okrange = (int(digits[0]), int(digits[1]))
        a,b = sorted(okrange)
        targletter = sep[1][0]
        targstring = sep[-1]

        v = idxcheck(a,b, targletter, targstring)
        if v:
            retctr += 1
        
    print(retctr) 

    # Check idxcheck
    assert idxcheck(1,3, 'a', 'abcde')
    assert not idxcheck(1,3, 'b', 'cdefg')
    assert not idxcheck(2,9, 'c', 'ccccccccc')
    

        

if __name__ == "__main__":
    main()
