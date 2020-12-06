from functools import reduce

def main():
    with open('data') as f: data = f.read()
    
    # Part One
    print("Part One")
    print(reduce(lambda cnt,ls: cnt + len(set(ls.replace('\n',''))),
                 data.split('\n\n'),
                 0))

    print("Part Two")
    print(reduce(lambda cnt,ls: 
                     cnt + len(reduce(
                                      lambda s,l: set(s).intersection(set(l)),
                                      ls.split())),
                 data.split('\n\n'),
                 0))

if __name__=="__main__":
    main()
