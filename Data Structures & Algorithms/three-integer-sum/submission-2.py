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

        hashset = set()
        for i in range(len(nums)):
            eleset = set()
            for j in range(i + 1, len(nums)):
                third = - (nums[i] + nums[j])
                if third in eleset:
                    temp = sorted([nums[i], nums[j], third])
                    hashset.add(tuple(temp))
                eleset.add(nums[j])
        return [list(t) for t in hashset]