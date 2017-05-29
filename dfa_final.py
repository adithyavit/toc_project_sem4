
dicti = {'b':1,'m':2,'q':3,'c':4,'f':5,'g':6,'j':7,'p':8,'r':9,'k':0}
class DFA:
    	current_state = None;

	def __init__(self, states, alphabet, transition_function, start_state, accept_states):
	 self.states = states;
	 self.alphabet = alphabet;
	 self.transition_function = transition_function;
	 self.start_state = start_state;
	 self.accept_states = accept_states;
	 self.current_state = start_state;
	 return;

	def transition_to_state_with_input(self, input_value):
		#print ((self.current_state, input_value));
		if (self.current_state in self.accept_states):
			print ("The given input is "+str(dicti[self.current_state]));
			return;
		if ((self.current_state, input_value) not in self.transition_function.keys()):
			print ("This condition matched\n");
			self.current_state = None;
			return;
		self.current_state = self.transition_function[(self.current_state, input_value)];
		return;

	def in_accept_state(self):
	 return self.current_state in accept_states;

	def go_to_initial_state(self):
		self.current_state = self.start_state;
		return;

	def run_with_input_list(self, input_list):
	 	self.go_to_initial_state();
		for inp in input_list:
			self.transition_to_state_with_input(inp);
			continue;
		return self.in_accept_state();
	pass;



states = {'s','a','aa','b','c','d','e','ee','eee','eeee','f','g','h','i','ii','j','k','l','m','n','nn','o','q','r','p'};
alphabet = {'0','1'};

tf = dict();
tf[('ss','0')] = 's';
tf[('ss','1')] = 's';
tf[('s', '0')] = 'a';
tf[('s', '1')] = 'd';
tf[('a', '1')] = 'aa';
tf[('aa', '0')] = 'b';
tf[('aa', '1')] = 'c';
tf[('d', '0')] = 'e';
tf[('d', '1')] = 'h';
tf[('e', '1')] = 'ee';
tf[('ee', '1')] = 'eee';
tf[('eee', '1')] = 'eeee';
tf[('eeee', '0')] = 'f';
tf[('eeee', '1')] = 'g';
tf[('d', '1')] = 'h';
tf[('h', '0')] = 'i';
tf[('i', '1')] = 'ii';
tf[('ii', '0')] = 'j';
tf[('ii', '1')] = 'k';
tf[('h', '1')] = 'l';
tf[('l', '0')] = 'm';
tf[('l', '1')] = 'n';
tf[('n', '1')] = 'nn';
tf[('nn', '0')] = 'o';
tf[('o', '0')] = 'q';
tf[('o', '1')] = 'r';
tf[('nn', '1')] = 'p';
start_state = 's';
accept_states = {'b','c','f','g','j','k','m','q','r','p'};

d = DFA(states, alphabet, tf, start_state, accept_states);

inp_program = list('1111100 ');

print d.run_with_input_list(inp_program);
