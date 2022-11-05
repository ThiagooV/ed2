def ordered_search(list, number):
    index = 0
    while index < len(list) and list[index] < number:
        index +=1
    aux = []
    if number == list[index]:
        while list[index] == number and index < len(list):
            aux.append(index)
            index += 1
        return aux
    else:
        return -1

numbers = [2,4,7,7,7,7,7,7,9,13,15,21]

print(ordered_search(numbers, 9))