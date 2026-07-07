import heapq
from collections import defaultdict

class AuctionSystem:

    def __init__(self):
        self.bids = {}
        self.bid_history = defaultdict(int)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        if itemId not in self.bids:
            self.bids[itemId] = [(-bidAmount, -userId)]
        else:
            heapq.heappush(self.bids[itemId], (-bidAmount, -userId))

        self.bid_history[(itemId, userId)] = bidAmount

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        if self.bids[itemId]:
            heapq.heappush(self.bids[itemId], (-newAmount, -userId))
        self.bid_history[(itemId, userId)] = newAmount

    def removeBid(self, userId: int, itemId: int) -> None:
        self.bid_history[(itemId,userId)] = -1


    def getHighestBidder(self, itemId: int) -> int:
        if itemId not in self.bids:
            return -1

        while self.bids[itemId]:
            bidAmount, userId = -self.bids[itemId][0][0], -self.bids[itemId][0][1]
            if self.bid_history[(itemId, userId)] == bidAmount:
                return userId
            heapq.heappop(self.bids[itemId])

        return -1
