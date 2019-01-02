def function(val,nums):
    my_dict={}
    prod=0
    for i in nums:
        prod=pow(i,val)
        my_dict[i]=prod





def main():
    num=input("Enter the number")
    stt = input("\n")
    #lisst=stt.split()
    stt.sort()
    r=function(num,stt)
    print(r)

if __name__ == '__main__':
    main()

