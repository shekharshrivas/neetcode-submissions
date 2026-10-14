class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # maxlen = 0
        # for i in range(len(s)):
        #     hasharray = [0]*26; maxf = 0
        #     for j in range(i, len(s)):
        #         hasharray[ord(s[j]) - ord("A")] += 1
        #         maxf = max(maxf, hasharray[ord(s[j]) - ord("A")])
        #         changes = (j - i + 1) - maxf
        #         if changes <= k:
        #             maxlen = max(maxlen, j - i + 1)
        #         else:
        #             break
        # return maxlen

        l = 0; r = 0; maxl = 0; maxf = 0
        hashmap = [0] * 26
        while r < len(s):
            hashmap[ord(s[r]) - ord("A")] += 1
            maxf = max(maxf, hashmap[ord(s[r]) - ord("A")])
            if (r - l + 1) - maxf > k:
                hashmap[ord(s[l]) - ord("A")] -= 1
                maxf = max(hashmap)
                l += 1

            if (r - l + 1) - maxf <= k:
                maxl = max(maxl, r - l + 1)
            r += 1
        return maxl