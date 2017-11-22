# Longest Substring Without Repeating Characters

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d_chr = {}
        max = []
        smax = []
        for i in range(len(s)) :
            if s[i] in smax :
                if len(smax) > len(max) : max = smax
                smax = smax[d_chr[s[i]]+1:] + [s[i]]
                d_chr[s[i]] = i
            else :
                d_chr[s[i]] = i
                smax.append(s[i])
        return [len(max), ''.join(max)] if len(smax) < len(max) else [len(smax), ''.join(smax)]


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("bbBbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("current"))
print(s.lengthOfLongestSubstring("curreut"))
print(s.lengthOfLongestSubstring("given"))