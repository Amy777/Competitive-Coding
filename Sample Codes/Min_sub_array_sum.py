'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
'''
s=5
nums=[2,3,1,2,4,3]

sums=[0]
ss=0
for i in nums:
   ss+=i
   sums.append(ss)
ans=[]
for i in range(len(nums)):
    left=i
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if sums[mid+1]-sums[i]>=s:
            ans.append(mid-i)
            right=mid-1
        else:
            left=mid+1
print(min(ans)+1)
print(sums)
print(ans)


'''
res = []
summ = 0
for i in range(len(nums)):
    summ = nums[i]
    j = i
    count = 1
    while (summ < s and j<len(nums)-1):
        j = j + 1
        summ = summ + nums[j]
        count += 1
    if summ>=s:
        res.append(count)
if len(res)==0:
    print(0)
else:
    print(min(res))
print(res)
'''