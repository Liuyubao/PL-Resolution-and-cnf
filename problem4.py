# Project 2
# Yubao Liu, Siqi Xiong, Xue Li
# Oct 13, 2018

from algorithms import *


if __name__ == "__main__":
    ''' Problem 4 Liars and Truth-tellers '''
    # knowledgebase
    problem4a = ['and',
                ['if', 'A', ['and', 'C', 'A']],
                ['if', ['not', 'A'], ['not', ['and', 'C', 'A']]],
                ['if', 'B', ['not', 'C']],
                ['if', ['not', 'B'], 'C'],
                ['if', 'C', ['or', 'B', ['not', 'C']]],
                ['if', ['not', 'C'], ['not', ['or', 'B', ['not', 'C']]]]
            ]
    toSolve4a = 'A'
    toSolve4b = 'B'
    toSolve4c = 'C'
    kbProblem4a = KnowledgeBase()
    for clause in problem4a[1:]:
        kbProblem4a.tell(clause)
    print("********KnowledgeBase for problem4a ********")
    for c in kbProblem4a.clauses:
        print(c)
    print("\n")
    # using truth table to solve
    print("********The result Using truth table ********")
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4a" % (toSolve4a, "" if tTEntails(kbProblem4a, toSolve4a) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4a" % (toSolve4b, "" if tTEntails(kbProblem4a, toSolve4b) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4a" % (toSolve4c, "" if tTEntails(kbProblem4a, toSolve4c) else "not"))
    
    print("\n")
    # using pl resolution to solve
    print("********The result Using pl resolution ********")
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4a" % (toSolve4a, "" if plResolution(kbProblem4a, toSolve4a) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4a" % (toSolve4b, "" if plResolution(kbProblem4a, toSolve4b) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4a" % (toSolve4c, "" if plResolution(kbProblem4a, toSolve4c) else "not"))

    # knowledgebase
    problem4b = ['and',
                ['if', 'A', ['not', 'C']],
                ['if', ['not', 'A'], 'C'],
                ['if', 'B', ['and','A', 'C']],
                ['if', ['not', 'B'], ['not', ['and','A', 'C']]],
                ['if', 'C', 'B'],
                ['if', ['not', 'C'], ['not', 'B']]
            ]
    kbProblem4b = KnowledgeBase()
    for clause in problem4b[1:]:
        kbProblem4b.tell(clause)
    print("********KnowledgeBase for problem4b ********")
    for c in kbProblem4b.clauses:
        print(c)
    print("\n")
    # using truth table to solve
    print("********The result Using truth table ********")
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4b" % (toSolve4a, "" if tTEntails(kbProblem4b, toSolve4a) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4b" % (toSolve4b, "" if tTEntails(kbProblem4b, toSolve4b) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4b" % (['not', toSolve4b], "" if tTEntails(kbProblem4b, ['not', toSolve4b]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4b" % (toSolve4c, "" if tTEntails(kbProblem4b, toSolve4c) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4b" % (['not', toSolve4c], "" if tTEntails(kbProblem4b, ['not', toSolve4c]) else "not"))

    print("\n")
    # using pl resolution to solve
    print("********The result Using pl resolution ********")
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4b" % (toSolve4a, "" if plResolution(kbProblem4b, toSolve4a) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4b" % (toSolve4b, "" if plResolution(kbProblem4b, toSolve4b) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4b" % (['not', toSolve4b], "" if plResolution(kbProblem4b, ['not', toSolve4b]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4b" % (toSolve4c, "" if plResolution(kbProblem4b, toSolve4c) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem4b" % (['not', toSolve4c], "" if plResolution(kbProblem4b, ['not', toSolve4c]) else "not"))
