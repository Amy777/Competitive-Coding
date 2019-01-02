# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
'''
def bin_ser(store_sort, item):
    print(store_sort,item)
    first = 0
    last = len(store_sort) - 1

    while (first < last):
        print(store_sort, item)
        print(first,last)
        mid = (first + last) // 2
        print(mid)
        if store_sort[mid] == item:
            return store_sort[mid]
        else:
            lop = abs(item - store_sort[mid - 1])
            print("item, store")
            print(item, store_sort[mid-1])
            print(lop)

            c = abs(item - store_sort[mid])
            print(c)
            if mid < len(store_sort) - 1:
                r = abs(item - store_sort[mid+1])
            else:
                r = abs(item - store_sort[0])
            print(r)
            if (c < lop and c < r):
                return store_sort[mid]
            elif (r < c and r < lop):
                first = mid + 1
            elif (lop < r and lop < c):
                last = mid - 1

    return store_sort[first]


def main():
    stores=[1,5,11,16,20]
    houses=[5,10,17]
    # write your code in Python 3.6
    res = []

    store_sort = sorted(stores)
    res = []
    print("hi")

    for i in range(len(houses)):
        res.append(bin_ser(store_sort, houses[i]))
        #print(res)
    print (res)
if __name__ == '__main__':
    main()

'''


with open('text_file.txt', 'r') as f:
    con=f.read()

with open('text_file.txt','r') as rl:
    con2=rl.readlines()

with open('text_filew.txt','w') as ww:
    ww.write('newly created file')


with open('text_file.txt', 'r') as r2:
    con3 = r2.readline()  #PRINTS ONLY ONE LINE AT ONE TIME


print(con)

for k in con:
    print(k,len(k),type(k))     #It takes each character of the line. If you want to use the entire word use con=open(".txt","r")
print(con2)
print(type(con))
print(type(con2))
print(con3)
#print(con2.strip())
print(str(con3))
print(con3.split())
con4=open("text_file.txt",'r')
print(con4)     #output : <_io.TextIOWrapper name='text_file.txt' mode='r' encoding='cp1252'>
for i in range(4):
    con3=con4.readline()
    print(con3)
#print(con3.split()[1][-1:])