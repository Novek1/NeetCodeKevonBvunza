class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash_map = {}
        # for index , value in enumerate(nums):
        #     hash_map[value] = index

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    j += 1
                if (nums[i] + nums[j] == target) and (i != j): 
                    return [i, j]



        