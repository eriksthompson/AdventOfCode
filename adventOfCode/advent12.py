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

print(grid1)
print(S, E, sep=' ')
