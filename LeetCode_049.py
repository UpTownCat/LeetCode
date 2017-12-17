class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return  [[]]
        hash_map = {}
        for s in strs:
            k = ''.join(sorted(s))
            if hash_map.has_key(k):
                hash_map[k].append(s)
            else:
                hash_map[k] = [s]
        return hash_map.values()
