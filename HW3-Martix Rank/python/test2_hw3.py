#%%
from my_solve import row_op1, row_op2, row_op3, get_rank
import numpy as np
from numpy.testing import assert_almost_equal
#%%
def test_op3():
    A = np.array([
        [1, -2, 1, 5],
        [2, 0, 3, -6],
        [3, -1, 2, -1]
    ], dtype=float)
    B = np.array([
        [1, -2, 1, 5],
        [3, -1, 2, -1],
        [2, 0, 3, -6]
    ], dtype=float)
    

    row_op3(A, 1, 2)
    assert_almost_equal(A, B), "The row operation 3 get the wrong answer"
    print("PASS: test op3")

#%%
def test_op2():
    A = np.array([
        [1, -2, 1, 5],
        [2, 0, 3, -6],
        [3, -1, 2, -1]
    ], dtype=float)
    B = np.array([
        [1, -2, 1, 5],
        [2, 0, 3, -6],
        [-6, 2, -4, 2]
    ], dtype=float)
    

    row_op2(A, 2, -2)
    assert_almost_equal(A, B), "The row operation 2 get the wrong answer"
    print("PASS: test op2")

# %%
def test_op1():
    A = np.array([
        [1, -2, 1, 5],
        [2, 0, 3, -6],
        [3, -1, 2, -1]
    ], dtype=float)
    B = np.array([
        [1, -2, 1, 5],
        [0, 4, 1, -16],
        [0, 5, -1, -16]
    ], dtype=float)
    

    row_op1(A, 0, -2, 1)
    row_op1(A, 0, -3, 2)
    assert_almost_equal(A, B), "The row operation 1 get the wrong answer"
    print("PASS: test op1")

#%%
def test_rank():
    A = np.array([
        [1,	 1,	 1,	0,	1],
        [0,	 0,	 0,	0,	0],
        [1,	 1,	 1,	0,	0],
        [1,	 1,	-1,	0,	0],
        [1,	-1,	 1,	1,	0]
    ], dtype=float)
    ans_rank = 4
    

    rank = get_rank(A)
    assert ans_rank == rank, "The rank is wrong."
    print("PASS: test rank")

# %%
