class Solution:
    
    from collections import deque

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # go from the EDGES of the heights, not the center
        # traverse from lower to higher/equal levels
        # traverse from pacific first -> store each pos reached in set
        # do the same for atlantic in diff set
        # for coords that are in both sets, add to res

        # pacific -> r = 0 or c = 0
        # atlantic -> r = len(heights) - 1 or c = len(heights[0]) - 1


        # SETUP

        pacific = set()
        pacificQueue = deque()
        atlantic = set()
        atlanticQueue = deque()

        for i in range(len(heights)):
            pacificQueue.append((i, 0))
            pacific.add((i, 0))
            atlanticQueue.append((i, len(heights[0]) - 1))
            atlantic.add((i, len(heights[0]) - 1))
        for i in range(len(heights[0])):
            pacificQueue.append((0, i))
            pacific.add((0, i))
            atlanticQueue.append((len(heights) - 1, i))
            atlantic.add((len(heights) - 1, i))

        # PACIFIC
        while pacificQueue:
            r, c = pacificQueue.popleft()
            currHeight = heights[r][c]

            if r + 1 < len(heights) and (r + 1, c) not in pacific and heights[r + 1][c] >= currHeight:
                pacificQueue.append((r + 1, c))
                pacific.add((r + 1, c))
            
            if r - 1 >= 0 and (r - 1, c) not in pacific and heights[r - 1][c] >= currHeight:
                pacificQueue.append((r - 1, c))
                pacific.add((r - 1, c))
            
            if c + 1 < len(heights[0]) and (r, c + 1) not in pacific and heights[r][c + 1] >= currHeight:
                pacificQueue.append((r, c + 1))
                pacific.add((r, c + 1))
            
            if c - 1 >= 0 and (r, c - 1) not in pacific and heights[r][c - 1] >= currHeight:
                pacificQueue.append((r, c - 1))
                pacific.add((r, c - 1))

        # ATLANTIC
        while atlanticQueue:
            r, c = atlanticQueue.popleft()
            currHeight = heights[r][c]

            if r + 1 < len(heights) and (r + 1, c) not in atlantic and heights[r + 1][c] >= currHeight:
                atlanticQueue.append((r + 1, c))
                atlantic.add((r + 1, c))
            
            if r - 1 >= 0 and (r - 1, c) not in atlantic and heights[r - 1][c] >= currHeight:
                atlanticQueue.append((r - 1, c))
                atlantic.add((r - 1, c))
            
            if c + 1 < len(heights[0]) and (r, c + 1) not in atlantic and heights[r][c + 1] >= currHeight:
                atlanticQueue.append((r, c + 1))
                atlantic.add((r, c + 1))
            
            if c - 1 >= 0 and (r, c - 1) not in atlantic and heights[r][c - 1] >= currHeight:
                atlanticQueue.append((r, c - 1))
                atlantic.add((r, c - 1))

        # BUILT RES
        result = []
        for pos in pacific:
            if pos in atlantic:
                result.append(pos)

        return result