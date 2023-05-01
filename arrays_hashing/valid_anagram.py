# Hashmap to store frequency. Scan the second string, if we see a char not in s, we know it is not an anagram. 
# Decrease the freq hashmap by 1 for every c. 
# If there is 0 in hashmap then we know the count of some char is not equal => not anagram.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for c in s:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1
        
        for c in t:
            if c not in map:
                return False
            else:
                map[c] -= 1

        for i in map:
            if map[i] != 0:
                return False
        return True