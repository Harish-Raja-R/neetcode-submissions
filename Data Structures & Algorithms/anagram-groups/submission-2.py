class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_new = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key not in strs_new:
                strs_new[key] = []

            strs_new[key].append(s)

        return list(strs_new.values())