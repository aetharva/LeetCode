class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        lcp = ""
        minlen = min(strs, key = len)
        
        for i in range(0, len(minlen)): 
            temp = strs[0][i]
            for j in range(0, len(strs)):
                if strs[j][i] != temp:
                    return lcp        
            lcp += temp
        
        return lcp