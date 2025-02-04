class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: list[list[int]],
    ) -> bool:
        def dfs(vertex: int) -> bool:
            if color[vertex] == 1:
                return True
            if color[vertex] == 2:
                return False

            color[vertex] = 1
            for child_vertex in adj[vertex]:
                if dfs(child_vertex):
                    return True

            color[vertex] = 2
            return False

        adj = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            adj[i].append(j)

        color = [0 for _ in range(numCourses)]
        for vertex in range(len(adj)):
            if dfs(vertex):
                return False
        return True


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]
    print(Solution().canFinish(numCourses, prerequisites))
