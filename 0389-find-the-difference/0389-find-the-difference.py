class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = 0
        t_sum = 0
        for letter in s:
            s_sum += ord(letter)
        for letter in t:
            t_sum += ord(letter)
        return chr(t_sum - s_sum)
