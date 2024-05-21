def enumerate_list(list):
        new_list = []
    for j in list:
        if j:
            new_list.append(j)
    for i, j in enumerate(list):
         new_list.append(f'{i}. {j}')    

    return new_list


def enumerate_backwards(list):
        reverse_list = []
    for i in list:
        if i:
            reverse_list.append(i)
    for i, j in enumerate(reverse_list):
        reverse_list.append(f'{i}. {j[::-1]}')
        
    return reverse_list
