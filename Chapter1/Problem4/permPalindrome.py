def pal_perm(s):
    s = s.replace(" ", "")
    map = {}
    for c in s:
        if c in map:
            map[c]+=1
        else:
            map[c] = 1
    count = 0
    for c in map:
        if map[c]%2 == 1:
            count +=1
        if count > 1:
            return False
    return True