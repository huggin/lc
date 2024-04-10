class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        j = len(deck) - 1
        a = deque()
        a.append(deck[j])
        j -= 1
        while j >= 0:
            a.append(a.popleft())
            a.append(deck[j])
            j -= 1
        a.reverse()
        return a
