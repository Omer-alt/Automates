
class DFA:
    
    def __init__(self, alphabet):

        self.states = []
        self.transitions = {}
        self.init = None
        self.finals = []
        self.alphabet = ""

        for symbol in alphabet:
            if symbol not in self.alphabet:
                self.alphabet += symbol

    # Add a state
    def add_state(self, state, final = False):
        """ Add a new state. Print error if the state already exists.
            @param state    the name of the new state.
            @param final    a boolean determining if the state is
                final"""
        if state in self.states:
            print("error : state '" + state + "' already exists.")
            return
        self.transitions[state] = []
        self.states.append(state)
        if final:
            self.finals.append(state)

    def valid_symbol(self, symbol):
        """ Returns true if the symbol is part of the alphabet,
            false otherwise.
            @param symbol the symbol to be tested """
        if symbol not in self.alphabet: return False
        return True
    # verify if my transition exist!
    def dst_state(self, src_state, symbol):
        """ Search the transition corresponding to the specified source state
            and symbol and returns the destination state. If the transition does
            not exists, return None.
            @param src_state the source state of the transition.
            @param symbol the symbol of the transition. """
        if src_state not in self.states:
            print("error : the state '" + src_state + "' is not an existing state.")
            return
        for (s, dst_state) in self.transitions[src_state]:
            if s == symbol:
                return dst_state
        return None

    def add_transition(self, src_state, symbol, dst_state):
        """ Add a transition to the FA. Print error if the automaton already have a
            transition for the specified source state and symbol.
            @param src_state the name of the source state.
            @param symbol the symbol of the transition
            @param dst_state the name of the destination state."""
        if not self.valid_symbol(symbol):
            print("error : the symbol '" + symbol + "' is not part of the alphabet.")
            return
        if src_state not in self.states:
            print("error : the state '" + src_state + "' is not an existing state.")
            return
        if dst_state not in self.states:
            print("error : the state '" + dst_state + "' is not an existing state.")
            return

        if self.dst_state(src_state, symbol) != None:
            print("error : the transition (" + src_state + ", " + symbol + ", ...) already exists.")
            return

        self.transitions[src_state].append((symbol, dst_state))

    def __str__(self):
        ret = "Finate Aautomate :\n"
        ret += "   - alphabet   : '" + self.alphabet + "'\n"
        ret += "   - init       : " + str(self.init) + "\n"
        ret += "   - finals     : " + str(self.finals) + "\n"
        ret += "   - states (%d) :\n" % (len(self.states))
        for state in self.states:
            ret += "       - (%s)" % (state)
            if len(self.transitions[state]) is 0:
                ret += ".\n"
            else:
                ret += ret + ":\n"
                for (sym, dest) in self.transitions[state]:
                    ret += ret + "          --(%s)--> (%s)\n" % (sym, dest)
        return ret

    def run(self, word):
        current_state = self.init

        i = 0
        for symbol in word:
            print("configuration : (" + current_state + ", " + word[i:] + ")")
            next_state = self.dst_state(current_state, symbol)

            if next_state is None:
                return False
    
            current_state = next_state
            i = i+1
    
        if current_state in self.finals:
            print("ending on final state '" + current_state + "'.")
            return True
        return False
    
if __name__ == '__main__':
    # instanciate the ADF that recognize word which contains "a" symbol
    a = DFA("aaaabbbba")
    # States
    a.add_state("0")
    a.add_state("1", True)
    # initial state
    a.init = "0"
    a.add_transition("0", "a", "1")
    a.add_transition("0", "b", "0")
    a.add_transition("1", "a", "1")
    a.add_transition("1", "b", "1")
    print(a)
    print(a.run("ababaa"))


