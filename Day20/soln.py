from functools import reduce

def parse(data):
    ret = dict()
    for d in data:
        d = d.strip().split('\n')
        num = int(d[0][5:-1])
        img = [[int(v == '#') for v in r] for r in d[1:]]
        ret[num] = img
    return ret

def get_edges(num,img):
    t = (num,tuple(img[0]))
    l = (num,tuple([r[0] for r in img])[::-1])
    r = (num,tuple([r[-1] for r in img]))
    b = (num,tuple(img[-1])[::-1])
    n = [t,r,b,l]
    revt = (num,t[1][::-1])
    revl = (num,l[1][::-1])
    revr = (num,r[1][::-1])
    revb = (num,b[1][::-1])
    m = [revt, revr, revb, revl]
    return (n,m)

def p1_meme(data):
    edgectr = dict()
    numtoedge = dict()
    edgetonum = dict()
    parsed = parse(data)
    for num,img in parsed.items():
        edges = get_edges(num,img)

        if num not in numtoedge.keys():
            numtoedge[num] = set()
        numtoedge[num].update(*edges)

        for i in range(len(edges)):

            for e in edges[i]:
                edgectr[e] = edgectr.get(e, 0) + 1
                if e[1] not in edgetonum.keys():
                    edgetonum[e[1]] = set()
                edgetonum[e[1]].add(num)

    lonectr = dict()
    for edge,nums in edgetonum.items():
        if len(nums) == 1:
            lonectr[tuple(nums)[0]] = lonectr.get(*nums, 0) + 1

    corners = []
    for num,ctr in lonectr.items():
        if ctr == 4:
            corners.append(num)

    return corners

def p2_stitch(large, data, start):
    print('start ', start)
    parsed = parse(data)

    nums_to_edges = dict()
    edges_to_nums = dict()
   
    init = None
    for num,img in parsed.items():
        edges = get_edges(num, img)
        if num == start:
            init = (num, [e[1] for e in edges[0]])

        nums_to_edges[num] = [e[1] for e in edges[0]]

        for i in range(4):
            if edges[0][i][1] not in edges_to_nums.keys():
                edges_to_nums[edges[0][i][1]] = set()
            edges_to_nums[edges[0][i][1]].add(num)

            if edges[1][i][1] not in edges_to_nums.keys():
                edges_to_nums[edges[1][i][1]] = set()
            edges_to_nums[edges[1][i][1]].add(num)
   
    large[0][0] = Cell(*init)
    print('init ', large[0][0]) 

    for i in range(len(large)):
        for j in range(len(large[0])):
            print("Now on ", i,j)
            if large[i][j] != None:
                continue
            if j == 0:
                # Source from above
                prev = large[i-1][j]
                new_nums = edges_to_nums[prev.get_edge(2)]
                if len(new_nums) == 2:
                    tmp = new_nums.copy()
                    tmp.remove(prev.get_num())
                    new_num = list(tmp)[0]
                    targ_edge = prev.get_edge(2)

                    new_cell = Cell(new_num, nums_to_edges[new_num])
                    # Calibrate new cell
                    for _ in range(8):
                        if new_cell.get_edge(3) == targ_edge:
                            print("ASSIGNED: ", i,j)
                            large[i][j] = new_cell
                            break
                        else:
                            new_cell.step()
            else:
                # Source from the left
                prev = large[i][j-1]
                new_nums = edges_to_nums[prev.get_edge(1)]
                if len(new_nums) == 2:
                    tmp = new_nums.copy()
                    tmp.remove(prev.get_num())
                    new_num = list(tmp)[0]
                    targ_edge = prev.get_edge(1)

                    new_cell = Cell(new_num, nums_to_edges[new_num])
                    # Calibrate new cell
                    toggle = False
                    for _ in range(8):
                        if new_cell.get_edge(3) == targ_edge:
                            print("ASSIGNED: ", i,j)
                            large[i][j] = new_cell
                            toggle = True
                            break
                        else:
                            new_cell.step()
                else:
                    print('failed length check ', new_nums)

                            
class Cell:
    def __init__(self, num, edges):
        assert len(edges) == 4
        self.num = num
        self.edges = edges
        self.rot = 0
        self.flip = False
        
    def do_rot(self):
        tmp = self.edges[-1]
        for i in range(1,len(self.edges)):
            self.edges[-i] = self.edges[-i-1]
        self.edges[0] = tmp

    def do_mir(self):
        self.edges[0] = self.edges[0][::-1]
        tmp = self.edges[1]
        self.edges[1] = self.edges[3][::-1]
        self.edges[2] = self.edges[2][::-1]
        self.edges[3] = tmp[::-1]
         
        self.flip = not self.flip
   
    # Cycles through 8 states
    def step(self):
        self.do_rot()
        if self.rot == 3:
            self.do_mir()
        self.rot = (self.rot + 1) % 4

    def __str__(self):
        return ', '.join(["Cell(", str(self.num), 'rot ' + str(self.rot), str(self.flip), str(self.edges), ')'])
        #return '\n'.join(['Cell ' + str(self.rot) + " " + str(self.flip)] + [str(e) for e in self.edges])

    def get_edge(self, direction):
        assert 0 <= direction < 4
        return self.edges[direction]
    def get_num(self):
        return self.num
    

def main():
    with open('data') as f: data = f.read().split('\n\n')

    print("Part One")
    corners = p1_meme(data)
    print(reduce(lambda x,y: x*y, corners))

    print("Part Two")
    large = [[None for i in range(12)] for j in range(12)]
    stitch = p2_stitch(large, data, corners[0])

if __name__=='__main__':
    main()
