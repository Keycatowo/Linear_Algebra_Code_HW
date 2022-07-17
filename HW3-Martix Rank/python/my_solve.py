import numpy as np


def row_op3(matrix, row_1, row_2):
    """
        交換矩陣的兩個列(row_1, row_2)
    """
    matrix[[row_1, row_2]] = matrix[[row_2, row_1]]
    return matrix    
# %%
def row_op2(matrix, row_1, const_1):
    """
        將一矩陣的某一列(row_1)乘以一個不為0的數(const_1)
    """ 
    
    return matrix
    

#%%
def row_op1(matrix, row_1, const_1, row_2):
    """
        將一矩陣的某列(row_1)列乘以數值(const_1)加入另一列(row_2)
    """
    
    return matrix

#%%
def get_rank(matrix) -> int:  
    """
        Get the rank of the matrix.

    arg:
        martix(np.array): A 2d matrix.

    return:
        rank(int): The rank of the matrix. 
    """
    
    return rank


