class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = {}


        for word in strs:

            idx = [0] * 26

            for char in word:

                index = ord(char) - ord("a")
                idx[index] += 1

            id_key = tuple(idx)

            if id_key not in dict1:
                dict1[id_key] = [word]
                
            else:

                dict1[id_key].append(word)
        
        return list(dict1.values())



