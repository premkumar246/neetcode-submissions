class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = sorted(list(s))
        t_chars = sorted(list(t))
        if s_chars == t_chars:
            return True
        else:
            return False
        