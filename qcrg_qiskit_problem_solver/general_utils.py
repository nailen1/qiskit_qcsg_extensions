from qiskit_aer import AerSimulator


def simulate_quantum_circuit(qc, shots=1024):
    simulator = AerSimulator()
    job = simulator.run(qc, shots=shots)
    return job

simulate_qc = simulate_quantum_circuit

def get_result_from_job(job):
    result = job.result()
    return result

def get_result_of_simualtion(simulation):
    job = simulation
    result = get_result_from_job(job)
    return result

def extend_counts(counts):
    output_format = list(counts.keys())[0]
    n = len(output_format)
    possible_results = [format(i, f'0{n}b') for i in range(2**n)]
    extended_counts = {result: counts.get(result, 0) for result in possible_results}
    for key, value in counts.items():
        extended_counts[key] = value
    return extended_counts

def draw_qc(qc):
    return qc.draw(output='mpl')