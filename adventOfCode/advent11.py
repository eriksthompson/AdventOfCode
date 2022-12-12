from math import lcm

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#Parse input data
#mi- monkey items (int list), o- operation (string list),
# t - test divisible by,
#  tr- if true throw to monkey #, fa - if false throw to monkey #
mi, o, t, tr, fa = [], [], [], [], []
with open('input11.txt') as file:
    data = file.read().splitlines()
    for l in data:
        s1 = l.strip(' ').split(' ')
        if s1[0] == '':
            continue
        if s1[0] == 'Starting':
            l1 = []
            for s in s1:
                if representsInt(s.strip(',')):
                    l1.append(int(s.strip(',')))
            mi.append(l1)
        elif s1[0] == 'Operation:':
            l1 = []
            l1.append(s1[-2])
            l1.append(s1[-1])
            o.append(l1)
        elif s1[0] == 'Test:':
            t.append(int(s1[-1]))
        elif s1[1] == 'true:':
            tr.append(int(s1[-1]))
        elif s1[1] == 'false:':
            fa.append(int(s1[-1]))
        
print(mi, o, t, tr, fa, sep='\n')
def part1(rounds):
    inspectC = [0] * len(mi)
    for r in range(rounds):
        #print(inspectC)
        #iterate through monkeys
        for m in range(len(mi)):
            inspectC[m] = inspectC[m] + len(mi[m])
            #iterate through monkey items
            for i in range(len(mi[m])):
                w = mi[m][0] #current item's worry level
                mi[m].remove(w)
                modifier = o[m][1]
                if modifier == 'old':
                    modifier = w
                if o[m][0] == '*':
                    w *= int(modifier)
                elif o[m][0] == '+':
                    w += int(modifier)
                w = int(w/3)
                if w % t[m] == 0:
                    mi[tr[m]].append(w)
                else:
                    mi[fa[m]].append(w)
    inspectC.sort(reverse=True)
    return inspectC[0]*inspectC[1]

# -> 20 rounds of monkey shenanigans
print(part1(20))

#@return greatest common factor of array
# Code contributed by Mohit Gupta_OMG
def gcf(l):
    num1=l[0]
    num2=l[1]
    gcf1=find_gcf(num1,num2)
    for i in range(2,len(l)):
        gcf1=find_gcf(gcf1,l[i])
    return gcf1

def find_gcf(x, y):
    while(y):
        x, y = y, x % y
    return x

def product(l):
    ans = 1
    for x in l:
        ans *= x
    return ans

def part2(rounds):
    master_divisor = lcm(*(t1 for t1 in t))
    inspectC = [0] * len(mi)
    for r in range(rounds):
        #print(inspectC)
        #iterate through monkeys
        for m in range(len(mi)):
            inspectC[m] = inspectC[m] + len(mi[m])
            
            #iterate through monkey items
            for i in range(len(mi[m])):
                w = mi[m][0] #current item's worry level
                mi[m].remove(w)
                modifier = o[m][1]
                if modifier == 'old':
                    modifier = w
                if o[m][0] == '*':
                    w *= int(modifier)
                elif o[m][0] == '+':
                    w += int(modifier)
                w %= master_divisor
                
                if w % t[m] == 0:
                    mi[tr[m]].append(w)
                else:
                    mi[fa[m]].append(w)
        

    inspectC.sort(reverse=True)
    return inspectC[0]*inspectC[1]
# -> 10000 rounds of monkey shenanigans
# worry level no longer divided by 3
#TODO find way to manage w high values
#End of round modulo greatest common factor?
print(part2(10000))


            
