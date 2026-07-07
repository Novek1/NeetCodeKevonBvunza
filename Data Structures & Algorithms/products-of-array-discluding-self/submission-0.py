class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        product_arr = []
        while i < len(nums):
            temp = nums.pop(i)
            product = 1
            for j in range(len(nums)):
                product = product * nums[j]
            product_arr.append(product)
            nums.insert(i, temp)
            i += 1
        return product_arr