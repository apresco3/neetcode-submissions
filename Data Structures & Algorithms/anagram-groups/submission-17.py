class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict()

        for wrd in strs:
            key = "".join(sorted(wrd))
            
            if key in word_map:
                word_map[key].append(wrd)
            else:
                word_map[key] = [wrd]

        return [x for x in word_map.values()]