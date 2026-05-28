class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = max(hand)
        count = [0 for _ in range(n+1)]
        for num in hand:
            count[num] += 1

        for i in range(n+1):
            while count[i] != 0:
                for j in range(i,i+groupSize):
                    if j>n or count[j] == 0:
                        return False
                    else:
                        count[j] -= 1
        return True
            

        