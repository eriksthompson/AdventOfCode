with open('input13.txt') as file:
    data = file.read()

    pair1 = []
    pair2 = []
    for lines in data.split('\n\n'):
        s = lines.split('\n')
        pair1.append(eval(s[0]))
        pair2.append(eval(s[1]))
    
def rightOrder(l, r):
    if type(l) == int and type(r) == int:
        if l < r:
            return True
        if l > r:
            return False
    elif type(l) == list and type(r) == list:
        i = 0 
        l1 = min(len(l),len(r))
        while i < l1:
            o = rightOrder(l[i], r[i])
            if o != None:
                return o
            i+=1
        if len(l) == l1:
            return True
        elif len(r) == l1:
            return False
    else:
        if type(l) == int:
            o = rightOrder([l], r)
            if o != None:
                return o
        elif type(r) == int:
            o = rightOrder(l, [r])
            if o != None:
                return o

def part1(): 
    ans = 0
    for i in range(1, len(pair1)+1):

        if rightOrder(pair1[i-1], pair2[i-1]):
            ans+=i
    print(ans)

part1()
