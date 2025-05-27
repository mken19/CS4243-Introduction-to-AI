## BFS

def bfs_search(dct) -> List[Tuple[int, int]]:
    rows, cols = dct["rows"], dct["cols"]
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    obstacles = [[0]*cols for _ in range(rows)]
    for obstacle in dct["obstacles"]:
        x, y = obstacle
        obstacles[x][y] = 1
    visited = [[0]*cols for _ in range(rows)]
    start = tuple(dct["start"])
    goals = set(tuple(goal) for goal in dct["goals"])

    if obstacles[start[0]][start[1]] == 1:
        return []
    
    reachable = False
    for goal in goals:
        if obstacles[goal[0]][goal[1]] == 0:
            reachable = True
            break
    if reachable == False:
        return []

    frontier = deque([start])
    parent = {}
    parent[start] = None
    while frontier:
        current = frontier.popleft()
        if current in goals:
            path = []
            while current is not None:
                path.append(current)
                current = parent.get(current)
            return path[::-1]
        x, y = current
        visited[x][y] = 1
        for move in moves:
            nextX, nextY = x + move[0], y + move[1]
            nextState = (nextX, nextY)
            if 0 <= nextX < rows and 0 <= nextY < cols and obstacles[nextX][nextY] == 0 and visited[nextX][nextY] == 0:
                parent[nextState] = current
                frontier.append(nextState)
    return []