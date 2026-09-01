class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""
        n = len(s)
        
        for center_idx in range(n):
            # 1. Odd length palindromes (center is a single character)
            left = center_idx
            right = center_idx
            
            # Expand outward as long as characters match and indices stay in bounds
            while left >= 0 and right < n and s[left] == s[right]:
                # If this is the longest valid palindrome we've seen, save it
                if (right - left + 1) > len(best):
                    best = s[left : right + 1]
                # Move pointers outward
                left -= 1
                right += 1

            # 2. Even length palindromes (center is between two characters)
            left = center_idx
            right = center_idx + 1
            
            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) > len(best):
                    best = s[left : right + 1]
                left -= 1
                right += 1
                
        return best