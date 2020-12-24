import re

def get_painted(parsed):
    painted_locs = set()

    mover = {'e' : (1,0),
             'se': (1,-1),
             'sw': (0,-1),
             'w' : (-1,0),
             'nw': (-1,1),
             'ne': (0,1)}

    for line in parsed:
        loc = [0,0] 
        for ins in line:
            m = mover[ins]
            loc[0] += m[0]
            loc[1] += m[1]
        loc = tuple(loc)
        if loc in painted_locs:
            painted_locs.remove(loc)
        else:
            painted_locs.add(loc)
    return painted_locs

def step(state):
    new = [[0 for _ in range(len(state[0]))] for _ in range(len(state))]
    adj_dirs = [(1,0),(1,-1),(0,-1),(-1,0),(-1,1),(0,1)]
    
    for i in range(len(new)):
        for j in range(len(new[0])):
            adj_ctr = 0
            for dx,dy in adj_dirs:
                adj_ctr += state[(i + dy) % len(state)][(j + dx) % len(state[0])]
            
            if (state[i][j] == 1) and not (0 < adj_ctr <= 2):
                new[i][j] = 0
            elif (state[i][j] == 0) and adj_ctr == 2:
                new[i][j] = 1
            else:
                new[i][j] = state[i][j]
    
    return new

def conway(start_coords, days):
    # Determine bounds
    xmin,xmax,ymin,ymax = 0,0,0,0
    for x,y in start_coords:
        xmin,xmax = min(xmin, x),max(xmax, x)
        ymin,ymax = min(ymin, y),max(ymax, y)
    
    playfield = [[0 for _ in range(xmax - xmin + 2*(days))] for _ in range(ymax - ymin + 2*(days))]
    for x,y in start_coords:
        playfield[y][x] = 1
    for i in range(days):
        playfield = step(playfield)
    
    return sum(sum(line) for line in playfield)
    
def main():
    with open('data') as f: data = f.read().split()
    parsed = [re.findall('(e|se|sw|w|nw|ne)', s) for  s in data]
    
    print('Part One')
    painted_locs = get_painted(parsed)
    print(len(painted_locs))

    print('Part Two')
    count = conway(painted_locs, 100)
    print(count)

if __name__=='__main__':
    main()
