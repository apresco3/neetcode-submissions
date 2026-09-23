class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_count = {}

        for c in s:
            c_count[c] = c_count.get(c, 0) + 1

        for c in t:
            if c in c_count:
                c_count[c] -= 1
            else:
                return False
        
        return all(v == 0 for v in c_count.values())