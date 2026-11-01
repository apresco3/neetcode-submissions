class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict()

        for w in strs:
            key = "".join(sorted(w))

            if key in word_map:
                word_map[key].append(w)
            else:
                word_map[key] = [w]

        return [values for key, values in word_map.items()]