def solve_CSP(input):
    variables = input['domains'].keys()
    domains =  input['domains']
    constraints = input['constraints']
    def is_valid(assignment, var, value):
        for (var1, var2), constraint in constraints.items():
            if var1 == var and var2 in assignment and not constraint(value, assignment[var2]):
                return False
            if var2 == var and var1 in assignment and not constraint(assignment[var1], value):
                return False
        return True
    def select_unassigned_variable(assignment):
        unassigned = [v for v in variables if v not in assignment]
        return min(unassigned, key=lambda var: len(domains[var]))
    def forward_check(assignment, var):
        removed_values = {}
        is_zero = False
        for (var1, var2), constraint in constraints.items():
            i = 0
            if var1 == var and var2 not in assignment:
                removed_values[var2] = []
                while i < len(domains[var2]):
                    value = domains[var2][i]
                    if not constraint(assignment[var], value):
                        domains[var2].pop(i)
                        removed_values[var2].append(value)
                        continue
                    i += 1
            elif var2 == var and var1 not in assignment:
                removed_values[var1] = []
                while i < len(domains[var1]):
                    value = domains[var1][i]
                    if not constraint(value, assignment[var]):
                        domains[var1].pop(i)
                        removed_values[var1].append(value)
                        continue
                    i += 1
        return removed_values
    def restore_domains(removed_values):
        for var, values in removed_values.items():
            domains[var].extend(values)
    def backtrack(assignment):
        if len(assignment) == len(variables):
            return assignment
        var = select_unassigned_variable(assignment)
        for value in domains[var]:
            if is_valid(assignment, var, value):
                assignment[var] = value
                removed_values= forward_check(assignment, var)
                result = backtrack(assignment)
                if result is not None:
                    return result
                assignment.pop(var)
                restore_domains(removed_values)
        return None
    return backtrack({})