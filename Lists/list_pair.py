# List of integers and a target number
# Find all pairs of elements in the list /
#whose sum matches to given target number

def sum(list,no):
    new_list = []
    i = 0
    while i < len(list):
        total = no - list[i]
        if total in list:
            new_list.append((list[i],total))
        i = i+1
    return new_list


list = [2,3,4,5,7,6,9,1,8] 
no = 7                       #target number
print(sum(list,no))