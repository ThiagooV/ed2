def binarySearch(array, length, number):
    begin = center = 0
    end = length -1
    while(begin <= end):
        center = (begin + end)//2
        if number < array[center]:
            end = center - 1
        else:
            if number > array[center]:
                begin = center + 1
            else:
                return center
    return -1


def binarySearchRecursive(array, number, length, start = 0):
    # length is the last index, is the end of the array
    if length >= start:
        mid = (length + start)//2

        if array[mid] == number:
            return mid
        elif number < array[mid]:
            return binarySearchRecursive(array, number, mid-1, start)
        else:
            return binarySearchRecursive(array, number, length, mid+1)
    else:
        return -1
    
    


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

print(binarySearch(numbers, len(numbers), 10))

print(binarySearchRecursive(numbers, 10, len(numbers)-1))