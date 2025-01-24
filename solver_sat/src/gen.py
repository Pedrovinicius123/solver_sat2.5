import random

def generate_random_SAT(n_literals:int, n_clauses:int, n_literals_per_clause:int) -> list:
    literals = list(range(n_literals))
    literals.extend(list(map(lambda x:-x, literals)))

    SAT = []
    for i in range(n_clauses):
        clause = random.sample(literals, k=n_literals_per_clause)

        for item in clause:
            if -item in clause:
                clause.remove(-item)

        SAT.append(clause)
    return SAT
    