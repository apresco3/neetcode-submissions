class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in word_dict:
                word_dict[key].append(word)
            else:
                word_dict[key] = [word]

        return [values for key, values in word_dict.items()]