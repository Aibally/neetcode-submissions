class Solution:
    def longestPalindrome(self, s: str) -> str:
        def cntPali(i,j,n):
            count = 0
            while i>=0 and j<n and s[i]==s[j]:
                count += 1
                i-=1
                j+=1
            return count
        palindroms=[]
        n=len(s)
        for i in range(n):
            count1 = cntPali(i,i,n)
            count2 = cntPali(i,i+1,n)

            palindroms.append(s[i-count1+1:i+count1])
            palindroms.append(s[i-count2+1:i+count2+1])
        return max(palindroms, key= lambda x: len(x))
