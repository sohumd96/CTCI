def isUnique1(s):
    for i in range(0,len(s)):
        for j in range(i+1, len(s)):
            if(s[i] == s[j]):
                return False
    return True

def isUnique2(s):
    letter_store = []
    for i in s:
        if i in letter_store:
            return False
        letter_store.append(i)
    return True

    
