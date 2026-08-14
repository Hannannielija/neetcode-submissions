class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            lenght = len(word)
            encoded += (f"{lenght}#{word}")
        return encoded
            
        


    def decode(self, s: str) -> List[str]:
        palguna = []
        a = 0
        kata = ""

        while a < len(s):
            b = a
            panjang = 0
            while s[b] != "#":
                b += 1
            
            panjang = int(s[a:b])
            palguna.append(s[b + 1:b + 1+panjang])
            a = b+1+panjang

        return palguna





