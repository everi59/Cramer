import numpy as np


def cramer_function(a, b):
    n = len(b)
    det_a = np.linalg.det(a)

    if det_a == 0:
        raise ValueError("Определитель матрицы равен нулю.")

    solutions = np.zeros(n, dtype=complex)

    for i in range(n):
        ai = a.copy()
        ai[:, i] = b
        det_ai = np.linalg.det(ai)
        solutions[i] = det_ai / det_a

    return solutions


a = np.array([[1, 2, 3+1j], [0, 1-2j, 4], [5, 6, 0]], dtype=complex)
b = np.array([6+4j, 4, 3], dtype=complex)
try:
    print(cramer_function(a, b))
except ValueError as e:
    print(e)
