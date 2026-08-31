class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def recursion(si, pi):
            if (si, pi) in cache:
                return cache[(si, pi)]

            if pi == len(p):
                result = si == len(s)
                cache[(si, pi)] = result
                return result

            first_match = (
                si < len(s)
                and (p[pi] == s[si] or p[pi] == ".")
            )

            if pi + 1 < len(p) and p[pi + 1] == "*":
                a = recursion(si, pi + 2)       # * = 0
                b = first_match and recursion(si + 1, pi)  # * = 1+

                result = a or b
            else:
                result = first_match and recursion(si + 1, pi + 1)

            cache[(si, pi)] = result
            return result

        return recursion(0, 0)
