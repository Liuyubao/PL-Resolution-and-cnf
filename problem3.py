# Project 2
# Yubao Liu, Siqi Xiong, Xue Li
# Oct 13, 2018

from algorithms import *


if __name__ == "__main__":

    ''' Problem 3 Wumpus world '''
    # knowledgebase
    problem3 = ['and',
                ['if', 'mythical', 'immortal'],
                ['if', ['not', 'mythical'], ['and', 'mortal', 'mammal']],
                ['if', ['or', 'immortal', 'mammal'], 'horned'],
                ['if', 'horned', 'magical']
            ]
    toSolve3a = 'mythical'
    toSolve3b = 'magical'
    toSolve3c = 'horned'
    kbProblem3 = KnowledgeBase()
    kbProblem3.detailsTurn = False
    for clause in problem3[1:]:
        kbProblem3.tell(clause)
    print("********KnowledgeBase for problem3 ********")
    for c in kbProblem3.clauses:
        print(c)
    print("\n")
    # using truth table to solve
    print("********The result Using truth table ********")
    print("******** Result: %s can %s be entailed by the knowledgebase of problem3" % (toSolve3a, "" if tTEntails(kbProblem3, toSolve3a) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem3" % (['not', toSolve3a], "" if tTEntails(kbProblem3, ['not', toSolve3a]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem3" % (toSolve3b, "" if tTEntails(kbProblem3, toSolve3b) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem3" % (toSolve3c, "" if tTEntails(kbProblem3, toSolve3c) else "not"))

    print("\n")
    # using pl resolution to solve
    print("********The result Using pl resolution ********")
    print("******** Result: %s can %s be entailed by the knowledgebase of problem3" % (toSolve3a, "" if plResolution(kbProblem3, toSolve3a) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem3" % (['not', toSolve3a], "" if plResolution(kbProblem3, ['not', toSolve3a]) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem3" % (toSolve3b, "" if plResolution(kbProblem3, toSolve3b) else "not"))
    print("******** Result: %s can %s be entailed by the knowledgebase of problem3" % (toSolve3c, "" if plResolution(kbProblem3, toSolve3c) else "not"))
    
    