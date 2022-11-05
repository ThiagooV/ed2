def linear_search(array, number):
    result = []
    for i in range(len(array)):
        if array[i] == number:
            result.append(i)
    if not result:
        return -1
    return result


numbers = [12,2,45,36,2,56,2]

print(linear_search(numbers, 2))