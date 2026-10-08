class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # maxP = float("-inf")
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(i, len(nums)):
        #         product *= nums[j]
        #         maxP = max(maxP, product)
        # return maxP

        result = float("-inf")
        prefix = 1
        suffix = 1
        n = len(nums)

        for i in range(n):
            if prefix == 0: prefix = 1
            if suffix == 0: suffix = 1

            prefix *= nums[i]
            suffix *= nums[n-i-1]
            result = max(result, max(prefix, suffix))

        return result