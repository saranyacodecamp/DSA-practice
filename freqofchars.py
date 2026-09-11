def freqofchars(word:str) -> dict:
    strlist = {}
    for i, char in enumerate(word):
        if char in strlist:
            strlist[char] += 1
        else:
            strlist[char] = 1
    return strlist
print(freqofchars('LEetcode'))
print(freqofchars('saranya'))

