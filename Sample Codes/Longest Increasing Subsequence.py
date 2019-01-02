'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''
nums=[10,9,2,5,3,7,101,18]
dirr = []
res = []
for i in range(len(nums) - 1):
    if nums[i + 1] - nums[i] > 0:
        dirr.append(1)
    else:
        dirr.append(-1)

for i in dirr:
    j = i
    count = 0
    while (dirr[j] > 0):
        j += 1
        count += 1
    res.append(count)

print(max(res) + 1)
print(dirr)
print(res)
