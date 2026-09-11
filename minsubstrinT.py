from collections import defaultdict
def minimum_substr(s:str,t:str) -> str:
    d = defaultdict(int)
    for char in t:
        d[char] += 1
    formed, total = 0, len(d)
    len_ans = float('inf')
    l = r = 0
    ansl = ansr = 0
    while r < len(s):
        char = s[r]
        if char in d:
            d[char] -=1
            if d[char] == 0: 
                formed +=1
        while l <= r and formed == total:
            curr_ans = r-l+1
            if curr_ans < len_ans:
                len_ans = curr_ans
                ansl, ansr = l, r+1
            char = s[l]
            if char in d:
                if d[char] == 0:
                    formed -= 1
                d[char] += 1
            l+=1
        r+=1
    return "" if len_ans == float('inf') else s[ansl:ansr]
print(minimum_substr("aabbbccccdedfg","abc"))


