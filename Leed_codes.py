def myAtoi(strs):
    """
    :type str: str
    :rtype: int
    """
    if not strs:
        return "ggg"
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    print(shortest)
    return shortest


if __name__ == '__main__':
    strs=(input("enter the string"))
  #  k=myAtoi(strs)
   # print(k)

    if not strs:
        print("kuch nahi hua")
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                print(shortest[:i])
    print(shortest)
