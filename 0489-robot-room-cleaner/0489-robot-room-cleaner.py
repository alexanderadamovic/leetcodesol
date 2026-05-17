class Solution:
    def cleanRoom(self, robot):
        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def dfs(row, col, direction):
            robot.clean()
            visited.add((row, col))
            
            for i in range(4):
                new_dir = (direction + i) % 4
                new_row = row + directions[new_dir][0]
                new_col = col + directions[new_dir][1]
                
                if (new_row, new_col) not in visited and robot.move():
                    dfs(new_row, new_col, new_dir)
                    go_back()
                
                robot.turnRight()
        
        dfs(0, 0, 0)
        