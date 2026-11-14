from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_signature = set()
        anagram_group = defaultdict(list)
        result = []
        for word in strs:
            seen_signature.add(str.join("", sorted(word)))
            anagram_group[str.join("", sorted(word))].append(word)

        for i in anagram_group.values():
            result.append(i)

        return result