def binary_search(array, length, number):
    begin = mid = 0
    end = length -1
    while(begin <= end):
        mid = (begin + end)//2
        if number < array[mid]:
            end = mid - 1
        else:
            if number > array[mid]:
                begin = mid + 1
            else:
                return mid
    return -1


def binary_search_recursive(array, number, length, start = 0):
    # length is the last index, is the end of the array
    if length >= start:
        mid = (length + start)//2

        if array[mid] == number:
            return mid
        elif number < array[mid]:
            return binary_search_recursive(array, number, mid-1, start)
        else:
            return binary_search_recursive(array, number, length, mid+1)
    else:
        return -1
    

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

print(binary_search(numbers, len(numbers), 10))

print(binary_search_recursive(numbers, 10, len(numbers)-1))