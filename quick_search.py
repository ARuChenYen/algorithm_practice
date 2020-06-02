from copy import deepcopy


def init():
    unsortlist = [3, 14, 15, 926, 535, 10, -89, 79, 3236, 7, 11, 520, 806, -2]
    or_unsortlist = deepcopy(unsortlist)
    len_unsortlist = len(unsortlist)
    return unsortlist, or_unsortlist, len_unsortlist


def quick_search(arr):
    
    if len(arr) < 2:
        return arr
    else:
        larger_arr, smaller_arr, pivot, count = separate_arr(arr)
        sortlist= quick_search(smaller_arr) + [pivot] + quick_search(larger_arr)
        #count = count + 1
        return sortlist

def separate_arr(arr):

    larger_arr = []
    smaller_arr = []
    pivot = arr[0]
    count = 0

    for i in arr[1:]:
        if pivot <= i:
            larger_arr.append(i)
            count += 1
        else:
            smaller_arr.append(i)
            count += 1

    return larger_arr, smaller_arr, pivot, count    


if __name__ == '__main__':
    unsortlist, or_unsortlist, len_unsortlist = init()
    sortlist = quick_search(unsortlist)
    print('The original list:{}\nThe sort list:{}\n'.format(or_unsortlist, sortlist))
