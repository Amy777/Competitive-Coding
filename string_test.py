

def checkpaly(subb):
    subtemp=subb[::-1]
    print("String", subb, "Ulta", subtemp)
    if subtemp==subb:
        return (len(subb))
    else:
        return 0;


def main():

 Len=0;
 longsub='';

 str=input("Enter the string")
 print(str)
 print(str[0])

 for i in range(len(str)):
         for k in range(i,len(str)):
             sub=str[i:k];
             l=checkpaly(sub);
             if l>Len:
                 Len=l;
                 longsub=sub;
 print("--------------")
 print(l)
 print(Len)
 print(longsub)


if __name__ == '__main__':
    main()





