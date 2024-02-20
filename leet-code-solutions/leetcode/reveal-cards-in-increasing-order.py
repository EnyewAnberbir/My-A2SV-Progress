class Solution:
  def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    queue = collections.deque()
    deck.sort()
    deck.reverse()
    for card in deck:
      queue.rotate()
      queue.appendleft(card)

    return list(queue)