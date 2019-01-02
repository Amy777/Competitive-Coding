
# Search Insert Position Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
'''
Input: [1,3,5,6], 5
Output: 2

Input: [1,3,5,6], 2
Output: 1
'''

def bst(nums,key):
    if key > nums[len(nums) - 1]:
        return len(nums)

    if key < nums[0]:
        return 0

    l, r = 0, len(nums) - 1
    while l <= r:
                m = (l + r)//2
                if nums[m] > key:
                    r = m - 1
                    if r >= 0:
                        if nums[r] < key:
                            return r + 1
                    else:
                        return 0

                elif nums[m] < key:
                    l = m + 1
                    if l < len(nums):
                        if nums[l] > key:
                            return l
                    else:
                        return len(nums)
                else:
                    return m

def main():
    arr = [0, 1, 7, 9, 11, 14, 17]
    key = 18
    k=bst(arr,key)
    print(k)
#other simple solution:
#return len([x for x in nums if x<target])

if __name__ == '__main__':
    main()