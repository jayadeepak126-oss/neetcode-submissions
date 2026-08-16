class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        output = defaultdict(list)

        for c in strs:
            sortedS = ''.join(sorted(c))
            output[sortedS].append(c)
            
        return list(output.values())