def solve_CSP(input_dict):
    cols = input_dict["cols"]
    rows = input_dict["rows"]
    input_squares = input_dict["input_squares"]
    obstacles = input_dict["obstacles"]
    
    def initialize_domain(square_size, rows, cols, obstacles):
        # Calculate the domain based on rows, cols, size, and obstacles
        domain = []
        for r in range(rows - square_size + 1):
            for c in range(cols - square_size + 1):
                # Check if any square in the domain overlaps with obstacles
                overlaps = any((r + i, c + j) in obstacles for i in range(square_size) for j in range(square_size))
                if not overlaps:
                    domain.append((r, c))
        return domain

    def get_unassigned_variable(domains, ordered_square_size):
        for square_size in ordered_square_size:
            if square_size in domains:
                if input_squares[square_size] > 0:
                    return square_size

    def assign(board, square_size, pos, assignment):
        for i in range(pos[0], pos[0] + square_size):
            for j in range(pos[1], pos[1] + square_size):
                board[i][j] += 1
        assignment.append([square_size, pos[0], pos[1]])
        input_squares[square_size] -= 1
        return assignment, board

    def unassign(board, square_size, pos, assignment):
        for i in range(pos[0], pos[0] + square_size):
            for j in range(pos[1], pos[1] + square_size):
                board[i][j] -= 1
        assignment.remove([square_size, pos[0], pos[1]])
        input_squares[square_size] += 1
        return assignment, board

    def is_consistent(square_size, pos, board):
        for r in range(pos[0], pos[0] + square_size):
            for c in range(pos[1], pos[1] + square_size):
                if board[r][c] != 0:
                    return False
        return True

    def find_position(assignment, rows, cols, obstacles):
        coordinates = [[r, c] for r in range(rows) for c in range(cols)]
        for square in assignment:
            square_size, row, col = square
            for i in range(row, row + square_size):
                for j in range(col, col + square_size):
                    coordinates.remove([i, j])
        # Remove obstacles
        obstacles_lists = [list(t) for t in obstacles]
        positions = [position for position in coordinates if position not in obstacles_lists]
        return positions

    def backtrack(assignment, total_number_of_squares, number_of_unit_squares, board, prev_var):
        # goal check
        if len(assignment) == total_number_of_squares - number_of_unit_squares:
            positions = find_position(assignment, rows, cols, obstacles)
            # Append unit squares into assignment
            for position in positions:
                assignment.append([1, position[0], position[1]])
            # Use a nested list comprehension to convert each element (list) to a tuple
            assignment_tuples = [tuple(sublist) for sublist in assignment]
            return assignment_tuples

        var = get_unassigned_variable(domains, ordered_square_size) # choose variable to assign value to
        for coordinates in domains[var]:
            if is_consistent(var, coordinates, board):
                assignment, current_board = assign(board, var, coordinates, assignment)
                prev_var = var
                result = backtrack(assignment, total_number_of_squares, number_of_unit_squares, board, prev_var)
                if result != None:
                    return result
                assignment, board = unassign(board, var, coordinates, assignment)
        return None

    ordered_square_size = sorted(list(input_squares.keys()), reverse = True)
    assignment = []
    domains = {}
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    for row, col in obstacles:
        board[row][col] = 1
    number_of_unit_squares = 0
    total_number_of_squares = 0
    for square_size, num_left in input_squares.items():
        if square_size != 1:
            domains[square_size] = initialize_domain(square_size, rows, cols, obstacles)
            total_number_of_squares += num_left
        else:
            number_of_unit_squares = num_left
            total_number_of_squares += number_of_unit_squares

    return backtrack(assignment, total_number_of_squares, number_of_unit_squares, board, None)