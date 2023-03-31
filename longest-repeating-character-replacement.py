# https://leetcode.com/problems/longest-repeating-character-replacement/



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest, start = 0, 0
        freq = defaultdict(int)

        for end in range(len(s)):
            freq[s[end]] += 1
            while (end - start + 1) - max(freq.values()) > k:
                freq[s[start]] -=  1
                start += 1

            longest = max(longest, end - start + 1)

        return longest
