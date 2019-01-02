
secret="1123"
guess="0111"
my_dict1={}
my_dict2={}
bull=0
cows=0

for i in range(len(secret)):
    my_dict1[i]=secret[i]
    my_dict2[i]=guess[i]

for i in my_dict1.keys():
    if my_dict1[i]== my_dict2[i]:
        bull+=1
        my_dict2[i]=999
        my_dict1[i]=888

for i in my_dict1.keys():
    if my_dict1[i] in my_dict2.values():
        cows+=1
        for k,j in my_dict2.items():
            if j==my_dict1[i]:
                my_dict2[k]=99
                break

print(cows,bull)
strr=""
strr=str(bull)+"A"+str(cows)+"B"
print(strr)

print(my_dict1)
print(my_dict2)

import collections
s, g = collections.Counter(secret), collections.Counter(guess)
print(s)
print(g)
a = sum(i == j for i, j in zip(secret, guess))
print(a)
str2= '%sA%sB' % (a, sum((s & g).values()) - a)
for i in (s & g).values():
    print(i)
print(str2)

