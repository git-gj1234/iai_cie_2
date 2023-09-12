def resolve(clause1, clause2):
    return [literal for literal in clause1 if -literal not in clause2] + [literal for literal in clause2 if -literal not in clause1]

def can_resolve(clause1, clause2):
    return any(-literal in clause2 for literal in clause1) or any(-literal in clause1 for literal in clause2)

def resolution(clauses):
    new_clauses = clauses.copy()
    while True:
        n = len(new_clauses)
        for i in range(n):
            for j in range(i + 1, n):
                if can_resolve(new_clauses[i], new_clauses[j]):
                    resolvent = resolve(new_clauses[i], new_clauses[j])
                    if not resolvent:
                        return True  # Contradiction found
                    if resolvent not in new_clauses:
                        new_clauses.append(resolvent)
        if len(new_clauses) == n:
            return False  # No new clauses can be generated

# Example usage
clauses = [[-1, 2], [-1, 2], [-1, 2],[-1, 2]]
result = resolution(clauses)
print("The clauses are unsatisfiable (contradictory)." if result else "The clauses are satisfiable.")
