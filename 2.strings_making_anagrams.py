def buildMap(s):
    the_map = {}
    for char in s:
        if char not in the_map:
            the_map[char] = 1
        else:
            the_map[char] +=1

    return the_map


if __name__ == '__main__':
    s1 = raw_input()
    s2 = raw_input()
    print anagram(s1, s2)
