# Project 2
# Yubao Liu, Siqi Xiong, Xue Li
# Oct 13, 2018

from algorithms import *


if __name__ == "__main__":
    ''' Problem 5 More Liars and Truth-tellers '''
    # knowledgebase
    problem5 = ['and',
                ['if', 'A', ['and', 'H', 'I']],
                ['if', ['not','A'], ['not', ['and', 'H', 'I']]],
                ['if', 'B', ['and', 'A', 'L']],
                ['if', ['not','B'], ['not', ['and', 'A', 'L']]],
                ['if', 'C', ['and', 'B', 'G']],
                ['if', ['not','C'], ['not', ['and', 'B', 'G']]],
                ['if', 'D', ['and', 'E', 'L']],
                ['if', ['not','D'], ['not', ['and', 'E', 'L']]],
                ['if', 'E', ['and', 'C', 'H']],
                ['if', ['not','E'], ['not', ['and', 'C', 'H']]],
                ['if', 'F', ['and', 'D', 'I']],
                ['if', ['not','F'], ['not', ['and', 'D', 'I']]],
                ['if', 'G', ['and', ['not', 'E'], ['not', 'J']]],
                ['if', ['not', 'G'], ['not', ['and', ['not', 'E'], ['not', 'J']]]],
                ['if', 'H', ['and', ['not', 'F'], ['not', 'K']]],
                ['if', ['not', 'H'], ['not', ['and', ['not', 'F'], ['not', 'K']]]],
                ['if', 'I', ['and', ['not', 'G'], ['not', 'K']]],
                ['if', ['not', 'I'], ['not', ['and', ['not', 'G'], ['not', 'K']]]],
                ['if', 'J', ['and', ['not', 'A'], ['not', 'C']]],
                ['if', ['not', 'J'], ['not', ['and', ['not', 'A'], ['not', 'C']]]],
                ['if', 'K', ['and', ['not', 'D'], ['not', 'F']]],
                ['if', ['not', 'K'], ['not', ['and', ['not', 'D'], ['not', 'F']]]],
                ['if', 'L', ['and', ['not', 'B'], ['not', 'J']]],
                ['if', ['not', 'L'], ['not', ['and', ['not', 'B'], ['not', 'J']]]]
            ]
    toSolve5a = 'A'
    toSolve5b = 'B'
    toSolve5c = 'C'
    toSolve5d = 'D'
    toSolve5e = 'E'
    toSolve5f = 'F'
    toSolve5g = 'G'
    toSolve5h = 'H'
    toSolve5i = 'I'
    toSolve5j = 'J'
    toSolve5k = 'K'
    toSolve5l = 'L'
    kbProblem5 = KnowledgeBase()
    for clause in problem5[1:]:
        kbProblem5.tell(clause)
    print("********KnowledgeBase for problem5 ********")
    for c in kbProblem5.clauses:
        print(c)
    print("\n")
    using truth table to solve
    print("********The result Using truth table ********")
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5a, "" if tTEntails(kbProblem5, toSolve5a) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (['not', toSolve5a], "" if tTEntails(kbProblem5, ['not', toSolve5a]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5b, "" if tTEntails(kbProblem5, toSolve5b) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (['not', toSolve5b], "" if tTEntails(kbProblem5, ['not', toSolve5b]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5c, "" if tTEntails(kbProblem5, toSolve5c) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (['not', toSolve5c], "" if tTEntails(kbProblem5, ['not', toSolve5c]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5d, "" if tTEntails(kbProblem5, toSolve5d) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (['not', toSolve5d], "" if tTEntails(kbProblem5, ['not', toSolve5d]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5e, "" if tTEntails(kbProblem5, toSolve5e) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (['not', toSolve5e], "" if tTEntails(kbProblem5, ['not', toSolve5e]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5f, "" if tTEntails(kbProblem5, toSolve5f) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (['not', toSolve5f], "" if tTEntails(kbProblem5, ['not', toSolve5f]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5g, "" if tTEntails(kbProblem5, toSolve5g) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (['not', toSolve5g], "" if tTEntails(kbProblem5, ['not', toSolve5g]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5h, "" if tTEntails(kbProblem5, toSolve5h) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (['not', toSolve5h], "" if tTEntails(kbProblem5, ['not', toSolve5h]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5i, "" if tTEntails(kbProblem5, toSolve5i) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (['not', toSolve5i], "" if tTEntails(kbProblem5, ['not', toSolve5i]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5j, "" if tTEntails(kbProblem5, toSolve5j) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5k, "" if tTEntails(kbProblem5, toSolve5k) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5l, "" if tTEntails(kbProblem5, toSolve5l) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (['not', toSolve5l], "" if tTEntails(kbProblem5, ['not', toSolve5l]) else "not"))
    
    print("\n")

    print("********The result Using walk SAT ********")
    print("WalkSAT result:", walkSAT(kbProblem5.clauses, maxFlips = 10000))
    print("\n")

    # # using pl resolution to solve
    # print("********The result Using pl resolution ********")
    # # print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5a, "" if plResolution(kbProblem5, toSolve5a) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (['not', toSolve5a], "" if plResolution(kbProblem5, ['not', toSolve5a]) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5b, "" if plResolution(kbProblem5, toSolve5b) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5c, "" if plResolution(kbProblem5, toSolve5c) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5d, "" if plResolution(kbProblem5, toSolve5d) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5e, "" if plResolution(kbProblem5, toSolve5e) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5f, "" if plResolution(kbProblem5, toSolve5f) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5g, "" if plResolution(kbProblem5, toSolve5g) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5h, "" if plResolution(kbProblem5, toSolve5h) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5i, "" if plResolution(kbProblem5, toSolve5i) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5j, "" if plResolution(kbProblem5, toSolve5j) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5k, "" if plResolution(kbProblem5, toSolve5k) else "not"))
    # print("******** Result: %s can %s be entailed by the knowledgebase of problem5" % (toSolve5l, "" if plResolution(kbProblem5, toSolve5l) else "not"))
    # print("\n")

