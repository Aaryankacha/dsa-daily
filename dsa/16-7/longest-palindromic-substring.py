class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s  # A single char is always a palindrome

        start = 0   # Start index of longest palindrome
        end = 0     # End index of longest palindrome

        for i in range(len(s)):
            len1 = self.expandFromCenter(s, i, i)     # Odd-length
            len2 = self.expandFromCenter(s, i, i + 1) # Even-length
            max_len = max(len1, len2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end+1]

    def expandFromCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
