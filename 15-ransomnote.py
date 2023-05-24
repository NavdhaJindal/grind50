class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        for i in magazine: 
            mag_dict[i] = mag_dict.get(i, 0) + 1

        for i in ransomNote:
            mag_dict[i] = mag_dict.get(i, 0) - 1
            if mag_dict[i] < 0:
                return False
        
        return True