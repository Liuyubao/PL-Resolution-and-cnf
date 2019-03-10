import time
from copy import deepcopy
import itertools
from dpll import DPLL
from cnf import *


def SAT_plan(init, constants, actions, grounded_predicates, actions_grounded, goal, t_max):

    # Functions used by SAT_plan
    def translate_to_SAT(init, constants, actions, grounded_predicates, actions_grounded, goal, time):
        clauses = []

        # Add initial state axiom
        functions_set = set()
        for atom in init:
            if tuple((atom.operator, atom.args)) not in functions_set:
                functions_set.add(tuple((atom.operator, atom.args)))

            atom_aux = deepcopy(atom)
            aux = atom_aux.change_op() + "{}"
            clauses.append(Atom(aux.format(0)))  # add positive clauses

        # Add other atoms in Hebrand base
        for predicate in grounded_predicates:
            if tuple((predicate.operator, predicate.args)) not in functions_set:
                aux = deepcopy(predicate)
                aux = aux.change_op() + "{}"
                clauses.append(~Atom(aux.format(0)))  # add negated clauses

        # Add goal state axiom
        for atom in goal:
            atom_aux = deepcopy(atom)
            aux = atom_aux.change_op() + "{}"
            clauses.append(Atom(aux.format(time)))

        # Add actions axiom
        for t in range(time):
            for action in actions:
                combinations = list(itertools.product(constants, repeat=len(action.args)))
                for combination in combinations:

                    # replace the variables in the preconditions and effects of a certain action with the appropriate
                    # constants
                    precond_n, precond_p, effect_add, effect_rem = action.substitute(combination)

                    if not any([i in effect_add for i in effect_rem]): # to remove inconsistent actions
                        expr = []
                        for c in combination:
                            expr.append(c)

                        new_action = Atom(action.name, *expr)
                        action_dict = deepcopy(new_action)
                        for i, precond in enumerate(precond_n):
                            aux = precond.change_op() + "{}"
                            precond_n[i] = Atom(aux.format(t))
                        for i, precond in enumerate(precond_p):
                            aux = precond.change_op() + "{}"
                            precond_p[i] = Atom(aux.format(t))
                        for i, effect in enumerate(effect_add):
                            aux = effect.change_op() + "{}"
                            effect_add[i] = Atom(aux.format(t+1))
                        for i, effect in enumerate(effect_rem):
                            aux = effect.change_op() + "{}"
                            effect_rem[i] = Atom(aux.format(t+1))

                        aux = new_action.change_op() + "{}"
                        action_sym[Atom(aux.format(t))] = action_dict
                        new_action = Atom(aux.format(t))

                        if len(precond_n) > 0:
                            clauses.append(new_action |'==>'| unite_clauses('&', [~precond for precond in precond_n]))
                        if len(precond_p) > 0:
                            clauses.append(new_action |'==>'| unite_clauses('&', [precond for precond in precond_p]))
                        if len(effect_add) > 0:
                            clauses.append(new_action |'==>'| unite_clauses('&', [effect for effect in effect_add]))
                        if len(effect_rem) > 0:
                            clauses.append(new_action |'==>'| unite_clauses('&', [~effect for effect in effect_rem]))

        # Add frame axioms
        for t in range(time):
            for action in actions:
                combinations = list(itertools.product(constants, repeat=len(action.args)))
                for combination in combinations:
                    precond_n, precond_p, effect_add, effect_rem = action.substitute(combination)
                    if not any([i in effect_add for i in effect_rem]):  # to remove inconsistent actions
                        effect = effect_add + effect_rem  # concatenate both effects
                        for e in effect:
                            for arg_pos, arg in enumerate(e.args):
                                e.args[arg_pos] = Atom(arg)
                            e.args = tuple(e.args)
                        expr = []
                        for c in combination:
                            expr.append(c)
                        new_action = Atom(action.name, *expr)
                        aux = new_action.change_op() + "{}"
                        new_action = Atom(aux.format(t))
                        for atom in grounded_predicates:  # atom.args -> tuple(Atom,Atom, ...)
                            for pos, e in enumerate(effect):
                                if atom.operator == e.operator and Atom(atom.args) == Atom(e.args):  # this move has an effect on the atom
                                    break  # don't add to clauses
                                if pos == (len(effect)-1): # this move has no effect on the atom -> add clauses (positives and negatives)
                                    aux_atom = deepcopy(atom)
                                    aux_next_atom = deepcopy(atom)
                                    aux_atom = aux_atom.change_op() + "{}"
                                    aux_atom = aux_atom.format(t)
                                    aux_next_atom = aux_next_atom.change_op() + "{}"
                                    aux_next_atom = aux_next_atom.format(t+1)
                                    clauses.append(((Atom(aux_atom)) |'&'| (Atom(new_action))) |'==>'| Atom(aux_next_atom))
                                    clauses.append(((~Atom(aux_atom)) |'&'| (Atom(new_action))) |'==>'| ~Atom(aux_next_atom))

        #  Add axioms "only one action at a time"
        for t in range(time):
            actions_with_index = [] # list with all actions in this t time
            for action in actions_grounded:
                action_aux = deepcopy(action)
                action_aux = action_aux.change_op() + "{}"
                action_aux = action_aux.format(t)
                actions_with_index.append(Atom(action_aux))
            clauses.append(unite_clauses('|', actions_with_index)) # add OR of all actions to clauses

            for i in range(len(actions_with_index)):
                for j in range(i+1, len(actions_with_index)):
                    clauses.append(~((actions_with_index[i]) & (actions_with_index[j])))

        return unite_clauses('&', clauses)

    # gets the solution from the model
    def extract_solution(model):
        solution = []
        for m in model:
            # gets the actions set to True
            if m in action_sym and model[m] is True:
                solution.append(m)
        # sorts the actions according to the time period
        solution = sorted(solution, key=lambda x: x.operator[-1])
        for i, item in enumerate(solution):
            solution[i] = action_sym[item]

        return solution

    # Body of algorithm
    for t in range(t_max):
        # dictionary to help extract the solution from model
        action_sym = {}

        cnf = translate_to_SAT(init, constants, actions, grounded_predicates, actions_grounded, goal, t)

        my_dpll = DPLL(cnf)

        if my_dpll.model is not False:
            return extract_solution(my_dpll.model)
    return None
