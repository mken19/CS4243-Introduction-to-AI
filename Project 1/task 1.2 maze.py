import heapq

class Soa:
    def __init__(self, position, num_flash_left, is_flash, num_nuke_left, is_nuke):
        self.position = position
        self.num_flash_left = num_flash_left
        self.is_flash = is_flash
        self.num_nuke_left = num_nuke_left
        self.is_nuke = is_nuke
    def __eq__(self, other):
        if isinstance(other, Soa):
            return self.position == other.position and self.num_flash_left == other.num_flash_left and self.is_flash == other.is_flash and self.num_nuke_left == other.num_nuke_left and self.is_nuke == other.is_nuke
class Node:
    def __init__(self, soa, parent, g, f, action):
        self.soa = soa
        self.parent = parent
        self.g = g
        self.f = f
        self.action = action
    def __lt__(self, other):
        return self.f < other.f
    def get_path(self):
        path = []
        current = self
        while current:
            path.append(current.action)
            current = current.parent
        return path[::-1][1:]

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

## Helper function to calculate heuristic
def calc_h(x, y, goals):
    min_h = float('inf')
    for goal in goals:
        h = manhattan(x, y, goal[0], goal[1])
        h *= 2  ## Minimum cost for moving to the goal
        if h < min_h:
            min_h = h
    return min_h

def check_visited(visited, node):
    state = node.soa
    state_tuple = (state.position, state.num_flash_left, state.is_flash, state.num_nuke_left, state.is_nuke)
    if state_tuple in visited:
        if visited[state_tuple] > node.g:
            visited[state_tuple] = node.g
            return False
        else:
            return True
    else:
        return False
def search(dct):
    ## Initialize the variables from the dictionary
    rows, cols = dct["rows"], dct["cols"]
    num_flash_left, num_nuke_left = dct["num_flash_left"], dct["num_nuke_left"]
    start = tuple(dct["start"])
    goals = set(tuple(goal) for goal in dct["goals"])
    ## Initialize the maze
    maze = [ [0 for j in range(cols)] for i in range(rows) ]
    for x, y in dct["obstacles"]:
        maze[x][y] = -1
    for x, y, num in dct["creeps"]:
        maze[x][y] = num
    ## Initialize frontier, visited, nuke
    frontier = []
    visited = {}
    
    f = calc_h(start[0], start[1], goals)
    starting_state = Soa(start, num_flash_left, False, num_nuke_left, (None, None))
    starting_node = Node(starting_state, None, 0, f, None)
    heapq.heappush(frontier, starting_node)
    
    ## A* Search
    while frontier:
        current_node = heapq.heappop(frontier)
        current_state = current_node.soa
        if current_state.position in goals:
            return current_node.get_path()
        if check_visited(visited, current_node):
            continue
        visited[(current_state.position, current_state.num_flash_left, current_state.is_flash,
                  current_state.num_nuke_left, current_state.is_nuke)] = current_node.g
        ## Helper function to calc creep_cost based on NUKE effect
        def calc_creep_cost(x, y, nuke):
            if nuke != (None, None):
                if manhattan(x, y, nuke[0], nuke[1]) <= 10:
                    return 0
            return maze[x][y]

        def action(action):
            current_position = current_state.position
            dx, dy = 0, 0
            activate_flash, activate_nuke = False, False
            if (action == 0):
                dx = -1
            elif (action == 1):
                dx = 1
            elif (action == 2):
                dy = -1
            elif (action == 3):
                dy = 1
            elif (action == 4):
                activate_flash = True
            elif (action == 5):
                activate_nuke = True

            new_x, new_y = current_position[0], current_position[1]
            
            new_num_flash_left = current_state.num_flash_left
            new_is_flash = current_state.is_flash
            new_num_nuke_left = current_state.num_nuke_left
            new_is_nuke = current_state.is_nuke
            new_g = current_node.g
            new_f = current_node.f
            if not (activate_flash or activate_nuke):
                if ((0 <= new_x + dx < rows) and (0 <= new_y + dy < cols) and maze[new_x + dx][new_y + dy] >= 0):
                    if (current_state.is_flash == True):
                        while ((0 <= new_x + dx < rows) and (0 <= new_y + dy < cols) and maze[new_x + dx][new_y + dy] >= 0):
                            new_x += dx
                            new_y += dy
                            new_g += calc_creep_cost(new_x, new_y, new_is_nuke) + 2
                    else:
                        new_x += dx
                        new_y += dy
                        new_g += calc_creep_cost(new_x, new_y, new_is_nuke) + 4
                else:
                    return None
                new_is_flash = False
            elif activate_flash:
                new_num_flash_left -= 1
                new_is_flash = True
                new_g += 10
            elif activate_nuke:
                new_is_nuke = True
                new_num_nuke_left -= 1
                new_g += 50
                new_is_nuke = current_position
            new_position = (new_x, new_y)
            new_f = new_g + calc_h(new_x, new_y, goals)
            new_state = Soa(new_position, new_num_flash_left, new_is_flash, new_num_nuke_left, new_is_nuke)
            new_node = Node(new_state, current_node, new_g, new_f, action)
            if not check_visited(visited, new_node):
                heapq.heappush(frontier, new_node)
        for i in range(4):
            action(i)
        if current_state.is_flash == False:
            if current_state.num_flash_left > 0: ## FLASH not active
                action(4)
            ## NUKE not active
            if (current_state.num_nuke_left > 0):
                action(5)
    return []