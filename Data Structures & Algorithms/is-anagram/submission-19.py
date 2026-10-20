class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = defaultdict(int)

        for c in s:
            char_dict[c] += 1
        
        for c in t:
            if c not in char_dict or char_dict[c] == 0:
                return False
            else:
                char_dict[c] -= 1
        
        return all(x == 0 for x in char_dict.values())