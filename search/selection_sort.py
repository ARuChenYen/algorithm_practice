from copy import deepcopy

def init():
    unsortlist = [3,14,15,926,535,10,-89,79,3236,7,11,520,806,-2]
    or_unsortlist = deepcopy(unsortlist)
    len_unsortlist = len(unsortlist)
    return unsortlist, or_unsortlist, len_unsortlist


def findsmallest(unsortlist):
    tempsmallest_num = unsortlist[0]
    tempsmallest_index = 0
    count = 0
    for i in range(0,len(unsortlist)):
        if tempsmallest_num > unsortlist[i]:
            tempsmallest_num = unsortlist[i]
            tempsmallest_index = i
        count += 1
    print('find smallest num:{} in index:{}, and count:{} times'.format(tempsmallest_num,tempsmallest_index,count))
    unsortlist.pop(tempsmallest_index)
    return unsortlist, tempsmallest_num,count
    
    
if __name__ == '__main__':
    
    unsortlist, or_unsortlist, len_unsortlist = init()
    
    sortlist = []
    count2 = 0
    total_O = 0

    while len_unsortlist != 0:
        unsortlist, samllest, count = findsmallest(unsortlist)
        sortlist.append(samllest)
        len_unsortlist = len(unsortlist)
        count2 +=1
        total_O = total_O + count + 1
        print('sortlist:{}, O(n):{}'.format(sortlist,total_O)) 
    print('The original list:{}\nThe sort list:{}\nThe O(n):{}\n'.format(or_unsortlist,sortlist,total_O))

