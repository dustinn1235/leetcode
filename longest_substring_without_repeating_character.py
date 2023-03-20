# two pointer. If see a duplicate (check by set) remove c at l and shift l. Keep track of res
def lengthOfLongestSubstring(s):    
    charSet = set()
    
    l = 0
    r = 0
    res = 0

    if len(s) < 2:
        return len(s)

    while r < len(s):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
        r += 1
    return res
