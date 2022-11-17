def bubble_sorting(string):

    string = string.upper().replace(' ','')
    length = len(string)

    string_list = list(string)

    for i in range(length):
        
        for j in range(length-1):
            if string_list[j] > string_list[j+1]:
                aux = string_list[j+1]
                string_list[j+1] = string_list[j]
                string_list[j] = aux
    
    return ''.join(string_list)

str_input = input()

test = bubble_sorting(str_input)

print(f'início: {test}')