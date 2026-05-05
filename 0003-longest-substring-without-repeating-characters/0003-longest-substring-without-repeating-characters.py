class Solution(object):
   def lengthOfLongestSubstring(self, s):
    chars = {}
    left = 0
    res = 0

    for right in range(len(s)):
        if s[right] in chars and chars[s[right]] >= left:
            left = chars[s[right]] + 1
        chars[s[right]] = right
        res = max(res, right - left + 1)

    return res