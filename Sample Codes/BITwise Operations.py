'''
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

a="11"
b='1'

a=int(a,2)
b=int(b,2)

c=a+b
d=format(c,'b')
print(d)
print(type(d))
print(format(c,'b'))