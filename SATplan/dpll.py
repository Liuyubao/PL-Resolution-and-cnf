from cnf import *
from copy import deepcopy


class DPLL:
    """ Receives a sentence of Atoms and returns a model that satisfies every clause """
    def __init__(self, sentence):
        self.sentence = sentence

        # Convert to CNF
        self.clauses = get_args('&', [Convert_to_cnf(sentence).s])

        # Get list of symbols
        self.symbols = list(self.prop_symbols(sentence, set()))

        # for consistent result
        self.symbols.sort()

        # Create an empty model with all symbols
        self.model = self.dpll(self.clauses, self.symbols, {})

    def dpll(self, clauses, symbols, model):
        "See if the clauses are true in a partial model."

        unknown_clauses = []  # clauses with an unknown truth value
        unit_clauses = []  # unit clauses list
        for c in clauses:
            val = self.evaluate_clause(c, model)
            if val is False:
                return False  # return UNSAT  -> Backtrack
            if val is not True:  # only append clauses that were not proved (val = None)
                # appends new clause
                unknown_clauses.append(c)
                # finds immediately if it is a unit clause or not
                P, value = self.unit_clause_assign(c, model)
                if P:
                    unit_clauses.append((P, value))
        if not unknown_clauses:  # no clauses left
            return model

        if unit_clauses: # return unit_clauses if they exist
            aux = set()
            for P, value in unit_clauses:
                aux.add(P)
                model[P] = value  # assign all values in the unit clauses
            return self.dpll(unknown_clauses, [x for x in symbols if x not in aux], model)

        P, value = self.find_pure_symbol(symbols, unknown_clauses)  # searches for a pure symbol and returns it
        if P:
            model[P] = value
            return self.dpll(unknown_clauses, [x for x in symbols if x != P], model)

        # Branch - choose the first symbol from the list and assign it a value
        P, symbols = symbols[0], symbols[1:]
        model_t, model_f = deepcopy(model), deepcopy(model)
        model_t[P] = True
        model_f[P] = False

        # Try True and False assignment, in this order
        return self.dpll(unknown_clauses, symbols, model_t) or self.dpll(unknown_clauses, symbols, model_f)

    @staticmethod
    def prop_symbols(x, symbols):
        """ Returns all the symbols in a sentence """
        x.args = list(x.args)
        for arg in x.args:
            if len(arg.args) == 0:
                symbols.add(arg)
            else:
                for a in arg.args:
                    x.args.append(a)
        return symbols

    def evaluate_clause(self, exp, model={}):
        """Return True if the sentence is already satisfiable, False if it is unsatisfiable
        and None if it is unknown in the model yet """

        operator, args = exp.operator, exp.args
        if operator[:1].isalpha() and operator[0].isupper():
            try:
                return model[exp]
            except:
                return None
        elif operator == '~':
            p = self.evaluate_clause(args[0], model)
            if p is None:
                return None
            else:
                return not p
        elif operator == '|':
            result = False
            for arg in args:
                p = self.evaluate_clause(arg, model)
                if p is True:
                    return True
                if p is None:
                    result = None
            return result
        elif operator == '&':
            result = True
            for arg in args:
                p = self.evaluate_clause(arg, model)
                if p is False:
                    return False
                if p is None:
                    result = None
            return result

    @staticmethod
    def find_pure_symbol(symbols, clauses):
        """Finds a pure symbol in a sentence"""
        for s in symbols:
            found_pos, found_neg = False, False
            for c in clauses:
                if not found_pos and s in get_args('|', [c]):
                    found_pos = True
                if not found_neg and ~s in get_args('|', [c]):
                    found_neg = True
            if found_pos != found_neg:
                return s, found_pos
        return None, None

    def unit_clause_assign(self, clause, model):
        """ Return the symbol and its value if the clause is Unit"""
        P, value = None, None
        for literal in get_args('|', [clause]):
            sym, positive = self.inspect_literal(literal)
            if sym in model:
                if model[sym] == positive:
                    return None, None  # clause already True
            elif P:
                return None, None      # more than 1 unbound variable
            else:
                P, value = sym, positive
        return P, value

    @staticmethod
    def inspect_literal(literal):
        """ AUxiliar function to unit_clause_assign, sees if literal is the positive or negative Atom"""
        if literal.operator == '~':
            return literal.args[0], False
        else:
            return literal, True