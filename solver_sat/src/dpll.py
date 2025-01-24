def unit_propagation(cnf, assignments):
    """Realiza a propagação de unidade (se possível)."""
    while True:
        unit_clause = None
        for clause in cnf:
            if len(clause) == 1:  # Encontra uma cláusula unitária
                unit_clause = clause
                break
        if not unit_clause:
            break

        literal = unit_clause[0]
        # Atribui o valor ao literal como inteiro (-1 ou 1)
        assignments[abs(literal)] = 1 if literal > 0 else -1
        # Propaga a atribuição
        cnf = [clause for clause in cnf if literal not in clause]  # Remove cláusulas contendo o literal
        for i, clause in enumerate(cnf):
            cnf[i] = [x for x in clause if x != -literal]  # Remove literais opostos
    return cnf, assignments

def pure_literal_elimination(cnf, assignments):
    """Elimina literais puros (que só aparecem com um sinal em todas as cláusulas)."""
    literals = set(literal for clause in cnf for literal in clause)
    pure_literals = {literal for literal in literals if -literal not in literals}

    for literal in pure_literals:
        assignments[abs(literal)] = 1 if literal > 0 else -1
        cnf = [clause for clause in cnf if literal not in clause]
        for i, clause in enumerate(cnf):
            cnf[i] = [x for x in clause if x != -literal]
    return cnf, assignments

def dpll(cnf, assignments=None):
    if assignments is None:
        assignments = {}

    # Aplica simplificações
    cnf, assignments = unit_propagation(cnf, assignments)
    cnf, assignments = pure_literal_elimination(cnf, assignments)

    # Se todas as cláusulas foram satisfeitas, retornamos as atribuições
    if not cnf:
        return assignments

    # Se houver uma cláusula vazia, a fórmula é insatisfatível
    if any(len(clause) == 0 for clause in cnf):
        return None

    # Escolhe um literal não atribuído
    literal = next(abs(literal) for clause in cnf for literal in clause if abs(literal) not in assignments)

    # Tenta atribuir True ao literal
    new_cnf = [clause for clause in cnf if literal not in clause]
    for i, clause in enumerate(new_cnf):
        new_cnf[i] = [x for x in clause if x != -literal]

    result = dpll(new_cnf, {**assignments, literal: 1})
    if result is not None:
        return result

    # Se a atribuição para o literal como True falhou, tenta False
    new_cnf = [clause for clause in cnf if -literal not in clause]
    for i, clause in enumerate(new_cnf):
        new_cnf[i] = [x for x in clause if x != literal]

    return dpll(new_cnf, {**assignments, literal: -1})