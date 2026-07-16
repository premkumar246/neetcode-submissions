# Data Structure: Strings
# Pattern: Two pointers
# Type: Subsequence
# Both i, j starts from first index of the respective strings
# i,j moves when there is a match 
# only j moves when there is a mismatch 
# i scans each element of the small string 
# j scans each element of the big string 

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        return i == len(s)

# 
