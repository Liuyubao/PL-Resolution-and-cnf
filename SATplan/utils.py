from copy import deepcopy


def to_atom(line):
    """ Creates an Atom from a string given the format 'operator(arg0, arg1, ... )' """
    operator = line[0:line.find('(')]
    args = line[line.find('(') + 1:line.find(')')]
    consts = args.split(',')
    expr = []
    for c in consts:
        expr.append(Atom(c))
    return Atom(operator, *expr)


class Atom(object):
    """ Auxiliar class to handle expressions of type 'operator(*args)' and its operations """
    def __init__(self, operator, *args):
        self.operator = str(operator)
        self.args = args

    """ Operations """

    # Negated Atom
    def __invert__(self):
        return Atom('~', self)

    # Atom1 & Atom2
    def __and__(self, rhs):
        return Atom('&', self, rhs)

    # Atom1 | Atom2
    def __or__(self, rhs):
        if isinstance(rhs, Atom):
            return Atom('|', self, rhs)
        else:
            return PartialAtom(rhs, self)

    def __call__(self, *args):
        return Atom(self.operator, *args)

    def __eq__(self, other): # Compare Atoms and return True if they're equal
        return isinstance(other, Atom) and self.operator == other.operator and self.args == other.args

    def __hash__(self): # make Atom hashable
        return hash(self.operator) ^ hash(self.args)

    def change_op(self):

        operator = deepcopy(self.operator)
        args_aux = deepcopy(self.args)
        args = [str(arg) for arg in args_aux]
        if operator.isidentifier():       # f(x) or f(x, y)
            self.operator = '{}({})'.format(operator, ','.join(args)) if args else operator
            del self.args
            self.operator = self.operator.replace("(", "")
            self.operator = self.operator.replace(")", "")
            self.operator = self.operator.replace(",", "")
            self.operator = self.operator.upper()

            return str(self.operator)
        elif len(args) == 1:        # -x or -(x + 1)
            self.operator = operator + args[0]
            self.operator = self.operator.replace("(", "")
            self.operator = self.operator.replace(")", "")
            self.operator = self.operator.replace(",", "")
            self.operator = self.operator.upper()
            del self.args
            return str(self.operator)


        else:                       # (x - y)
            opp = ('' + operator + '')
            self.operator = '(' + opp.join(args) + ')'

            del self.args
            self.operator = self.operator.replace("(", "")
            self.operator = self.operator.replace(")", "")
            self.operator = self.operator.replace(",", "")
            self.operator = self.operator.upper()

            return str(self.operator)

    def __repr__(self):
        operator = self.operator
        args = [str(arg) for arg in self.args]
        if operator.isidentifier():       # f(x) or f(x, y)
            return '{} {}'.format(operator, ' '.join(args)) if args else operator
        elif len(args) == 1:        # -x or -(x + 1)
            return operator + args[0]
        else:                       # (x - y)
            opp = (' ' + operator + ' ')
            return '(' + opp.join(args) + ')'

    def __lt__(self, other):
        return str(self.operator)+str(self.args) < str(other.operator)+str(other.args)


class PartialAtom:
    """Given 'P |'==>'| Q, first form PartialExpr('==>', P), then combine with Q."""
    def __init__(self, operator, lhs):
        self.operator, self.lhs = operator, lhs

    def __or__(self, rhs):
        return Atom(self.operator, self.lhs, rhs)