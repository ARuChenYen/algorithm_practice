# find a number using binary search and show how many times to find it.


original_seri = list(range(1,1001))

def inputunm():
    while True :
        input_num = float(input('Enter a num (0-1000) : '))
        
        if input_num >=0 and input_num <=1000:
            break
        else:
            print('Please Enter a number between 0 and 1000 again.')
    
    print(input_num)
    return input_num

def cont_process(count,guess,input_num,mid):
    print('Guess {} times \nGuess number:{}, index:{}\nInput num:{}' .format(count,guess,mid,input_num))
    

def binary_search(original_seri,input_num):
    low = 0
    high = len(original_seri)-1
    count = 0
    
    while low <= high:
        mid = int((low + high)/2)
        guess = original_seri[mid]
        
        count +=1
        cont_process(count,guess,input_num,mid)
        
        if input_num > guess:
            low = mid + 1
        elif input_num < guess:
            high = mid-1
        else:
            return mid
    
    return None

if __name__ == '__main__':
    input_num = inputunm()
    result = binary_search(original_seri,input_num)
    print(result)
    

    



            


