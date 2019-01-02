
s="leetcodai"
vowels= ["a", "e", "i", "o", "u"]
left = 0
right = len(s) - 1
s_list=list(s)
while (left <= right):
    #if left == right:
    # check for vowel

    if s_list[left] in vowels:
        while(s_list[right] not in vowels):
            right=right-1

        s_list[left],s_list[right]=s_list[right],s_list[left]   # To swap the values

        right=right-1
    left=left+1

print(s_list)


