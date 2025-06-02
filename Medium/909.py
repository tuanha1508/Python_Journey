#909. Snakes and Ladders
"""
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    
    Problem Overview: Find the minimum of move to the cell n * n in a board

    - Call v is the number of rows and columns in the board
    - For this problem, we can use a BFS approach to find all the shortest paths from the start to the end.
    - We will use a queue to store the current position and then we iterate through all the possible moves (For this problem is from 1 to 6)
    - Call step is the next position we can move to and we will check if the position is a snake or a ladder.
    - We calculate next row and column suitable for the current step.
    - After that, call variable check is the value of the cell we can move to, if it equal v * v, we return the number of moves. 
    Else, if the res check is -1, we update the res check with res curr + 1 and push the check into the queue.
    - After all, if we cannot reach the end, we return -1.
"""
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        v = len(board)
        res = [-1] * (v * v + 1)
        q = deque()
        res[1] = 0
        q.append(1)
        while q:
            curr = q.popleft()
            for i in range(1, 7):
                step = curr + i
                if step > v * v:
                    break
                row = (step - 1) // v
                col = (step - 1) % v
                u = board[v - 1 - row][(v - 1 - col) if (row % 2 == 1) else col]
                check = u if u > 0 else step
                if check == v * v:
                    return res[curr] + 1
                if res[check] == -1:
                    res[check] = res[curr] + 1
                    q.append(check)
        return -1