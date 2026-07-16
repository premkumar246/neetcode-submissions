# Data structure: Strings
# Pattern: String basics
# Type: ASCII value 
# Process:
# loop thorugh the string one lessthan the length of the string 
# find ASCII value of each char and its adjcent char 
# find differnce and calculate absolute and add to sum
# repeat for all the elements
class Solution:
    def scoreOfString(self, s: str) -> int:
        sum=0
        for i in range(len(s)-1):
            sum+=abs(ord(s[i+1])-ord(s[i]))
        return sum
        