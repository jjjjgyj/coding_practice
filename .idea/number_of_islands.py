from collections import deque
class Practice:
    def num_islands(self, grid):
        res = 0
        queue = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    res += 1
                    queue.append((i, j))
                    visited.add((i, j))
                    self.find_island(grid, i, j, queue, visited)
        return res

    def find_island(self, grid, row, col, queue, visited):
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            row, col = queue.popleft()
            for delta_row, delta_col in DIRECTIONS:
                next_row = row + delta_row
                next_col = col + delta_col
                if 0 <= next_row <= len(grid) - 1 and 0 <= next_col <= len(grid[0]) - 1 and (next_row, next_col) not in visited and grid[next_row][next_col] == "1":
                    queue.append((next_row, next_col))
                    visited.add((next_row, next_col))

if __name__ == "__main__":
    practice = Practice()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    grid_2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print(practice.num_islands(grid))
    print(practice.num_islands(grid_2))
    print(__name__, type(__name__), type(Practice), type(practice), type(practice.num_islands(grid)))