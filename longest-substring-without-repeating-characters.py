# https://leetcode.com/problems/longest-substring-without-repeating-characters/



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         last_seen = {}
#         start = 0
#         longest = 0
        
#         for i, c in enumerate(s):
#             if c in last_seen and last_seen[c] >= start:
#                 start = last_seen[c] + 1
#             else:
#                 longest = max(longest, i - start + 1)
                
#             last_seen[c] = i
            
#         return longest
            charSet = set()
            l = 0 
            res = 0
            
            for r in range(len(s)):
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                charSet.add(s[r])
                res = max(res, r-l+1) #since counting starts from 0 we add 1
            return res
