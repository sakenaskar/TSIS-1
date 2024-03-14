def generator(n):
    for i in range(n): 
        if i % 2 == 0:
            yield i

n = int(input())
for x in generator(n):
    print (x, end="; ")