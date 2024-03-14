def generator(n):
    for i in reversed(range(n+1)): 
        yield i

n = int(input())
for x in generator(n):
    print (x)