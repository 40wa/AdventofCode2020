
def get_seatloc(d):
    print(d)

def string_to_binary(targstring, oneletter):
    init = 0b1
    acum = 0
    for idx,l in enumerate(targstring[::-1]):
        if l == oneletter:
            acum += init
        init *= 2
    return acum

def encode(seatcode):
    row = string_to_binary(seatcode[:7], 'B')
    col = string_to_binary(seatcode[7:], 'R')
    return (row, col, row * 8 + col)

def main():
    with open('data') as f:
        data = f.read().split()

    # Part One
    print("Part One")

    # Encode to integers
    encoded = [encode(sc) for sc in data]

    encoded.sort(key=lambda x: x[2])

    print(encoded[-1][2])

    # Part Two
    print("Part Two")
    for i in range(len(encoded)-1):
        if (encoded[i+1][2] - encoded[i][2] == 2):
            print(encoded[i][2] + 1)
            break
    

    

if __name__=="__main__":
    main()
