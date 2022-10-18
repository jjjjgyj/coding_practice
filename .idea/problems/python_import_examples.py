from collections import deque
from collections import defaultdict
from heapq import heapify, heappush, heappop
from math import sqrt

class Test:
    def __init__(self):
        self.pq = []
        for i in range(3, -1, -1):
            heappush(self.pq, i)
        heappop(self.pq)

        self.pq_2 = [6,5,4,3,2]
        heapify(self.pq_2)

        self.num = sqrt(4)
        self.queue = deque([1,2,3])
        self.dict = defaultdict(list)
        for i in range(5):
            self.dict[i].append(i)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class DLL:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

if __name__ == "__main__":
    test = Test()
    print(test.pq[0])
    print(test.pq_2[2])
    print(test.num)
    print(test.queue)
    print(test.dict)