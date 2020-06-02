from copy import deepcopy

def init():
    unsortlist = [3,14,15,926,535,10,-89,79,3236,7,11,520,806,-2]
    or_unsortlist = deepcopy(unsortlist)
    len_unsortlist = len(unsortlist)
    return unsortlist, or_unsortlist, len_unsortlist

def sum(arr):
    if len(arr)==0:
        return 0
    else:
        total = arr[0]+sum(arr[1:])
        return total
    
def count_item(arr):
    if len(arr)==0:
        return 0
    else:
        total_item = 1 + count_item(arr[1:])
        return total_item

def findmax(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    else:
        previous_max = findmax(arr[1:])
        if arr[0] > previous_max:
            return arr[0]
        else:
            return previous_max
    
if __name__ == '__main__':
    unsortlist, or_unsortlist, len_unsortlist = init()
    
    sortlist = []
    count2 = 0
    total_O = 0

    total = sum(unsortlist)
    total_item = count_item(unsortlist)
    findmax_num = findmax(unsortlist)
    
    print(total)
    print(total_item)
    print(findmax_num )