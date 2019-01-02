
strs=["tea","and","ace","ad","eat","dans"]
count= 0
my_dict = {}
res = []
my_dict[0] = [strs[0]]
for i in range(1, len(strs)):
    flag=0
    for j in range(len(my_dict)):
        if all(x in my_dict[j][0] for x in strs[i]):
            my_dict[j].append(strs[i])
            print(my_dict[j])
            flag=1
            break

    if flag==0:
        count = count + 1
        my_dict[count] = [strs[i]]
        print(my_dict)
        print(count)


for j in range(len(my_dict)):
    res.append(my_dict[j])

print(res)

[["ray"],["cod"],["abe"],["ned","den"],["arc"],["jar"],["owl","woo"],["pop"],["paw"],["sky"],["yup","yup","pup"],
 ["fed","fee"],["jul"],["ado"],["why"],["ben"],["mys"],["dem"],["fat"],["you"],["eon"],["sui"],["oct"],["asp"],
 ["ago"],["lea"],["sow"],["hus"],["eve"],["red"],["flo"],["ids"],["tic"],["hag"],["ito"],["zoo"]]
Expected:
[["hag"],["pup"],["ids"],["ito"],["flo"],["red"],["hus"],["sow"],["asp"],["oct"],["sui"],["fee"],["eon"],
 ["tic"],["sky"],["ago"],["paw"],["jul"],["pop"],["jar"],["den","ned"],["owl"],["eve"],["mys"],["abe"],["zoo"],
 ["ado"],["ray"],["cod"],["lea"],["arc"],["dem"],["fat"],["yup","yup"],["woo"],["fed"],["why"],["ben"],["you"]]
'''
def function(nums):
    i = 0
    while (i <= (len(nums) // 2)):
        if nums[i] == nums[i + 1]:
            i += 2
            continue
        elif nums[i] != nums[i + 1]:
            return nums[i+2]

    return nums[i + 2]


def main():
    stt = [1, 1, 2, 2, 4, 4, 5, 5,9]
    print(len(stt) // 2)
    r=function(stt)
    print(r)

if __name__ == '__main__':
    main()

'''