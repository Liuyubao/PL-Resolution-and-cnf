# Project 2
# Yubao Liu, Siqi Xiong, Xue Li
# Oct 13, 2018

def biCondElimination(s):
    if type(s) is str:
        return s
    elif s[0] == "iff":
        return(["and",
                ["if",
                 biCondElimination(s[1]),
                 biCondElimination(s[2])],
                ["if",
                 biCondElimination(s[2]),
                 biCondElimination(s[1])]])
    else:
        return([s[0]] + [biCondElimination(i) for i in s[1:]])

def impliElimination(s):
    if type(s) is str:
        return s
    elif s[0] == "if":
        return(["or",
                ["not",
                 impliElimination(s[1])],
                impliElimination(s[2])])
    else:
        return([s[0]] + [impliElimination(i) for i in s[1:]])

def twoNegElimination(s):
    if type(s) is str:
        return s
    elif s[0] == "not" and type(s[1]) is list and s[1][0] == "not":
        return(twoNegElimination(s[1][1]))
    else:
        return([s[0]] + [twoNegElimination(i) for i in s[1:]])

def demorgan(s):
    revision = demorgan1(s)
    if revision == s:
        return s
    else:
        return demorgan(revision)
    
def demorgan1(s):
    if type(s) is str:
        return s
    elif s[0] == "not" and type(s[1]) is list and s[1][0] == "and":
        return(["or"] + [demorgan(["not", i]) for i in s[1][1:]])
    elif s[0] == "not" and type(s[1]) is list and s[1][0] == "or":
        return(["and"] + [demorgan(["not", i]) for i in s[1][1:]])
    else:
        return ([s[0]] + [demorgan(i) for i in s[1:]])

def binaryize(s): 
    if type(s) is str:
        return s
    elif s[0] == "and" and len(s) > 3: 
        return(["and", s[1], binaryize(["and"] + s[2:])])
    elif s[0] == "or" and len(s) > 3:
        return(["or", s[1], binaryize(["or"] + s[2:])])
    else:
        return([s[0]] + [binaryize(i) for i in s[1:]])
    
def distrib(s):
    revision = distribOnBi(s)
    if revision == s:
        return s
    else:
        return distrib(revision)
    
def distribOnBi(s): 
    '''
    only works on binary connectives

    '''
    if type(s) is str:
        return s
    elif s[0] == "or" and type(s[1]) is list and s[1][0] == "and":
        # distribute s[2] over s[1]
        return(["and"] + [distrib(["or", i, s[2]]) for i in s[1][1:]])
    elif s[0] == "or" and type(s[2]) is list and s[2][0] == "and":
        # distribute s[1] over s[2]
        return(["and"] + [distrib(["or", i, s[1]]) for i in s[2][1:]])
    else:
        return ([s[0]] + [distrib(i) for i in s[1:]])

def andCombine(s):
    '''
    use and to combine

    '''
    revision = andCombine1(s)
    if revision == s:
        return s
    else:
        return andCombine(revision)
    
def andCombine1(s):
    if type(s) is str:
        return s
    elif s[0] == "and":
        result = ["and"]
        for i in s[1:]:
            if type(i) is list and i[0] == "and":
                result = result + i[1:]
            else:
                result.append(i)
        return result
    else:
        return([s[0]] + [andCombine1(i) for i in s[1:]])

def orCombine(s):
    '''
    use or to combine

    '''
    revision = orCombine1(s)
    if revision == s:
        return s
    else:
        return orCombine(revision)

def orCombine1(s):
    if type(s) is str:
        return s
    elif s[0] == "or":
        result = ["or"]
        for i in s[1:]:
            if type(i) is list and i[0] == "or":
                result = result + i[1:]
            else:
                result.append(i)
        return result
    else:
        return([s[0]] + [orCombine1(i) for i in s[1:]])


def duplicateLiteralsElination(s):
    if type(s) is str:
        return s
    if s[0] == "not":
        return s
    if s[0] == "and":
        return(["and"] + [duplicateLiteralsElination(i) for i in s[1:]])
    if s[0] == "or":
        remains = []
        for l in s[1:]:
            if l not in remains:
                remains.append(l)
        if len(remains) == 1:
            return remains[0]
        else:
            return(["or"] + remains)

def duplicateClausesElimination(s):
    if type(s) is str:
        return s
    if s[0] == "not":
        return s
    if s[0] == "or":
        return s
    if s[0] == "and": 
        remains = []
        for c in s[1:]:
            if unique(c, remains):
                remains.append(c)
        if len(remains) == 1:
            return remains[0]
        else:
            return(["and"] + remains)

def unique(c, remains):
    for p in remains:
        if type(c) is str or type(p) is str:
            if c == p:
                return False
        elif len(c) == len(p):
            if len([i for i in c[1:] if i not in p[1:]]) == 0:
                return False
    return True

# def removeNeg(s):
#     if type(s) == str:
#         return s
#     elif type(s) == list and len(s) >= 2:        
        

def cnf(s):
    s = biCondElimination(s)
    s = impliElimination(s)
    s = demorgan(s)
    s = twoNegElimination(s)
    s = binaryize(s)
    s = distrib(s)
    # print("before andCombine:", s)
    s = andCombine(s)
    # print("before orCombine:", s)
    s = orCombine(s)
    # print("after orCombine:", s)
    s = duplicateLiteralsElination(s)
    s = duplicateClausesElimination(s)
    return s



if __name__ == "__main__":

    sentences = ['and',
            ['not', 'P11'],
            ['iff', 'B11', ['or', 'P12', 'P21']],
            ['iff', 'B21', ['or', 'P11', 'P22', 'P31']],
            ['not', 'B11'],
            'B21',
            'P12']
    test = ['and', 'P12', ['or', ['not', 'P12'], 'P21']]
    testand = ['and', 'P12', ['and', ['not', 'P12'], 'P21']]
    # print(orCombine(testand))
    print(repr(cnf(testand)))


