from collections import deque

def bfs(adj):
    V = len(adj)
    visited = [False] * V
    res = []
    src = 0
    q = deque()
    visited[src] = True
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

    return res


def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


if __name__ == "__main__":
    V = 5
    adj = []
    for i in range(V):
        adj.append([])

    addEdge(adj, 1, 2)
    addEdge(adj, 1, 0)
    addEdge(adj, 2, 0)
    addEdge(adj, 2, 3)
    addEdge(adj, 2, 4)

    res = bfs(adj)
    for node in res:
        print(node, end=" ")

    print("\n")

    # ---------------- Water Jug DFS ----------------

    def water_jug_dfs(capacity1, capacity2, target):
        visited = set()
        path = []

        def dfs(jug1, jug2):
            if (jug1, jug2) in visited:
                return False

            visited.add((jug1, jug2))
            path.append((jug1, jug2))

            if jug1 == target or jug2 == target:
                return True

            # Fill Jug1
            if dfs(capacity1, jug2):
                return True

            # Fill Jug2
            if dfs(jug1, capacity2):
                return True

            # Empty Jug1
            if dfs(0, jug2):
                return True

            # Empty Jug2
            if dfs(jug1, 0):
                return True

            # Pour Jug1 -> Jug2
            if dfs(max(0, jug1 - (capacity2 - jug2)),
                   min(capacity2, jug1 + jug2)):
                return True

            # Pour Jug2 -> Jug1
            if dfs(min(capacity1, jug1 + jug2),
                   max(0, jug2 - (capacity1 - jug1))):
                return True

            path.pop()
            return False

        dfs(0, 0)
        return path

    capacity1 = 3
    capacity2 = 5
    target = 4

    solution = water_jug_dfs(capacity1, capacity2, target)

    if solution:
        print("Solution steps:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")
