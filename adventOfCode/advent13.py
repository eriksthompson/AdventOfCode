with open('input13.txt') as file:
    data = file.read()

    pair1 = []
    pair2 = []
    for lines in data.split('\n\n'):
        s = lines.split('\n')
        pair1.append(eval(s[0]))
        pair2.append(eval(s[1]))
    
def rightOrder(a, b):
    if type(a) == int and type(b) == list:
        return rightOrder([a], b)
    if type(a) == list and type(b) == int:
        return rightOrder(a, [b])
    if type(a) == list and type(b) == list:
        for l, r in zip(a, b):
            x = rightOrder(l, r)
            if x is not None:
                return x
        return rightOrder(len(a), len(b))
    if a == b:
        return None
    return a < b

    """if type(l) == int and type(r) == int:
        if l < r:
            return True
        if l > r:
            return False
    elif type(l) == list and type(r) == list:
        i = 0 
        l1 = min(len(l),len(r))
        while i < l1:
            o = rightOrder(l[i], r[i])
            if o is not None:
                return o
            i+=1
        if len(l) == l1:
            return True
        elif len(r) == l1:
            return False
    else:
        if type(l) == int:
            o = rightOrder([l], r)
            if o is not None:
                return o
        elif type(r) == int:
            o = rightOrder(l, [r])
            if o is not None:
                return o"""

def part1(): 
    ans = 0
    for i in range(1, len(pair1)+1):

        if rightOrder(pair1[i-1], pair2[i-1]):
            ans+=i
    print(ans)

class Signal:
    def __init__(self, arr):
        self.arr = arr
    def __lt__(self, other):
        return rightOrder(self.arr, other.arr)

def part2():
    a, b = Signal([[2]]), Signal([[6]])
    array1 = [a,b]
    for sig1, sig2 in zip(pair1,pair2):
        array1 += [Signal(sig1)]
        array1 += [Signal(sig2)]
    array1.sort()
    print((array1.index(a)+1) * (array1.index(b)+1))


part1()
part2()