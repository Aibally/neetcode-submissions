class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        visited = {};max_length = -1
        for i in range(len(s)):
            if s[i] in visited:
                max_length = max(max_length,i-visited[s[i]]-1)
            else:
                visited[s[i]]=i
        return max_length
