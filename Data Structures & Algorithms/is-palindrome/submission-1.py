class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        s_ = ""

        for char in s:
            if char.isalnum() == False:
                continue
            s_ += char

        rev_s = s_[::-1]
        print(s_)
        if (rev_s == s_):
            return True
        else :
            return False


