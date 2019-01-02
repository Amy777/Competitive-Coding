




'''Plus One

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.


list=[9,9,9]
lenn=len(list)
num=0
j=0

for i in range(lenn-1,-1,-1):
    print(i)
    n=pow(10,i)
    num=num+(n*list[j])
    j+=1
print(num)

num+=1


res=[]
k=num
while(k>0):
    res.append(k%10)
    k=k//10
res=res[::-1]
print(res)

'''

'''nums=[-1,-1,-1,-1,-1,0]
left=1
right=len(nums)-2
sum1,sum2=nums[0],nums[len(nums)-1]

while(left<=right):

    if sum1==sum2:
        if left-right==0:
            print("I am here %d",left+1)
            break
        else:
            left=left+1
            right=right-1
    elif sum1<sum2:
        sum1=sum1+nums[left]
        left=left+1
        print(sum1)
        print(left)
    elif sum1>sum2:
        sum2=sum2+nums[right]
        right=right-1
        print(sum2)
        print(right)

print'''