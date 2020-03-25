def one_away(s1, s2):
    def fun(s1, s2):
        switch = True
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                if not switch:
                    return False
                switch = False
        return True
    if(len(s1) == len(s2)):
        return fun(s1, s2)
    if(abs(len(s1)-len(s2)) > 1):
        return False
    if(len(s1) < len(s2)):
       return one_away(s2,s1)
    j = 0
    switch = True
    for i in range(0, len(s1)):
        if j < len(s2) and s1[i] != s2[j]:
            if not switch:
                return False
            switch = False
        else:
            j+=1
    return True