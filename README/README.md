# README

    Yubao Liu
    Oct 13, 2018


Environment:

    python3.6.7

Components:
* algorithm.py  --  all the algorithms implemented
* cnf.py        --  inplements about cnf
* problem1-6.py --  details about each problem



How to run?

    >>>python3 problem1.py
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

Don't want to see the details?

    # change the variable detailsTurn in KnowledgeBase to be False
    kbProblem1 = KnowledgeBase()
    kbProblem1.detailsTurn = True   # print the algorithm details

    # then ran the corresponding problem
    >>>python3 problem2.py
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
