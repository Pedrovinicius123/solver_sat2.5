from template import Template, GeneralTemplate
import itertools, random, copy, time, pycosat
import numpy as np

def parse_formula(formula:list, assignments=[]):
    new_formula = []
    for C in formula:
        new_clause = []
        for comb in itertools.combinations(C, 2):
            new_clause.append(list(comb))

        new_formula.append(np.array(new_clause))

    return simplify(new_formula)  

def concatenate_boolean_array(A:np.ndarray, B:np.ndarray) -> np.ndarray:
    new_boolean = []

    for i in range(A.shape[0]):
        inner_boolean = []
        for j in range(B.T.shape[1]):
            inner_boolean.append(np.append(A[i], B[j]))

        new_boolean.append(inner_boolean)

    return new_boolean

def simplify(new_formula:list):
    arrangements = []
    for i in list(range(len(new_formula)))[::2]:
        arrangements.append(tuple(new_formula[i:i+2]))
    
    if len(arrangements) == 1:
        return new_formula

    concatenated = []
    print(arrangements)
    for A, B in arrangements:
      concatenated.append(concatenate_boolean_array(A, B))

    time.sleep(3)

    return simplify(np.array(concatenated))

def solve(formula:list):
    result = parse_formula(copy.deepcopy(formula))
    print(result)        

def test(assignments:list, formula:list):
    for C in formula:
        satisfied = False

        for literal in assignments:
            if literal in C:
                satisfied = True
                break

        if not satisfied:
            print(C)
            return False

    return True
