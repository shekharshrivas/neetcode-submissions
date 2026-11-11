class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result 

    def decode(self, s: str) -> List[str]:
        result = []
        l = 0
        while l < len(s):
            j = l
            while s[j] != "#":
                j += 1
            wlen = int(s[l:j])
            result.append(s[j+1:j
             + wlen+1])
            l = j+1+wlen
        return result