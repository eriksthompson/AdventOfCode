with open('input12.txt') as file:
    data = file.read().splitlines()

#start and end
S, E = 0,0
grid1 = []
for l in range(len(data)):
    l1 = []
    for c in range(len(data[0])):
        l1.append(data[l][c])
        if data[l][c] == 'S':
            S = (l,c)
        if data[l][c] == 'E':
            E = (l,c)
    grid1.append(l1)

dict1 = {}
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(alpha)):
    dict1[alpha[i]] = i+1 
dict1['S'] = 1
dict1['E'] = 26

grid = []
def copyGrid():
    for l in grid1:
        l1 = []
        for s in l:
            l1.append(s)
        grid.append(l1)

def travel(part):
    queue1 = []
    S1 = set()
    for r in range(len(grid1)):
        for c in range(len(grid1[0])):
            if (part==1 and grid1[r][c]=='S') or (part==2 and dict1[grid1[r][c]] == 1):
                queue1.append((r,c, 0))

    while len(queue1) > 0:
        front = queue1.pop(0)
        #print(front)
        x,y, d = front[0], front[1], front[2]
        if (x,y) in S1:
            continue
        S1.add((x,y))
        if grid[x][y] == 'E':
            return d
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = x+dr
            cc = y+dc
            if 0<=rr<len(grid1) and 0<=cc<len(grid1[0]) and dict1[grid1[rr][cc]]<=1+dict1[grid1[x][y]]:
                queue1.append((rr,cc,d+1))
        """if x-1 >= 0 and dict1[grid1[x-1][y]] <= dict1[grid1[x][y]] + 1:
            #travel left
            queue1.append((x-1, y, d+1))
        if y-1 >= 0 and dict1[grid1[x][y-1]] <= dict1[grid1[x][y]] + 1:
            #travel up
            queue1.append((x, y-1, d+1))
        if x+1 < len(grid[0]) and dict1[grid1[x+1][y]] <= dict1[grid1[x][y]] + 1:
            #travel right
            queue1.append((x+1, y, d+1))
        if y+1 < len(grid) and dict1[grid1[x][y+1]] <= dict1[grid1[x][y]] + 1:
            #travel down
            queue1.append((x, y+1, d+1))"""

def part1():
    copyGrid()
    print(travel(1))
    print(travel(2))

part1()