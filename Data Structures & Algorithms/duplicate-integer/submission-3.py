class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            dic[nums[i]] = True
        return False