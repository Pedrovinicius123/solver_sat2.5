import random, os

def generate_random_SAT(n_literals:int, n_clauses:int, n_literals_per_clause:int) -> list:
    literals = list(range(n_literals))[1:]
    literals.extend(list(map(lambda x:-x, literals)))

    SAT = []
    for i in range(n_clauses):
        clause = random.sample(literals, k=n_literals_per_clause)

        for item in clause:
            if -item in clause:
                clause.remove(-item)

        SAT.append(clause)
    return SAT

def read_cnf(filename:str):
    with open(os.path.join('samples', filename), 'r') as file:
        lines = file.readlines()
        SAT = []

        for line in lines:
            clause = list(map(int, line.split()))
            SAT.append(clause)

        return SAT
    