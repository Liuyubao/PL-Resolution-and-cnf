# Project 2
# Yubao Liu, Siqi Xiong, Xue Li
# Oct 13, 2018


from algorithms import *


if __name__ == "__main__":
    ''' Problem 2 Wumpus world '''
    # knowledgebase
    problem2 = ['and',
                ['not', 'P11'],
                ['iff', 'B11', ['or', 'P12', 'P21']],
                ['iff', 'B21', ['or', 'P11', 'P22', 'P31']],
                ['not', 'B11'],
                'B21'
            ]
    toSolve2 = ['not', 'P12']
    kbProblem2 = KnowledgeBase()
    kbProblem2.detailsTurn = False
    for clause in problem2[1:]:
        kbProblem2.tell(clause)
    print("********KnowledgeBase for problem2 ********")
    for c in kbProblem2.clauses:
        print(c)
    print("\n")
    # using truth table to solve
    print("********The result Using truth table ********")
    print("******** Result: %s can %s be entailed by the knowledgebase of problem2" % (toSolve2, "" if tTEntails(kbProblem2, toSolve2) else "not"))
    
    print("\n")
    # using pl resolution to solve
    print("********The result Using pl resolution ********")
    print("******** Result: %s can %s be entailed by the knowledgebase of problem2" % (toSolve2, "" if plResolution(kbProblem2, toSolve2) else "not"))
    