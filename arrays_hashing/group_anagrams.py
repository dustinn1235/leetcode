# use bit mask as the key for hashmap. acc -> 201 (2 c 1 a 0 b)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            mask = 0
            for c in word:
                mask += 10 ** (ord(c) - 97)
            if mask not in hashmap:
                hashmap[mask] = [word]
            else:
                hashmap[mask].append(word)
        
        res = []
        for key in hashmap:
            res.append(hashmap[key])
        
        return hashmap.values()