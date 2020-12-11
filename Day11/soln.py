from functools import reduce

def get_adj_cnt(l, i, j, default):
    cnters = [get_adj_default(l, i+1, j, default),
                get_adj_default(l, i-1, j, default),
                get_adj_default(l, i, j+1, default),
                get_adj_default(l, i, j-1, default),
                get_adj_default(l, i+1, j+1, default),
                get_adj_default(l, i-1, j-1, default),
                get_adj_default(l, i+1, j-1, default),
                get_adj_default(l, i-1, j+1, default)]
    return sum(cnters)

def get_sight_cnt(l, i, j):
    dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
    
    ctr = 0
    for d in dirs:
        init = [i,j]
        init[0] += d[0]
        init[1] += d[1]
        while 0 <= init[0] < len(l) and 0 <= init[1] < len(l[0]):
            if l[init[0]][init[1]] == 0:
                init[0] += d[0]
                init[1] += d[1]
            elif l[init[0]][init[1]] == 1:
                break
            else:
                ctr += 1
                break
    return ctr


def get_adj_default(l, i,j, default):
    if i < 0 or j < 0:
        return default
    try:
        return int(l[i][j] == 2)
    except IndexError:
        return default

def pred_cnt(l, pred):
    if type(l) is not list:
        return int(pred(l))
    else:
        return sum((pred_cnt(a, pred) for a in l))
        
def iter_game(state):
    output = [[i for i in d] for d in state]
    
    muteflag = False
    for i in range(len(state)):
        for j in range(len(state[0])):
            # Count adjacent seats
            adj_cnt = get_adj_cnt(state, i, j, 0)

            if state[i][j] == 1:
                if (adj_cnt == 0):
                    output[i][j] = 2
                    muteflag = True
                else:
                    output[i][j] = state[i][j] 
            elif state[i][j] == 2:
                if (adj_cnt >= 4):
                    output[i][j] = 1
                    muteflag = True
                else:
                    output[i][j] = state[i][j]
            else:
                output[i][j] = state[i][j]

    return (muteflag, output)

def iter_game_p2(state):
    output = [[i for i in d] for d in state]
    
    muteflag = False
    for i in range(len(state)):
        for j in range(len(state[0])):
            
            # Count adjacent seats

            adj_cnt = get_sight_cnt(state, i, j)

            if state[i][j] == 1:
                if (adj_cnt == 0):
                    output[i][j] = 2
                    muteflag = True
                else:
                    output[i][j] = state[i][j] 
            elif state[i][j] == 2:
                if (adj_cnt >= 5):
                    output[i][j] = 1
                    muteflag = True
                else:
                    output[i][j] = state[i][j]
            else:
                output[i][j] = state[i][j]

    return (muteflag, output)

def main():
    with open('data') as f: data = f.read().split()

    # 0 is floor, 1 is empty seat, 2 is occupied
    m = {'.': 0, 'L': 1, '#': 2}
    data = [[m[j] for j in d] for d in data]

    print("Part One")
    init = (True, data)

    ctr = 0
    while init[0] == True:
        init = iter_game(init[1])

    cnt = pred_cnt(init[1], lambda x: x == 2)
    print(cnt)

    print("Part Two")
    init = (True, data)

    ctr = 0
    while init[0] == True:
        ctr += 1
        init = iter_game_p2(init[1])

    cnt = pred_cnt(init[1], lambda x: x == 2)
    print(cnt)

if __name__=="__main__":
    main()
