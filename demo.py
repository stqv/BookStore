#Assignment 1

books = [('Harry Potter and the Goblet of Fire',2000,455),('The Girl With the Dragon Tattoo',2008,600),('Bad Blood',2000,772),('Adults in the Room',2017,555),('The Cost of Living',2018,745)]

# 1.a sort the list based on price
for i in range(len(books)-1):
    for j in range(len(books)-2):
        if books[j][2]>books[j+1][2]:
            books[j],books[j+1] = books[j+1],books[j]

print(books)


# 1.a sort the list based on book name
for i in range(len(books)-1):
    for j in range(len(books)-2):
        if books[j][0]>books[j+1][0]:
            books[j],books[j+1] = books[j+1],books[j]

print(books)

# 1. b


for i in range(len(books)):
    l = list(books[i])
    l[0],l[1],l[2] = l[1],l[2],l[0]
    books[i] = tuple(l)

print(books)

# Assignment 2
from itertools import combinations
# qdt = list(map(int,input().split()))
qdt = [0,-1,2,3,-2,4,5]
comb = combinations(qdt, 4)
qdl = []
for i in list(comb):
    s = sum(i)
    if s == 2:
        qdl.append(i)

for i in qdl:
    print(list(i))