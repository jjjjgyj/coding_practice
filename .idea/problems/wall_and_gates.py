from collections import deque

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
class WallsAndGates:
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        visited = set()

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        self.calc_steps(rooms, queue, visited)
        return rooms

    def calc_steps(self, rooms, queue, visited):
        step = 0
        while queue:
            step += 1
            for i in range(len(queue)):
                row, col = queue.popleft()
                for delta_row, delta_col in DIRECTIONS:
                    next_row = row + delta_row
                    next_col = col + delta_col
                    if 0 <= next_row <= len(rooms) - 1 and 0 <= next_col <= len(rooms[0]) - 1 and (next_row, next_col) not in visited and rooms[next_row][next_col] > 0:
                        queue.append((next_row, next_col))
                        visited.add((next_row, next_col))
                        rooms[next_row][next_col] = step

if __name__ == "__main__":
    walls_and_gates = WallsAndGates()
    rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    print(walls_and_gates.wallsAndGates(rooms))