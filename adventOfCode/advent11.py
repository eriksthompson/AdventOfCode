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
        print(s1)
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