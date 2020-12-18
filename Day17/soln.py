
def get_shape(x):
    shape = []
    tmp = x
    for d in range(getdepth(x)):
        shape.append(len(tmp))
        tmp = tmp[0]

    return tuple(shape)

def getdepth(x):
    return 1 + getdepth(x[0]) if isinstance(x, list) else 0

def get_boundaries(cycles, initconditions, dim=3):
    
    shape = list(get_shape(initconditions))
    while len(shape) < dim: shape.append(1)
    
    return [d+2*cycles for d in shape]

def init_space(cycles, space, initconditions, dims=3):
    for i in range(len(initconditions)):
        for j in range(len(initconditions[0])):
            if dims == 3:
                space[cycles+i][cycles+j][cycles] = initconditions[i][j]
            elif dims == 4:
                space[cycles+i][cycles+j][cycles][cycles] = initconditions[i][j]

def count_ones(space):
    if isinstance(space, int):
        return space
    else:
        return sum(count_ones(s) for s in space)

def get_neighbouring_coords(shape, targetcoord, dims=3):
    if dims == 3:
        x,y,z = targetcoord
    elif dims == 4:
        x,y,z,w = targetcoord
    ret = set()
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                if dims == 3:
                    if (0<=x+i<shape[0]) and (0<=y+j<shape[1]) and (0<=z+k<shape[2]):
                        ret.add((x+i,y+j,z+k))
                elif dims == 4:
                    for l in range(-1,2):
                        if (0<=x+i<shape[0]) and (0<=y+j<shape[1]) and (0<=z+k<shape[2]) and (0<=w+l<shape[3]):
                            ret.add((x+i,y+j,z+k,w+l))
    ret.remove(targetcoord)
    return ret

def iter_space(space, dims=3):
    # need to start getting neighbours now
    shape = get_shape(space)
    if dims == 3:
        newspace = [[[0 for k in range(shape[2])] for j in range(shape[1])] for i in range(shape[0])]
    elif dims == 4:
        newspace = [[[[0 for l in range(shape[3])] for k in range(shape[2])] for j in range(shape[1])] for i in range(shape[0])]
    
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                if dims == 3:
                    coords = get_neighbouring_coords(shape, (i,j,k))
                    ctr = 0
                    for c in coords:
                        x,y,z = c
                        if space[x][y][z] == 1:
                            ctr += 1
                        if ctr == 4:
                            break

                    if space[i][j][k] == 1:
                        newspace[i][j][k] = int(ctr == 2 or ctr == 3) 
                    else:
                        newspace[i][j][k] = int(ctr == 3)
                elif dims == 4:
                    for l in range(shape[3]):
                        coords = get_neighbouring_coords(shape, (i,j,k,l), dims=4)
                        ctr = 0
                        for c in coords:
                            x,y,z,w = c
                            if space[x][y][z][w] == 1:
                                ctr += 1
                            if ctr == 4:
                                break

                        if space[i][j][k][l] == 1:
                            newspace[i][j][k][l] = int(ctr == 2 or ctr == 3) 
                        else:
                            newspace[i][j][k][l] = int(ctr == 3)

    return newspace

def main():
    with open('data') as f: data = f.read().split()
   
    print("Part One")
    data = [[int(d == '#') for d in r] for r in data]
    cycles = 6 

    bounds = get_boundaries(cycles, data)
    space = [[[0 for k in range(bounds[2])] for j in range(bounds[1])] for i in range(bounds[0])]

    # Initialise space
    init_space(cycles, space, data)
    
    for i in range(6):
        space = iter_space(space)
    print(count_ones(space))

    print("Part Two")
    bounds = get_boundaries(cycles, data, dim=4)
    space = [[[[0 for l in range(bounds[3])] for k in range(bounds[2])] for j in range(bounds[1])] for i in range(bounds[0])]

    init_space(cycles, space, data, dims=4)


    for i in range(6):
        space = iter_space(space, dims=4)

    
    print(count_ones(space))


if __name__=="__main__":
    main()
