# PL Resolution and cnf

    Yubao Liu
    Oct 13, 2018

### 1.What I did?
* implemented truth table enumeration method
* implemented PL resolution method
* improved PL resolution
* implemented WalkSAT method
* implemented cnf
* all codes on working out problems 3, 4, 5, 6
* researches on SATplan algorithm about last 2 problem



### 2. Environment:

    python3.6.7

### 3. Components:
* algorithm.py  --  all the algorithms implemented
* cnf.py        --  inplements about cnf
* problem1-6.py --  details about each problem

### 4. Problems results
#### 4.1 Problem 1 Modus Ponens
    python3 problem1.py
    ********KnowledgeBase for problem1 ********
    P
    ['or', ['not', 'P'], 'Q']


    ********The result Using truth table ********
    model: {'Q': True, 'P': True}
    result: True
    model: {'Q': True, 'P': False}
    result: True
    model: {'Q': False, 'P': True}
    result: False
    model: {'Q': False, 'P': False}
    result: False
    ******** Result: Q can  be entailed by the knowledgebase of problem1


    ********The result Using pl resolution ********
    After doing resolution for P and ['or', ['not', 'P'], 'Q'] we get ['Q']
    After doing resolution for P and ['not', 'Q'] we get []
    After doing resolution for ['or', ['not', 'P'], 'Q'] and ['not', 'Q'] we get [['not', 'P']]
    After doing resolution for P and ['or', ['not', 'P'], 'Q'] we get ['Q']
    After doing resolution for P and ['not', 'Q'] we get []
    After doing resolution for P and Q we get []
    After doing resolution for P and ['not', 'P'] we get [[]]
    ******** Result: Q can  be entailed by the knowledgebase of problem1
#### 4.2 Problem 2 Wumpus world
    python3 problem2.py
    ********KnowledgeBase for problem2 ********
    ['not', 'P11']
    ['or', ['not', 'B11'], 'P12', 'P21']
    ['or', ['not', 'P12'], 'B11']
    ['or', ['not', 'P21'], 'B11']
    ['or', ['not', 'B21'], 'P11', 'P22', 'P31']
    ['or', ['not', 'P11'], 'B21']
    ['or', ['not', 'P22'], 'B21']
    ['or', ['not', 'P31'], 'B21']
    ['not', 'B11']
    B21


    ********The result Using truth table ********
    ******** Result: ['not', 'P12'] can  be entailed by the knowledgebase of problem2


    ********The result Using pl resolution ********
    ******** Result: ['not', 'P12'] can  be entailed by the knowledgebase of problem2
#### 4.3 Problem 3 Wumpus world
    python3 problem3.py
    ********KnowledgeBase for problem3 ********
    ['or', ['not', 'mythical'], 'immortal']
    ['or', 'mortal', 'mythical']
    ['or', 'mammal', 'mythical']
    ['or', ['not', 'immortal'], 'horned']
    ['or', ['not', 'mammal'], 'horned']
    ['or', ['not', 'horned'], 'magical']


    ********The result Using truth table ********
    ******** Result: mythical can not be entailed by the knowledgebase of problem3
    ******** Result: ['not', 'mythical'] can not be entailed by the knowledgebase of problem3
    ******** Result: magical can  be entailed by the knowledgebase of problem3
    ******** Result: horned can  be entailed by the knowledgebase of problem3


    ********The result Using pl resolution ********
    ******** Result: mythical can not be entailed by the knowledgebase of problem3
    ******** Result: ['not', 'mythical'] can not be entailed by the knowledgebase of problem3
    ******** Result: magical can  be entailed by the knowledgebase of problem3
    ******** Result: horned can  be entailed by the knowledgebase of problem3
#### 4.4 Problem 4 Liars and Truth-tellers
    python3 problem4.py
    ********KnowledgeBase for problem4a ********
    ['or', 'C', ['not', 'A']]
    ['or', 'A', ['not', 'A']]
    ['or', 'A', ['not', 'C'], ['not', 'A']]
    ['or', ['not', 'B'], ['not', 'C']]
    ['or', 'B', 'C']
    ['or', ['not', 'C'], 'B']
    ['or', ['not', 'B'], 'C']
    C


    ********The result Using truth table ********
    ******** Result: A can  be entailed by the knowledgebase of problem4a
    ******** Result: B can  be entailed by the knowledgebase of problem4a
    ******** Result: C can  be entailed by the knowledgebase of problem4a


    ********The result Using pl resolution ********
    ******** Result: A can  be entailed by the knowledgebase of problem4a
    ******** Result: B can  be entailed by the knowledgebase of problem4a
    ******** Result: C can  be entailed by the knowledgebase of problem4a


    ********KnowledgeBase for problem4b ********
    ['or', ['not', 'A'], ['not', 'C']]
    ['or', 'A', 'C']
    ['or', 'A', ['not', 'B']]
    ['or', 'C', ['not', 'B']]
    ['or', 'B', ['not', 'A'], ['not', 'C']]
    ['or', ['not', 'C'], 'B']
    ['or', 'C', ['not', 'B']]


    ********The result Using truth table ********
    ******** Result: A can  be entailed by the knowledgebase of problem4b
    ******** Result: B can not be entailed by the knowledgebase of problem4b
    ******** Result: ['not', 'B'] can  be entailed by the knowledgebase of problem4b
    ******** Result: C can not be entailed by the knowledgebase of problem4b
    ******** Result: ['not', 'C'] can  be entailed by the knowledgebase of problem4b


    ********The result Using pl resolution ********
    ******** Result: A can  be entailed by the knowledgebase of problem4b
    ******** Result: B can not be entailed by the knowledgebase of problem4b
    ******** Result: ['not', 'B'] can  be entailed by the knowledgebase of problem4b
    ******** Result: C can not be entailed by the knowledgebase of problem4b
    ******** Result: ['not', 'C'] can  be entailed by the knowledgebase of problem4b
#### 4.5 Problem 5 Problem 5 More Liars and Truth-tellers
    python3 problem5.py
    ********KnowledgeBase for problem5 ********
    ['or', 'H', ['not', 'A']]
    ['or', 'I', ['not', 'A']]
    ['or', 'A', ['not', 'H'], ['not', 'I']]
    ['or', 'A', ['not', 'B']]
    ['or', 'L', ['not', 'B']]
    ['or', 'B', ['not', 'A'], ['not', 'L']]
    ['or', 'B', ['not', 'C']]
    ['or', 'G', ['not', 'C']]
    ['or', 'C', ['not', 'B'], ['not', 'G']]
    ['or', 'E', ['not', 'D']]
    ['or', 'L', ['not', 'D']]
    ['or', 'D', ['not', 'E'], ['not', 'L']]
    ['or', 'C', ['not', 'E']]
    ['or', 'H', ['not', 'E']]
    ['or', 'E', ['not', 'C'], ['not', 'H']]
    ['or', 'D', ['not', 'F']]
    ['or', 'I', ['not', 'F']]
    ['or', 'F', ['not', 'D'], ['not', 'I']]
    ['or', ['not', 'E'], ['not', 'G']]
    ['or', ['not', 'J'], ['not', 'G']]
    ['or', 'G', 'E', 'J']
    ['or', ['not', 'F'], ['not', 'H']]
    ['or', ['not', 'K'], ['not', 'H']]
    ['or', 'H', 'F', 'K']
    ['or', ['not', 'G'], ['not', 'I']]
    ['or', ['not', 'K'], ['not', 'I']]
    ['or', 'I', 'G', 'K']
    ['or', ['not', 'A'], ['not', 'J']]
    ['or', ['not', 'C'], ['not', 'J']]
    ['or', 'J', 'A', 'C']
    ['or', ['not', 'D'], ['not', 'K']]
    ['or', ['not', 'F'], ['not', 'K']]
    ['or', 'K', 'D', 'F']
    ['or', ['not', 'B'], ['not', 'L']]
    ['or', ['not', 'J'], ['not', 'L']]
    ['or', 'L', 'B', 'J']


    ********The result Using truth table ********
    ******** Result: A can not be entailed by the knowledgebase of problem5
    ******** Result: ['not', 'A'] can  be entailed by the knowledgebase of problem5
    ******** Result: B can not be entailed by the knowledgebase of problem5
    ******** Result: ['not', 'B'] can  be entailed by the knowledgebase of problem5
    ******** Result: C can not be entailed by the knowledgebase of problem5
    ******** Result: ['not', 'C'] can  be entailed by the knowledgebase of problem5
    ******** Result: D can not be entailed by the knowledgebase of problem5
    ******** Result: ['not', 'D'] can  be entailed by the knowledgebase of problem5
    ******** Result: E can not be entailed by the knowledgebase of problem5
    ******** Result: ['not', 'E'] can  be entailed by the knowledgebase of problem5
    ******** Result: F can not be entailed by the knowledgebase of problem5
    ******** Result: ['not', 'F'] can  be entailed by the knowledgebase of problem5
    ******** Result: G can not be entailed by the knowledgebase of problem5
    ******** Result: ['not', 'G'] can  be entailed by the knowledgebase of problem5
    ******** Result: H can not be entailed by the knowledgebase of problem5
    ******** Result: ['not', 'H'] can  be entailed by the knowledgebase of problem5
    ******** Result: I can not be entailed by the knowledgebase of problem5
    ******** Result: ['not', 'I'] can  be entailed by the knowledgebase of problem5
    ******** Result: J can  be entailed by the knowledgebase of problem5
    ******** Result: K can  be entailed by the knowledgebase of problem5
    ******** Result: L can not be entailed by the knowledgebase of problem5
    ******** Result: ['not', 'L'] can  be entailed by the knowledgebase of problem5

    ********The result Using walk SAT ********
    symbols:  ['B', 'D', 'K', 'A', 'C', 'E', 'G', 'I', 'F', 'L', 'H', 'J']
    running time: 0
    running time: 1
    running time: 2
    running time: 3
    running time: 4
    running time: 5
    running time: 6
    running time: 7
    running time: 8
    running time: 9
    running time: 10
    running time: 11
    running time: 12
    running time: 13
    running time: 14
    running time: 15
    running time: 16
    running time: 17
    running time: 18
    running time: 19
    running time: 20
    running time: 21
    running time: 22
    running time: 23
    running time: 24
    running time: 25
    running time: 26
    running time: 27
    running time: 28
    running time: 29
    running time: 30
    running time: 31
    running time: 32
    running time: 33
    running time: 34
    running time: 35
    running time: 36
    running time: 37
    running time: 38
    WalkSAT result: {'B': False, 'D': False, 'K': True, 'A': False, 'C': False, 'E': False, 'G': False, 'I': False, 'F': False, 'L': False, 'H': False, 'J': True}




#### 4.6 Problem 6 Problem 6 The doors of enlightenment
    python3 problem6.py
    ********KnowledgeBase for problem6a ********
    ['or', ['not', 'A'], 'X']
    ['or', 'A', ['not', 'X']]
    ['or', ['not', 'B'], 'Y', 'Z']
    ['or', ['not', 'Y'], 'B']
    ['or', ['not', 'Z'], 'B']
    ['or', 'A', ['not', 'C']]
    ['or', 'B', ['not', 'C']]
    ['or', 'C', ['not', 'A'], ['not', 'B']]
    ['or', 'X', ['not', 'D']]
    ['or', 'Y', ['not', 'D']]
    ['or', 'D', ['not', 'X'], ['not', 'Y']]
    ['or', 'X', ['not', 'E']]
    ['or', 'Z', ['not', 'E']]
    ['or', 'E', ['not', 'X'], ['not', 'Z']]
    ['or', ['not', 'F'], 'D', 'E']
    ['or', ['not', 'D'], 'F']
    ['or', ['not', 'E'], 'F']
    ['or', ['not', 'G'], ['not', 'C'], 'F']
    ['or', 'C', 'G']
    ['or', ['not', 'F'], 'G']
    ['or', ['not', 'H'], ['not', 'G'], 'A']
    ['or', 'G', 'H']
    H
    ['or', ['not', 'A'], 'H']


    ********The result Using truth table ********
    ******** Result: X can  be entailed by the knowledgebase of problem6a
    ******** Result: ['not', 'X'] can not be entailed by the knowledgebase of problem6a
    ******** Result: Y can not be entailed by the knowledgebase of problem6a
    ******** Result: ['not', 'Y'] can not be entailed by the knowledgebase of problem6a
    ******** Result: Z can not be entailed by the knowledgebase of problem6a
    ******** Result: ['not', 'Z'] can not be entailed by the knowledgebase of problem6a
    ********KnowledgeBase for problem6b ********
    ['or', ['not', 'A'], 'X']
    ['or', 'A', ['not', 'X']]
    ['or', ['not', 'C'], 'A']
    ['or', 'C', ['not', 'A']]
    ['or', ['not', 'G'], ['not', 'C'], 'AT', ['not', 'AT']]
    ['or', 'C', 'G']
    ['or', ['not', 'AT'], 'G']
    ['or', 'AT', 'G']
    ['or', ['not', 'H'], ['not', 'G'], 'A']
    ['or', 'G', 'H']
    H
    ['or', ['not', 'A'], 'H']
    AT


    ********The result Using truth table ********
    ******** Result: X can  be entailed by the knowledgebase of problem6b
    ******** Result: ['not', 'X'] can not be entailed by the knowledgebase of problem6b
    ******** Result: Y can not be entailed by the knowledgebase of problem6b
    ******** Result: ['not', 'Y'] can not be entailed by the knowledgebase of problem6b
    ******** Result: Z can not be entailed by the knowledgebase of problem6b
    ******** Result: ['not', 'Z'] can not be entailed by the knowledgebase of problem6b


    ********The result Using walk SAT ********
    symbols:  ['F', 'A', 'D', 'H', 'B', 'C', 'E', 'X', 'G', 'Y', 'Z']
    running time: 0
    running time: 1
    running time: 2
    running time: 3
    running time: 4
    running time: 5
    running time: 6

    WalkSAT result: {'F': False, 'A': True, 'D': False, 'H': True, 'B': False, 'C': False, 'E': False, 'X': True, 'G': True, 'Y': False, 'Z': False}
### 5.Algorithms implemented
#### 5.1 Truth table enumeration
##### tTEntails
1. put KB and alpha together
2. get all the Symbols
3. call tTCheckAll function


    def tTEntails(kb, alpha):
        '''
        returns if KB entailments alpha True or False using truth table
        kb: KnowledgeBase
        alpha: the result to prove

        '''
        clauses = kb.clauses + disCombine('and', cnf.cnf(alpha))
        symbols = propSymbols(combine('and', clauses))

        return tTCheckAll(kb, alpha, symbols, {})

##### tTCheckAll
1. if symbols all given value, start to evalue it by calling function plTrue
2. if the kb is True, to see value of alpha; else return True
3. Returns True only if all the alpha is True when KB is True


    def tTCheckAll(kb, alpha, symbols, model):
        '''
        help to implement tTEntails
        model is a dictionary such as {'P': True, "Q": False}

        '''
        if len(symbols) == 0:
            alphaCnf = cnf.cnf(alpha)
            if plTrue(cnf.cnf(combine('and', kb.clauses)), model):
                return plTrue(alphaCnf, model)
            else:
                return True     # when KB is false, always return True
        else:
            p, rest = symbols[0], symbols[1:]
            return (tTCheckAll(kb, alpha, rest, modelExtend(model, p, True)) and
            tTCheckAll(kb,alpha, rest, modelExtend(model, p, False)))


##### plTrue
1. the input clause is already converted to cnf
2. Return True if the clause is true in the model, and False if it is false.


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



##### tTCheckAll
1. if symbols all given value, start to evalue it by calling function plTrue
2. if the kb is True, to see value of alpha; else return True
3. Returns True only if all the alpha is True when KB is True





#### 5.2 PL resolution method
##### plResolution
1. combine negative alpha with the KB to new clauses
2. do resolution for every pair of the clauses
3. if resolvents contains [], it means contradictary and return true
4. after doing resolution for a lot of time and no new resolvents found return false


```python
def plResolution(kb, alpha):
    '''
    returns if KB entailments alpha True or False using pl resolution
    kb: KnowledgeBase
    alpha: the result to prove

    '''
    clauses = kb.clauses + disCombine('and', cnf.cnf(negativeInside(alpha)))
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
        newList = [cc for cc in newList if not orContainTautology(cc)]
        # subSumption(newList)
        if isSublistOf(newList, clauses):
            return False
        for cc in newList:
            if not cc in clauses:
                clauses.append(cc)
```


##### plResolve
1. follow the rules of pl resolution
2. returns all clauses that can be obtained from clauses ci and cj

```python
def plResolve(ci, cj):
    '''
    returns all clauses that can be obtained from clauses ci and cj

    '''
    clauses = []
    for di in disCombine('or', ci):
        for dj in disCombine('or',cj):
            if di == negativeInside(dj) or negativeInside(di) == dj:
                diNew = disCombine('or', ci)
                diNew.remove(di)
                djNew = disCombine('or', cj)
                djNew.remove(dj)
                dNew = diNew + djNew
                dNew = toUnique(dNew)
                toAddD = combine('or', dNew)
                clauses.append(toAddD)
    return clauses

```

#### 5.3 walkSAT method
1. get all the symbols
2. randomly get a model
3. randomly flipping values of variables for maxFlips times and check its satisfiability
4. If maxFlip times and no model satisfied, return None

```python
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

```

### 6 plresolution improving
I use pl resolution on the 5th and 6th problem, however it run out of my memory.
Even I tried to run it on my personal Nvidia Tesla P4 GPU Server with 64G memory, it still can not work. It did the resolution more than 5,000,000 times.

Finally, I chose WalkSAT to also solve the problem.


    ********The result Using pl resolution ********
    times: 0
    times: 10000
    times: 20000
    times: 30000
    times: 40000
    times: 50000
    .
    .
    .
    times: 5500000
    times: 5510000
    times: 5520000
    times: 5530000
    times: 5540000
    times: 5550000
    times: 5560000
    times: 5570000
    times: 5580000
    times: 5590000
    times: 5600000
    times: 5610000
    times: 5620000
    times: 5630000
    times: 5640000
    times: 5650000
    times: 5660000
    times: 5670000
    times: 5680000
    times: 5690000
    times: 5700000
    times: 5710000
    times: 5720000
    times: 5730000
    ^Z


#### 6.1 duplicateOrElemination
1. Eleminate the duplicate item in or clause

```python
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

```

#### 6.2 subSumption
1. check if the or clause contain the tautology

```python
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

```

### 7 SATplan research

I also read a paper about SATplan algorithm. The paper addresses the problem of encoding Sudoku puzzles into conjunctive normal form (CNF), and subsequently solving them using polynomial-time propositional satisfiability (SAT) inference techniques.

I attach with the paper and some codes in the files.
The codes was writen by JoaoLages https://github.com/JoaoLages
