from math import cos, sin, radians

def get_manhattan(data):
    # x, y, rotation
    # 0 rot is East
    # positive rot is anticlockwise
    initstate = [0,0,0]

    switcher = {
        'N': lambda s,val: ((1, s[1] + val),),
        'S': lambda s,val: ((1, s[1] - val),),

        'E': lambda s,val: ((0, s[0] + val),),
        'W': lambda s,val: ((0, s[0] - val),),

        'L': lambda s,val: ((2, s[2] + val),),
        'R': lambda s,val: ((2, s[2] - val),),

        'F': lambda s,val: ((0, s[0] + val * cos(radians(s[2]))),
                            (1, s[1] + val * sin(radians(s[2]))))
    }
    
    for d in data:
        action = d[0]
        val = int(d[1:])

        for idx,updated in switcher[action](initstate, val):
            initstate[idx] = round(updated)

    return initstate

def waypoint_manhattan(data):
    # x, y, waypointx, waypointy
    initstate = [0,0,10,1]
    switcher = {
        'N': lambda s,val: ((3, s[3] + val),),
        'S': lambda s,val: ((3, s[3] - val),),
        'E': lambda s,val: ((2, s[2] + val),),
        'W': lambda s,val: ((2, s[2] - val),),

        'L': lambda s,val: ((2, s[2] * cos(radians(val)) - s[3] * sin(radians(val))),
                            (3, s[2] * sin(radians(val)) + s[3] * cos(radians(val)))),

        'R': lambda s,val: ((2, s[2] * cos(radians(val)) + s[3] * sin(radians(val))),
                            (3, s[2] * sin(radians(-val)) + s[3] * cos(radians(val)))),

        'F': lambda s,val: ((0, s[0] + val * s[2]),
                            (1, s[1] + val * s[3]))
        }

    for d in data:
        action = d[0]
        val = int(d[1:])
        for idx, updated in switcher[action](initstate, val):
            initstate[idx] = round(updated)

    return initstate

def main():
    with open('data') as f: data = f.read().split()


    print("Part One")
    ret = get_manhattan(data)
    print(abs(ret[0]) + abs(ret[1]))

    print("Part Two")
    ret = waypoint_manhattan(data)
    print(abs(ret[0]) + abs(ret[1]))
    


if __name__=='__main__':
    main()
