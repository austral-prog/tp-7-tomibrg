def index_of_by_index(word, list, index):
    if word in list[index:]:
        for i, j in enumerate(list[index:]):
            if j == word:
                return i + index
    else:
        return -1


def index_of_empty(list):
    if ''  in list:
        for i, j in enumerate(list):
            if j.strip() == '':
                return i
                break
    else:
        return -1


def index_of(word, list):
    if word in list:
        for i, j in enumerate(list):  
             if j == word:
                return i
                break
    else:
        return -1


def put(word, list):
    if index_of_empty(list) != -1:
        list[index_of_empty(list)] = word
        return list.index(word)
    else:
        return -1


def remove(word, list):
    counter = 0
    for i, j in enumerate(list):
        if j == word:
            list[i] = ''
            counter += 1
    return counter
