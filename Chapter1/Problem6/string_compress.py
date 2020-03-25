def compress(s):
    if len(s) == 0:
        return ""
    count = 1
    curr_l = s[0]
    solution = ""
    for l in s[1:]:
        if l == curr_l:
            count += 1
        else:
            solution += curr_l + str(count)
            count = 1
            curr_l = l
    solution += curr_l + str(count)
    return solution
