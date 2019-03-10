# Project 2
# Yubao Liu, Siqi Xiong, Xue Li
# Oct 13, 2018

from algorithms import *


if __name__ == "__main__":

    ''' Problem 6 The doors of enlightenment '''
    # knowledgebase
    problem6a = ['and',
                ['if', 'A', 'X'],
                ['if', ['not','A'], ['not', 'X']],
                ['if', 'B', ['or', 'Y', 'Z']],
                ['if', ['not','B'], ['not', ['or', 'Y', 'Z']]],
                ['if', 'C', ['and', 'A', 'B']],
                ['if', ['not','C'], ['not', ['and', 'A', 'B']]],
                ['if', 'D', ['and', 'X', 'Y']],
                ['if', ['not','D'], ['not', ['and', 'X', 'Y']]],
                ['if', 'E', ['and', 'X', 'Z']],
                ['if', ['not','E'], ['not', ['and', 'X', 'Z']]],
                ['if', 'F', ['or', 'D', 'E']],
                ['if', ['not','F'], ['not', ['or', 'D', 'E']]],
                ['if', 'G', ['if', 'C', 'F']],
                ['if', ['not','G'], ['not', ['if', 'C', 'F']]],
                ['if', 'H', ['if', ['and', 'G', 'H'], 'A']],
                ['if', ['not','H'], ['not', ['if', ['and', 'G', 'H'], 'A']]]
            ]
    toSolve6a = 'A'
    toSolve6b = 'B'
    toSolve6c = 'C'
    toSolve6d = 'D'
    toSolve6e = 'E'
    toSolve6f = 'F'
    toSolve6g = 'G'
    toSolve6h = 'H'
    toSolve6x = 'X'
    toSolve6y = 'Y'
    toSolve6z = 'Z'
    # toSolve6l = ''
    kbProblem6a = KnowledgeBase()
    for clause in problem6a[1:]:
        kbProblem6a.tell(clause)
    print("********KnowledgeBase for problem6a ********")
    for c in kbProblem6a.clauses:
        print(c)
    print("\n")
    # using truth table to solve
    print("********The result Using truth table ********")
    print("******** Result: %s can %s be entailed by the knowledgebase of problem6a" % (toSolve6x, "" if tTEntails(kbProblem6a, toSolve6x) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem6a" % (['not', toSolve6x], "" if tTEntails(kbProblem6a, ['not', toSolve6x]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem6a" % (toSolve6y, "" if tTEntails(kbProblem6a, toSolve6y) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem6a" % (['not', toSolve6y], "" if tTEntails(kbProblem6a, ['not', toSolve6y]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem6a" % (toSolve6z, "" if tTEntails(kbProblem6a, toSolve6z) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem6a" % (['not', toSolve6z], "" if tTEntails(kbProblem6a, ['not', toSolve6z]) else "not"))
    
    # print("\n")
    # # using pl resolution to solve
    # print("********The result Using pl resolution ********")
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem6a" % (toSolve6x, "" if plResolution(kbProblem6a, toSolve6x) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem6a" % (['not', toSolve6x], "" if plResolution(kbProblem6a, ['not', toSolve6x]) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem6a" % (toSolve6y, "" if plResolution(kbProblem6a, toSolve6y) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem6a" % (['not', toSolve6y], "" if plResolution(kbProblem6a, ['not', toSolve6y]) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem6a" % (toSolve6z, "" if plResolution(kbProblem6a, toSolve6z) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem6a" % (['not', toSolve6z], "" if plResolution(kbProblem6a, ['not', toSolve6z]) else "not"))
    
    

    print("********The result Using walk SAT ********")
    print("WalkSAT result:", walkSAT(kbProblem6a.clauses, maxFlips = 10000))
    print("\n")

    # knowledgebase
    problem6b = ['and',
                ['if', 'A', 'X'],
                ['if', ['not','A'], ['not', 'X']],
                ['if', 'C', 'A'],
                ['if', ['not','C'], ['not', 'A']],
                ['if', 'G', ['or', ['if', 'C', 'AT'], ['if', 'C', ['not','AT']]]],
                ['if', ['not','G'], ['not', ['or', ['if', 'C', 'AT'], ['if', 'C', ['not','AT']]]]],
                ['if', 'H', ['if', ['and', 'G', 'H'], 'A']],
                ['if', ['not','H'], ['not', ['if', ['and', 'G', 'H'], 'A']]],
                'AT'   # always true
            ]
    kbProblem6b = KnowledgeBase()
    for clause in problem6b[1:]:
        kbProblem6b.tell(clause)
    print("********KnowledgeBase for problem6b ********")
    for c in kbProblem6b.clauses:
        print(c)
    print("\n")
    # using truth table to solve
    print("********The result Using truth table ********")
    print("******** Result: %s can %s be entailed by the knowledgebase of problem6b" % (toSolve6x, "" if tTEntails(kbProblem6b, toSolve6x) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem6b" % (['not', toSolve6x], "" if tTEntails(kbProblem6b, ['not', toSolve6x]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem6b" % (toSolve6y, "" if tTEntails(kbProblem6b, toSolve6y) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem6b" % (['not', toSolve6y], "" if tTEntails(kbProblem6b, ['not', toSolve6y]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem6b" % (toSolve6z, "" if tTEntails(kbProblem6b, toSolve6z) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem6b" % (['not', toSolve6z], "" if tTEntails(kbProblem6b, ['not', toSolve6z]) else "not"))
    
    print("\n")
    # # using pl resolution to solve
    # print("********The result Using pl resolution ********")
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem6b" % (toSolve6x, "" if plResolution(kbProblem6b, toSolve6x) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem6b" % (['not', toSolve6x], "" if plResolution(kbProblem6b, ['not', toSolve6x]) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem6b" % (toSolve6y, "" if plResolution(kbProblem6b, toSolve6y) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem6b" % (['not', toSolve6y], "" if plResolution(kbProblem6b, ['not', toSolve6y]) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem6b" % (toSolve6z, "" if plResolution(kbProblem6b, toSolve6z) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem6b" % (['not', toSolve6z], "" if plResolution(kbProblem6b, ['not', toSolve6z]) else "not"))
    
    print("\n")
