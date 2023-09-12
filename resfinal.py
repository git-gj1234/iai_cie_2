def negate_literal(literal):
    if literal.startswith("~"):
        return literal[1:]
    else:
        return "~" + literal
    
def resolve(clause1, clause2):
    new_clause = []
    for literal1 in clause1:
        for literal2 in clause2:
            if literal1 == negate_literal(literal2):
                new_clause = [lit for lit in (clause1 + clause2) if lit != literal1 and lit != literal2]
                return new_clause

def resolution(premises, conclusion):
    premises.append(negate_literal(conclusion))
    clauses = [prem.split(" v ") for prem in premises]
    while True:
        new_clauses = []
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvent = resolve(clauses[i], clauses[j])
                if not resolvent:
                    return True # Empty clause, contradiction found
                new_clauses.append(resolvent)
        if any(new_clause == clause for new_clause in new_clauses for clause in clauses):
            return False # No more new clauses can be generated
        clauses += new_clauses


# Example premises and conclusion in CNF
premises = ["P v Q", "~P v R", "~Q v R"]
conclusion = "R"
result = resolution(premises, conclusion)
if result:
    print("Conclusion follows from the premises.")
else:
    print("Conclusion does not follow from the premises.")