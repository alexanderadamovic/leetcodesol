class Solution:
    def numberOfCleanRooms(self, room):
        rows, cols = len(room), len(room[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c, d = 0, 0, 0
        cleaned = set()
        visited = set()

        while (r, c, d) not in visited:
            visited.add((r, c, d))
            cleaned.add((r, c))
            nr, nc = r + dirs[d][0], c + dirs[d][1]
            if 0 <= nr < rows and 0 <= nc < cols and room[nr][nc] == 0:
                r, c = nr, nc
            else:
                d = (d + 1) % 4

        return len(cleaned)