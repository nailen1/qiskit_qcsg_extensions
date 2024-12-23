from .external_functions import set_initial, set_input_qubits, set_f_s, set_f_c, set_measure_on_s, set_measure_on_c, set_the_oracle, draw_qc, set_job_on_simulator, extend_counts
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
        self.full = self.set_oracle(include_input=True)
        self.draw = self.draw_qc()
        self.draw_full =self.draw_qc_full()

    def set_initial(self):
        qc_initial = set_initial()
        return qc_initial

    def reset_input(self):
        qc = set_input_qubits(self.a, self.b)
        return qc

    def set_f_s(self, include_input=False):
        qc = self.reset_input() if include_input else self.set_initial()
        qc = set_f_s(qc)
        self.xor = qc
        return qc
    
    def set_f_c(self, include_input=False):
        qc = self.reset_input() if include_input else self.set_initial()
        qc = set_f_c(qc)
        self.toffoli = qc
        return qc
    
    def set_measure_s(self, include_input=False):
        qc = self.reset_input() if include_input else self.set_initial()
        qc = set_measure_on_s(qc)
        return qc

    def set_measure_c(self, include_input=False):
        qc = self.reset_input() if include_input else self.set_initial()
        qc = set_measure_on_c(qc)
        return qc

    def set_oracle(self, include_input=False):
        qc = self.reset_input() if include_input else self.set_initial()
        qc_oracle = set_the_oracle(qc)
        self.f = qc_oracle
        return qc_oracle
    
    def draw_qc(self):
        dct = {
            'initial': draw_qc(self.initial),
            'input': draw_qc(self.input),
            'xor': draw_qc(self.xor),
            'toffoli': draw_qc(self.xor),
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

    def run(self):
        job = set_job_on_simulator(self.full)
        self.job = job
        self.result = job.result()
        self.counts = self.result.get_counts()
        return job
    
    def plot(self):
        if not hasattr(self, 'counts'):
            raise ValueError('You need to run the circuit first: self.run()')
        extended_counts = extend_counts(counts=self.counts)
        output = plot_histogram(extended_counts)
        return output
    
    