# Data structure: Strings
# Pattern: String basics
# Type: stripping and split  
# Process:
# strip the string all ther empty spaces 
# split the string based on space
# read the last word and return the len of the word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
        
        