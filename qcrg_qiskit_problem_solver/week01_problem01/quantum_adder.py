from .quantum_adder_utils import set_initial, set_input_qubits, set_f_s, set_f_c, set_measure_on_s, set_measure_on_c, set_the_oracle
from qcrg_qiskit_problem_solver.general_utils import simulate_quantum_circuit, extend_counts, draw_qc
from qiskit.visualization import plot_histogram

class QuantumAdder:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.initial = self.set_initial()
        self.input = self.reset_input()
        self.f_s = self.set_f_s()
        self.f_c = self.set_f_c()
        self.measure_s = self.set_measure_s()
        self.measure_c = self.set_measure_c()
        self.oracle = self.set_oracle()
        self.full = self.set_full_circuit()
        self.draw = self.draw_qc()
        self.draw_full =self.draw_qc_full()

    def set_initial(self):
        qc_initial = set_initial()
        return qc_initial

    def reset_input(self):
        qc = set_input_qubits(self.a, self.b)
        return qc

    def set_f_s(self, input=None):
        qc = self.set_initial() if input is None else input
        qc = set_f_s(qc)
        self.xor = qc
        return qc
    
    def set_f_c(self, input=None):
        qc = self.set_initial() if input is None else input
        qc = set_f_c(qc)
        self.toffoli = qc
        return qc
    
    def set_measure_s(self, input=None):
        qc = self.set_initial() if input is None else input
        qc = set_measure_on_s(qc)
        return qc

    def set_measure_c(self, input=None):
        qc = self.set_initial() if input is None else input
        qc = set_measure_on_c(qc)
        return qc

    def set_oracle(self, input=None):
        qc = self.set_initial() if input is None else input
        qc_oracle = set_the_oracle(qc)
        self.f = qc_oracle
        return qc_oracle
    
    def set_full_circuit(self):
        qc = self.reset_input()
        qc = self.set_oracle(qc)
        self.full = qc
        return qc
    
    def draw_qc(self):
        dct = {
            'initial': draw_qc(self.initial),
            'input': draw_qc(self.input),
            'xor': draw_qc(self.xor),
            'f_s': draw_qc(self.f_s),
            'toffoli': draw_qc(self.xor),
            'f_c': draw_qc(self.f_c),
            'measure_s': draw_qc(self.measure_s),
            'measure_c': draw_qc(self.measure_c),
            'oracle': draw_qc(self.oracle),
            'f': draw_qc(self.oracle),
            'full': draw_qc(self.full)
        }
        return dct
    
    def draw_qc_full(self):
        output = draw_qc(self.full)
        return output

    def simulate(self):
        simulation = simulate_quantum_circuit(self.full)
        self.simulation = simulation
        self.result = simulation.result()
        self.counts = self.result.get_counts()
        return simulation
    
    def plot(self):
        if not hasattr(self, 'counts'):
            raise ValueError('You need to run simulator the circuit first: self.simulate()')
        extended_counts = extend_counts(counts=self.counts)
        output = plot_histogram(extended_counts)
        return output
    
    