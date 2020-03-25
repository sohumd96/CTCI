def main():
    print(check_permutation("asdf", "dfas"))

def check_permutation(s1, s2):
    map = {}
    for i in s1:
        if i not in map:
            map[i] = 1
        else:
            map[i] = map[i] + 1
    for i in s2:
        if i not in map:
            return False
        map[i] = map[i] - 1
        if map[i] == 0:
            del map[i]
    return len(map) == 0

main()
