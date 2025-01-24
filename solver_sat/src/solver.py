from template import Template, GeneralTemplate

def parse_formula(formula:list):
    general_templates = []
    for C in formula:
        for i in range(len(C)-1):
            general_temp = GeneralTemplate(C[i], C[i+1], [])
            temp = Template(C[i], C[i+1], [])

            if general_temp not in general_templates:
                general_templates.append(general_temp)

                if len(C) > 2:                        
                    general_temp.add_template(temp)
            
            elif len(C) > 2:                        
                general_templates[general_templates.index(general_temp)].add_template(temp)

    return general_templates

def solve(formula:list):
    general_templates = parse_formula(formula)
