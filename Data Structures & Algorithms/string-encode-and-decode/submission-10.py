class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            n = len(word)
            encoded_string = encoded_string + str(n) + "#" + word

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        l = r = 0

        while r < len(s):
            l = r

            while s[r] != "#":
                r += 1

            word_len = int(s[l:r])
            word = s[r+1:r+1+word_len]

            decoded_strs.append(word)

            r = r + 1 + word_len

        return decoded_strs