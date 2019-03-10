from utils import Atom


class Convert_to_cnf:
    """Receives a list of Atoms and converts the whole list to cnf"""
    def __init__(self, s):
        self.s = s
        self.s = self.remove_implications(self.s)
        self.s = self.NOT(self.s)
        self.s = self.distributive(self.s)

    def remove_implications(self, s): # Remove '==>'
        if not s.args or s.operator[0].isalpha():
            return s  # Atoms are unchanged.
        args = list(map(self.remove_implications, s.args))
        a, b = args[0], args[-1]
        if s.operator == '==>':
            return b | ~a
        else:
            return Atom(s.operator, *args)

    def NOT_inverted(self, s):  # reversed version of NOT
        return self.NOT(~s)

    def NOT(self, s):  # move ~(NOT) to the inside of a sentence
        if s.operator == '~':
            a = s.args[0]
            if a.operator == '~': # ~~x
                return self.NOT(a.args[0])  # return x
            if a.operator == '&': # & -> |
                return unite_clauses('|', list(map(self.NOT_inverted, a.args)))  # return arguments with operatorposite signal
            if a.operator == '|': # | -> &
                return unite_clauses('&', list(map(self.NOT_inverted, a.args)))  # return arguments with operatorposite signal
            return s  # nothing to change
        elif s.operator[0].isalpha() or not s.args:
            return s  # nothing to change
        else:
            return Atom(s.operator, *list(map(self.NOT, s.args)))

    def distributive(self, s):  # do the distributive (x & y) | z = (z|x) & (z|y)
        if s.operator == '|':
            s = unite_clauses('|', s.args)
            if s.operator != '|':
                return self.distributive(s)
            if len(s.args) == 0:
                return False
            if len(s.args) == 1:
                return self.distributive(s.args[0])
            conj = [arg for arg in s.args if arg.operator == '&']
            try:
                conj = conj[0]
            except:
                conj = None
            if not conj:
                return s
            others = [a for a in s.args if a is not conj]
            rest = unite_clauses('|', others)
            return unite_clauses('&', [self.distributive(c | rest) for c in conj.args])
        elif s.operator == '&':
            return unite_clauses('&', list(map(self.distributive, s.args)))
        else:
            return s



def unite_clauses(operator, args):
    """ Return the sentence united with &s or |s """
    args = get_args(operator, args)
    if len(args) == 0:
        if operator == '&':
            return True
        else: # operator == |
            return False
    elif len(args) == 1:
        return args[0]
    else:
        return Atom(operator, *args)


def get_args(operator, args):
    """Returns a list of all the arguments in a clause"""
    result = []

    def collect(subargs):
        for arg in subargs:
            if arg.operator == operator:
                collect(arg.args)
            else:
                result.append(arg)
    collect(args)
    return result