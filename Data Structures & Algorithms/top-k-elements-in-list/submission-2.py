class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        count_map = defaultdict(int)

        for item in nums:
            count_map[item] += 1

        sorted_count_map = {k: v for k, v in sorted(count_map.items(), key=lambda item: item[1])}
        stuff = list(sorted_count_map.keys())
        results = []
        

        for i in range(k):
            results.append(stuff[-1])
            stuff.pop(-1)
            

        return results

        
