class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for i in range(len(strs[0])):
            for item in strs:
                if i == len(item) or item[i] != strs[0][i]:
                    return result
            
            result += strs[0][i]
        
        return result