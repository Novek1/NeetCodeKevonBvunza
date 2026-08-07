class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        count = 0

        if s == "":
            return count
        if len(s) == 1:
            return 1

        traverse_set: set = set()

        while right < len(s):
            if s[right] not in traverse_set:
                traverse_set.add(s[right])
                right += 1
                count = max(count, right - left) 

            else:
                traverse_set.discard(s[left])
                left += 1                      

        return count