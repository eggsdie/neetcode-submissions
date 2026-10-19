class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False


        count = Counter(hand)
        hand.sort()
        #hand=[1,2,4,2,3,5,3,4]
        #Counter({2: 2, 4: 2, 3: 2, 1: 1, 5: 1})
        print(count[4])
        #groupSize=4

        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i]-=1

        return True