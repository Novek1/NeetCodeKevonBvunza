class Solution:
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

