class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(queue):
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            print(f"queue is : {queue}")

            while len(queue) > 0:
                r, c = queue.pop(0)
                visited[r][c] = 1
 
                for direction in directions:
                    row = r + direction[0]
                    col = c + direction[1]
                    
                    # Skip out of bounds index
                    if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])):
                        continue
                    
                    # Skip already visited index
                    if visited[row][col] == 1:
                        continue
                    
                    # Visite a new island
                    if grid[row][col] == "1":
                        queue.append((row,col))


        visited = [[0 for _ in grid[0]] for _ in grid]
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # Dont double check one node
                if visited[r][c] == 0:
                    # Start breadth first search when an island has been targetted
                    if grid[r][c] == "1":
                        print(f"about to trigger bfs with {(r,c)}")
                        bfs([(r,c)])
                        count += 1
        return count


        






                    