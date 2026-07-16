class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i,j = 0,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j+=1
            i+=1
        if j == len(t):
            return len(t[j:])
        if i == len(s):
            return len(t[j:])
        