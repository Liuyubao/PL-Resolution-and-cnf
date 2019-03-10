# Project 2
# Yubao Liu
# Oct 13, 2018

import cnf
import time

class KnowledgeBase:
    '''
    A KnowledgeBase for Propositional logic.

    '''
    def __init__(self, sentence = None):
        self.clauses = []
        self.detailsTurn = False    # print the algorithm details or not 
        if sentence:
            self.tell(sentence)

    def tell(self, sentence):
        '''
        Add the sentence to KnowledgeBase
        also reduce it to smallest structure

        '''
        self.clauses.extend(disCombine('and', cnf.cnf(sentence)))

# ______________________________________________________________________________
# Truth table enumeration method


def combine(op, elements):
    '''
    return the combination of elements using operation op

    '''
    if len(elements) == 0:
        return elements
    elif len(elements) == 1:
        return elements[0]
    elif op == 'and':
        return ['and'] + elements
    elif op == 'or':
        return ['or'] + elements

def disCombine(op, clause):
    '''
    return the discombination(list) of clause using operation op

    '''
    result = []
    if type(clause) == str:
        return [clause]
    elif len(clause) <= 2:    # P or not P, just return self
        return [clause]
    elif op == clause[0]:
        return clause[1:]
    else:
        return [clause]


def tTEntails(kb, alpha):
    '''
    returns if KB entailments alpha True or False using truth table
    kb: KnowledgeBase
    alpha: the result to prove

    '''
    clauses = kb.clauses + disCombine('and', cnf.cnf(alpha))
    symbols = propSymbols(combine('and', clauses))

    return tTCheckAll(kb, alpha, symbols, {})

call_times = 0

def tTCheckAll(kb, alpha, symbols, model):
    '''
    help to implement tTEntails
    model is a dictionary such as {'P': True, "Q": False}

    '''

    if len(symbols) == 0:
        alphaCnf = cnf.cnf(alpha)
        # print("kb:", kb.clauses)
        if kb.detailsTurn:
            print("model:", model)
            print("result:", plTrue(alphaCnf, model))
        # print("\n")
        # global call_times
        # print("call_times:", call_times)
        # call_times+=1
        if plTrue(cnf.cnf(combine('and', kb.clauses)), model):
            return plTrue(alphaCnf, model)
        else:
            return True     # when KB is false, always return True
    else:
        p, rest = symbols[0], symbols[1:]
        return (tTCheckAll(kb, alpha, rest, modelExtend(model, p, True)) and tTCheckAll(kb,alpha, rest, modelExtend(model, p, False)))



def plTrue(clause, model = {}):
    '''
    Return True if the clause is true in the model, and False if it is false.
    Return None if the model does not specify all symbols

    '''
    assert len(model) > 0, 'the length of model should be more than 0'
    assert len(clause) > 0, 'the length of clause should be more than 0'
    if type(clause) == str:
        return model[clause]
    elif len(clause) >=2:   # must be the type of list
        if clause[0] == 'not':
            return not plTrue(clause[1], model)
        elif clause[0] == 'and':
            clauseRest = combine('and', clause[2:])
            if len(clauseRest) == 0:    # if operation is 'and', remove the influence of []
                return plTrue(clause[1], model)
            else:
                return plTrue(clause[1], model) and plTrue(clauseRest, model)
        elif clause[0] == 'or':
            clauseRest = combine('or', clause[2:])
            if len(clauseRest) == 0:
                return plTrue(clause[1], model)
            else:
                return plTrue(clause[1], model) or plTrue(clauseRest, model)


def propSymbols(clause):
    '''
    Return the list of all propositional symbols in cnfClause.

    '''
    if len(clause) == 0:
        return []
    elif type(clause) == str:
        return [clause]
    elif len(clause) <= 2:   # P or not P, just return self
        return [clause[-1]]
    else:
        rtSymbols = []
        for s in clause[1:]:
            pI = propSymbols(s)
            rtSymbols.extend(list(set(pI)))
        return list(set(rtSymbols))

# ______________________________________________________________________________
# PL resolution method

def modelExtend(model, p, v):
    '''
    Return the new model with p values v added

    '''
    model2 = model.copy()
    model2[p] = v
    return model2

def duplicateOrElemination(clauses):
    '''
    Eleminate the duplicate item in or clause
    eg: ['or', 'P', ['not', 'P']] return []

    '''
    if type(clauses) == str or len(clauses) <= 1:
        return clauses
    else:
        for item in clause:
            if negativeInside(item) in clause:
                return []
    return clauses

def orContainTautology(clause):
    '''
    return if the or clause contain the tautology
    eg: ['P', ['not', 'P']]

    '''
    if type(clause) == str or len(clause) <= 1:
        return False
    else:
        for item in clause:
            if negativeInside(item) in clause:
                return True
    return False

def subSumption(clauses):
    '''
    return if the or clause contain the tautology
    eg: ['P', ['and', 'P', "Q"]] return ['P']

    '''
    unitClauses = [item for item in clauses if type(item) == str or (type(item) == list) and len(item) == 2]
    print("unitClauses:", unitClauses)
    print("before sub:", clauses)
    for cc in clauses:
        for unitC in unitClauses:
            if type(cc) == list and len(cc) >2:
                if unitC in disCombine('or', cc) and cc in clauses:
                    clauses.remove(cc)
    print("After sub:", clauses)




def plResolution(kb, alpha):
    '''
    returns if KB entailments alpha True or False using pl resolution
    kb: KnowledgeBase
    alpha: the result to prove

    '''
    clauses = kb.clauses + disCombine('and', cnf.cnf(negativeInside(alpha)))
    # clauses = duplicateOrElemination(clauses)
    # if str(clauses) == list and len(clauses) == 0:
    #     return True
    newList = []
    while True:
        
        # subSumption(clauses)
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i+1, n)]
        for (ci, cj) in pairs:
            resolvents = plResolve(ci, cj)
            if kb.detailsTurn:
                print("After doing resolution for %s and %s we get %s" % (ci, cj, resolvents))
            if [] in resolvents:
                return True
            for tempCR in resolvents:
                if not tempCR in newList:
                    newList.append(tempCR)
            # newList = toUnique(newList + resolvents)
        #     print("newList:", newList)
        # print("clauses:", clauses)
        newList = [cc for cc in newList if not orContainTautology(cc)]
        # subSumption(newList)
        if isSublistOf(newList, clauses):
            return False
        for cc in newList:
            if not cc in clauses:
                clauses.append(cc)
        # clauses = toUnique(clauses + newList)




gloVar = 0  #   used to compute the excute times

def plResolve(ci, cj):
    '''
    returns all clauses that can be obtained from clauses ci and cj

    '''
    clauses = []
    for di in disCombine('or', ci):
        for dj in disCombine('or',cj):
            if di == negativeInside(dj) or negativeInside(di) == dj:
                # global gloVar
                # if gloVar % 10 == 0:
                #     print("times: ", gloVar)
                #     print("ci is %s, and cj is %s" % (ci, cj))
                # gloVar += 1
                diNew = disCombine('or', ci)
                diNew.remove(di)
                djNew = disCombine('or', cj)
                djNew.remove(dj)
                # print("diNew:", diNew)
                # print("djNew:", djNew)
                dNew = diNew + djNew
                dNew = toUnique(dNew)
                # print("dNew:", dNew)
                toAddD = combine('or', dNew)
                # print("toAddD:", toAddD)
                clauses.append(toAddD)
    return clauses



def negativeInside(s):
    '''
    move negation sign inside s

    '''
    if type(s) == str:
        return ['not', s]
    elif s[0] == 'not':
        return s[1]
    elif s[0] == 'and':
        tempRet = ['or']
        for element in s[1:]:
            tempRet.append(negativeInside(element))
        return tempRet
    elif s[0] == 'or':
        tempRet = ['and']
        for element in s[1:]:
            tempRet.append(negativeInside(element))
        return tempRet

def toUnique(clauses):
    '''
    return a clauses list whose elements are unique


    '''
    if type(clauses) == str:
        return clauses
    if len(clauses) == 0:
        return clauses
    retClauses = []

    strElementList = list(set([str(element) for element in clauses]))


    for element2 in strElementList:
        if '[' in element2:
            retClauses.append(eval(element2))
        else:
            retClauses.append(element2)
    return retClauses



def isSublistOf(l1, l2):
    '''
    return if l1 is sublist of l2

    '''
    for element in l1:
        if not element in l2:
            return False
    return True


# ______________________________________________________________________________
# WaklSAT method

import random

def walkSAT(clauses, p = 0.5, maxFlips = 10000):
    '''
    returns every symbols' result by randomly flipping values of variables for maxFlips times and check its satisfiability
    clauses: the clauses to check
    p: the probability of flipping the value of the symbol
    maxFlip: maximum flipping time

    '''
    symbols = propSymbols(combine('and', clauses))
    print("symbols: ", symbols)

    model = {s: random.choice([True, False]) for s in symbols}
    for i in range(maxFlips):
        print("running time:", i)
        satisfied, unsatisfied = [], []
        for clause in clauses:
            if plTrue(clause, model):
                satisfied.append(clause)
            else:
                unsatisfied.append(clause)
        if len(unsatisfied) == 0: # if model satisfied all the clauses
            return model
        clause = random.choice(unsatisfied)
        if p > random.uniform(0.0, 1.0):
            sym = random.choice(list(propSymbols(clause)))
        else:
            def sat_count(sym):
                # Return the number of clauses satisfied after flipping the symbol.
                model[sym] = not model[sym]
                count = len([clause for clause in clauses if plTrue(clause, model)])
                model[sym] = not model[sym]
                return count
            sym = max(propSymbols(clause), key = sat_count)
        model[sym] = not model[sym]
    # Return None if no solution is found within the flip limit
    return None





# "not"   negation
# "and"   conjunction
# "or"    disjunction
# "if"    implication
# "iff"   biconditional implication
