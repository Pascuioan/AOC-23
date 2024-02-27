def true(*x):
    return True

def false(*x):
    return False

def functionBuilder(sign, val):
    if sign == "<":
        return lambda x : x < val
    return lambda x : x > val

def part1():
    parts = []
    workflows = {}
    readingWorkflows = True
    for line in open("input.txt"):
        if line == "\n":
            readingWorkflows = False
            continue
        
        if readingWorkflows:
            line = line.strip().split("{")
            workflowName = line[0]
            rules = []
            line = line[1].strip("}").split(",")
            for rule in line:
                rule = rule.split(":")
                if len(rule) == 1:
                    rules.append(rule[0])
                    continue
                rule, dest = rule[0], rule[1]
                component, sign, value = rule[0], rule[1], int(rule[2:]) 
                # if sign == "<":
                #     f = (lambda x : x < value)
                # else:
                #     f = (lambda x : x > value)
                f = functionBuilder(sign, value)
                rules.append((component, f, dest))
            
            workflows[workflowName] = rules
        else:
            line = line.strip("{}\n ").split(",")
            part = {}
            for ind, component in enumerate(line):
                match(ind):
                    case 0:
                        part["x"] = int(component[2:])
                    case 1:
                        part["m"] = int(component[2:])
                    case 2:
                        part["a"] = int(component[2:])
                    case 3:
                        part["s"] = int(component[2:])
            parts.append(part)

    # for w in workflows.values():
    #     for r in w:
    #         if not isinstance(r, str):
    #             print(r[1])
    # return
    sum = 0
    for part in parts:
        workflow = "in"
        accepted = False
        while True:
            for rule in workflows[workflow]:
                if isinstance(rule, str):
                    workflow = rule
                    break
                if rule[1](part[rule[0]]):
                    workflow = rule[2]
                    break
            
            if workflow == "A":
                accepted = True
                break
            if workflow == "R":
                accepted = False
                break
        
        if accepted == True:
            sum += part["x"] + part["m"] + part["a"] + part["s"]

    print(sum)
                
            
part1()