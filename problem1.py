# Project 2
# Yubao Liu, Siqi Xiong, Xue Li
# Oct 13, 2018

from algorithms import *



if __name__ == "__main__":
    ''' Problem 1 Modus Ponens '''
    # knowledgebase
    problem1 = ['and',
                'P',
                ['if', 'P', 'Q']
            ]
    toSolve1 = 'Q'
    kbProblem1 = KnowledgeBase()
    kbProblem1.detailsTurn = True   # print the algorithm details
    for clause in problem1[1:]:
        kbProblem1.tell(clause)
    print("********KnowledgeBase for problem1 ********")
    for c in kbProblem1.clauses:
        print(c)
    print("\n")
    # using truth table to solve
    print("********The result Using truth table ********")
    print("******** Result: %s can %s be entailed by the knowledgebase of problem1" % (toSolve1, "" if tTEntails(kbProblem1, toSolve1) else "not"))
    
    print("\n")

    # using pl resolution to solve
    print("********The result Using pl resolution ********")
    print("******** Result: %s can %s be entailed by the knowledgebase of problem1" % (toSolve1, "" if plResolution(kbProblem1, toSolve1) else "not"))
    