def urlify(s, length):
    char_arr = list(s)
    j = len(char_arr)-1
    for i in range (length-1, -1, -1):
        if char_arr[i] != ' ':
            char_arr[j] = char_arr[i]
            j-=1
        else:
            char_arr[j] = '0'
            char_arr[j-1] = '2'
            char_arr[j-2] = '%'
            j -= 3
    return "".join(str(i) for i in char_arr)