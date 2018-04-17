def ransom_note(magazine, ransom):

    d1 = {}
    for i in magazine:
        d1[i] = 0
    for i in magazine:
        if d1[i] == 0:
            d1[i] = 1
        else:
            d1[i] = d1[i] + 1

    d2 = {}
    for i in ransom:
        d2[i] = 0
    for i in ransom:
        if d2[i] == 0:
            d2[i] = 1
        else:
            d2[i] = d2[i] + 1
            
    flag = True
    for key in d2:
        if (not (key in d1)) or d2[key] > d1[key]:
            flag = False
            break
    return flag

m = input()
n = input()
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)

if answer:
    print("Yes")
else:
    print("No")
