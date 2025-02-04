class Solution:
    def findOrder(
        self,
        numCourses: int,
        prerequisites: list[list[int]],
    ) -> list[int]:
        def dfs(vertex: int):
            if color[vertex] == 2:
                return False
            if color[vertex] == 1:
                return True

            color[vertex] = 1
            for child in adj[vertex]:
                if dfs(child):
                    return True

            color[vertex] = 2
            stack.append(vertex)

            return False

        adj = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            adj[i].append(j)

        color = [0 for _ in range(len(adj))]
        stack = []
        for vertex in range(len(adj)):
            if dfs(vertex):
                return []

        ## Мы не делаем реверс, потому что узлы по условию сразу расположены в обратном порядке
        return stack


if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(Solution().findOrder(numCourses, prerequisites))
