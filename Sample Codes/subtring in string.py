'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

if needle is empty, output=0




def fn(haystack,needle):
    for i in range(len(haystack) - len(needle)+1):
            if haystack[i] != needle[0]:
                continue
            if haystack[i:i+len(needle)] == needle:
                return i
    return -1


def main():
    haystack = "mississipp"
    needle = "issip"
    sub_str = ""
    k=fn(haystack,needle)
    print(k)

if __name__ == '__main__':
    main()

'''

'''
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","ightflo"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i, letter_group in enumerate(zip(*strs)):
        print(i,letter_group)
        if len(set(letter_group)) > 1:
            return strs[1][:i]
    else:
        return min(strs)

def main():
    a = ["flower", "flow", "floightflow"]
    k=longestCommonPrefix(a)
    print(k)

if __name__ == '__main__':
    main()
