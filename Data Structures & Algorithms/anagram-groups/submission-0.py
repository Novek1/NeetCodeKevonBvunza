class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_groups = []

        while len(strs) > 0: # slow counter
            current_word = strs.pop(0)
            groups = [current_word]
            i = 0
            while i < len(strs): # fast counter, per slow counter
                if self.isAnagram(current_word, strs[i]):
                    groups.append(strs.pop(i))
                else:
                    i += 1
            list_of_groups.append(groups)
        return list_of_groups


    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False        
        s_ = list(s)
        t_ = list(t)
        i = 0
        while i < len(s):
            if s_[i] not in t_:
                return False
            elif s_[i] in t_:
                t_.remove(s_[i])
            i += 1
        return True
        