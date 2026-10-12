class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # hashset = set()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 temp = sorted([nums[i], nums[j], nums[k]])
        #                 hashset.add(tuple(temp))
        # return [list(t) for t in hashset]

        # hashset = set()
        # for i in range(len(nums)):
        #     eleset = set()
        #     for j in range(i + 1, len(nums)):
        #         third = - (nums[i] + nums[j])
        #         if third in eleset:
        #             temp = sorted([nums[i], nums[j], third])
        #             hashset.add(tuple(temp))
        #         eleset.add(nums[j])
        # return [list(t) for t in hashset]

        result = []
        nums.sort()
        n = len(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k  -= 1
        return result