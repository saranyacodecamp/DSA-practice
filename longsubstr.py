def lengthOfLongestSubstring(s: str) -> int:
    L = 0
    best = 0
    seen = {}
    for R, ch in enumerate(s):
        if ch in seen and seen[ch] >= L:
            L = seen[ch] + 1
        seen[ch] = R
        best = max(best,R-L+1)
    return best
s = "abcabcabc"
print(lengthOfLongestSubstring(s))
