# Data structure: Strings
# Pattern: Two Pointer 
# Type: Sub-sequence 
# Process:
# 1. Initiate two pointers i,j for two strings
# 2. Loop through the string till any of the string reaches its max length 
# 3. At each index match two chars if matched increase both pointers by one
# 4. if not matched increase the bigger pointer by one 
# 5. Once the travesal is done return the leftover size of the t string 

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i,j = 0,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j+=1
            i+=1
        return len(t[j:])
        