import numpy as np
from runtime.QuQCS.qucuQuantum.cuQuantumSim import cuQuantumSimulator
import cupy as cp

class TestCYGate:
    def test_cy_gate(self):
        nIndexBits = 2
        simulator = cuQuantumSimulator()
        simulator.create_qureg(nIndexBits)
        # initialize to |00> state
        simulator.init_zero_state()

        control = 0
        target = 1
        simulator.cy(control, target)

        amps_list = []
        for i in range(simulator.total_num_amps):
            amps_list.append(simulator.real[i] + 1j * simulator.imag[i])

        d_sv = cp.asarray(amps_list, dtype=cp.complex128)

        expected = np.asarray([
            1.0 + 0.0j, 0.0 + 0.0j,
            0.0 + 0.0j, 0.0 + 0.0j
        ], dtype=np.complex64)

        # check result

        if not cp.allclose(expected, d_sv):
            raise ValueError("results mismatch")

