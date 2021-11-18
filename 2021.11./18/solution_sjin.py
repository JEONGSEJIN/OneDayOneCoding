n = int(input())
x = list(map(int, input().split(' ')))

def PressCoordi(n, x):
    tmp = list(set(x))
    x_sort = sorted(tmp)

    coordi = dict()
    for i in range(len(x_sort)):
        if x_sort[i] not in coordi.keys() :
            coordi[x_sort[i]] = i

    for i in range(n):
        print(coordi[x[i]], end=' ')
        
PressCoordi(n,x)
