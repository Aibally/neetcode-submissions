class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)
        memo={}

        def recursion(word):
            if word in memo: return memo[word]
            for i in range(1,len(word)):
                a = word[:i]
                b = word[i:]
                if a in words_set and (b in words_set or recursion(b)):
                    memo[word]= True
                    return True
            memo[word]=False
            return False
        res=[]
        for word in words:
            words_set.remove(word)
            if recursion(word):
                res.append(word)
            words_set.add(word)
        return res