def binary_search(array,number):
    mid=0
    lowest=0
    highest=len(array)-1
    itr=0
    while lowest <= highest:
        mid=(lowest+highest)//2
        if array[mid] < number:
            lowest=mid+1
            
            itr += 1
        elif array[mid] > number:
            highest=mid-1
            print(arr[highest] )
            
        else:
            return (mid)
    return -1
    
arr=[2,4,6,7,10,12,15]
number= 6

result = binary_search(arr,number)

if result != -1:
    print("Element is present at index", result)
else:
    print("element not present ")
