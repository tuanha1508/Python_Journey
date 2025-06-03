#1298. Maximum Candies You Can Get from Boxes
"""
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Problem Overview: 
    - Given n boxes, each box has a status (open or closed), a number of candies.
    - Some boxes require keys to open, and containedBoxes may contain other boxes.
    - You can open boxes that are open or you have keys for, and you can get candies from them.
    - Return the maximum number of candies you can get.

    Approach: BFS, Graph
    - Use a queue to perform BFS on the boxes.
    - Call ownBox to track which boxes you own.
    - Call ownKey to track which keys you have.
    - Call checkBox to track which boxes have been checked.
    - Iterate and check boxes, keys, and candies to create initial queue.
    - In queue, check the box :
        1. If the box has been checked, continue.
        2. Add candies to the result.
        3. Mark the box as checked.
        4. Add contained boxes to ownBox.
        5. Add keys to ownKey.
        6. Check all boxes and add them to the queue if they are not checked, you have keys, and you own them.
    - Return the total candies collected.
"""
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        ownBox = [0] * n
        ownKey = [0] * n
        checkBox = [0] * n
        res = 0
        dq = deque()

        for i in range(n):
            if status[i]:
                ownKey[i] = 1
        
        for i in initialBoxes:
            ownBox[i] = 1
            if ownKey[i]:
                dq.append(i)
        
        while dq:
            u = dq.popleft()
            if checkBox[u]:
                continue
            res += candies[u]
            checkBox[u] = 1

            for i in containedBoxes[u]:
                ownBox[i] = 1
            
            for i in keys[u]:
                ownKey[i] = 1

            for i in range(n):
                if not checkBox[i] and ownBox[i] and ownKey[i]:
                    dq.append(i)
        
        return res
        

