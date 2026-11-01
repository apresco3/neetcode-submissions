class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_map = {}

        if len(s) != len(t):
            return False

        for c in s:
            word_map[c] = word_map.get(c, 0) + 1

        for c in t:
            if c not in word_map:
                return False
            word_map[c] -= 1

        return all(values == 0 for key, values in word_map.items())