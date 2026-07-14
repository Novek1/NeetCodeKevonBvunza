class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict:dict = {}

        for index, num in enumerate(numbers):
            num_dict[index] = num


        for i in num_dict.keys():
            for r in num_dict.keys():
                if num_dict[i] + num_dict[r] == target:
                    return [i + 1 ,  r + 1]
        return []

            