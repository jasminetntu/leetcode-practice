class Solution:

    from collections import defaultdict, deque

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # build list of counts of prereqs each course needs
        # build adj dict for what courses the prereq unlocks
        # keep track of courses in arr
        # add courses with no prereqs into queue
        # process each course -> add to arr -> unlock next courses -> add into queue
        # return arr if all prereqs have been taken, otherwise return empty

        prereqs = defaultdict(list)
        count_prereqs = [0] * numCourses
        for c, p in prerequisites:
            prereqs[p].append(c)
            count_prereqs[c] += 1
        
        toTake = deque()
        for i in range(len(count_prereqs)):
            if count_prereqs[i] == 0:
                toTake.append(i)
        
        res = []
        while toTake:
            curr = toTake.popleft()
            res.append(curr)

            for c in prereqs[curr]:
                count_prereqs[c] -= 1
                if count_prereqs[c] == 0:
                    toTake.append(c)
        
        return res if sum(count_prereqs) == 0 else []