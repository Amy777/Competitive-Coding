

y = [i for i in input("Enter string").split(',')]
x=[]
import math
for d in y:
    x.append(str(int(round(math.sqrt(float(d))))))
print(x)

print(','.join(x))
k=','.join(x)
print(k)

---------------

'''

Input:  ar1 = [1, 5, 10, 20, 40, 80]
        ar2 = [6, 7, 20, 80, 100]
        ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output: [80, 20]

Input:  ar1 = [1, 5, 5]
        ar2 = [3, 4, 5, 5, 10]
        ar3 = [5, 5, 10, 20]
Output: [5, 5]
'''

import collections
ar1 = [1, 5, 5]
ar2 = [3, 4, 5, 5, 10]
ar3 = [5, 5, 10, 20]
dict1=collections.Counter(ar1)
dict2=collections.Counter(ar2)
dict3=collections.Counter(ar3)
m=min(len(ar1),len(ar2),len(ar3))
resultDict = dict(dict1.items() & dict2.items() & dict3.items())
print(resultDict)

for key,value in dict1.items():
    if key in dict2.keys() and key in dict3.keys():
        if value == dict2[key] and value == dict3[key]:
            print(key, value, "this combination is common")




