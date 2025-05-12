class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        seen = set()
        pairs = 0
        for word in words: 
            if word[::-1] in seen:
                pairs += 1
                seen.remove(word[::-1])
            else:
                seen.add(word)
        return pairs