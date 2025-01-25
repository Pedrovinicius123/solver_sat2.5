from template import Template, GeneralTemplate
from dpll import dpll
import itertools, random, copy, time

def parse_formula(formula:list):
    general_templates = []
    for C in formula:
        for i in range(len(C)-1):
            general_temp = GeneralTemplate(C[i], C[i+1], [])
            anterior_temp = Template(C[i], C[i+1], [])

            if general_temp not in general_templates:
                general_templates.append(general_temp)

                if len(C) > 2:                        
                    general_temp.add_template(anterior_temp)
            
            elif len(C) > 2:                  
                general_templates[general_templates.index(general_temp)].add_template(anterior_temp)

    return general_templates

def eliminate_contradiction(result:list):
    final_result = []
    for item in result:
        if -item in result:
            result.remove(-item)

        else:
            final_result.append(item)

    return final_result

def solve(formula:list):
    general_templates = parse_formula(formula)
    general_templates_options = copy.deepcopy(general_templates)

    result = None
    cond = True

    for temp in general_templates_options:
        result = create_connections(formula, temp, general_templates)    
        res = eliminate_contradiction(result)
        cond = test(res, formula)

        if cond:
            return list(set(res))

    if not cond:
        return 'UNSAT'

def create_connections(formula:list, initial_template:GeneralTemplate, general_templates:list, res=[]):
    if any(general_templates):
        if len(initial_template.sub_templates) == 4:
            temp = random.choice(initial_template.sub_templates)
            print(temp)
            for C in formula:
                if temp.a in C:
                    C.remove(temp.a)

                elif temp.b in C:
                    C.remove(temp.b)

            result = None
            general_templates = parse_formula(formula)

            if any(general_templates):
                result = create_connections(copy.deepcopy(formula), random.choice(general_templates), general_templates)

            if not result:
                initial_template.sub_templates.remove(temp)
                return create_connections(copy.deepcopy(formula), initial_template, general_templates)
            
            else:
                initial_template.sub_templates.remove(temp)
                res.extend(result)
                return res

        elif len(initial_template.sub_templates) == 0:
            if initial_template in general_templates:
                general_templates.remove(initial_template)

            if any(general_templates):
                create_connections(copy.deepcopy(formula), random.choice(general_templates), general_templates, res)   

        else:
            resolution = dpll(initial_template.to_cnf())
            assignments = []

            for key, value in resolution.items():
                assignments.append(key*value)

            res.extend(assignments)

            for literal in assignments:
                for C in formula:
                    if literal in C:
                        formula.remove(C)

                    elif -literal in C:
                        C.remove(-literal)

            general_templates = parse_formula(formula)

            if any(general_templates):
                create_connections(copy.deepcopy(formula), random.choice(general_templates), general_templates, res)
        
        return res

    else:
        return False

def test(assignments:list, formula:list):
    for C in formula:
        satisfied = False

        for literal in assignments:
            if literal in C:
                satisfied = True
                break

        if not satisfied:
            return False

    return True

