class Solution:
    # x : int = 0
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            ord_string = ""
            # if string == "":
            #         self.x += 1
            
            for char in string:
                n = ord(char) + 2
                ord_string += chr(n)
            encoded_string += (ord_string + " ") 
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string: List[str] = []

        s = s.split(" ")
        s = s[:-1] 
        for string in s:
            # while self.x > 0:
            #     decoded_string.append("")
            #     self.x -= 1

            d_ord_string = ""
            for char in string:
                n = ord(char) - 2
                d_ord_string += chr(n)
            # if d_ord_string != "":
            decoded_string.append(d_ord_string)

        
        return decoded_string
