#909. Snakes and Ladders
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