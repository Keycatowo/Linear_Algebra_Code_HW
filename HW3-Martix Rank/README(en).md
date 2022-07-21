# Gaussian elimination method to find the rank of matrix

## row opreations of the matrix
There are three different types of row operations that can be performed by the matrix
1. Multiply a row of a matrix by a constant value and add it to another row.
2. Multiply a row of a matrix by a non-zero number.
3. Swap two rows in a matrix.


## Program Description
Please complete the **three different row operations of the matrix** and **find the rank** by Gaussian elimination method
+ [x] complete`matrix_op3()` -> This has been completed as an example
+ [ ] complete`matrix_op2()`
+ [ ] complete`matrix_op1()`
+ [ ] complete`get_rank()`

> A sample test is included for debugging purposes, and those who pass the sample test will receive 60% of the points, while the remaining 40% of the points will be provided by the unpublished test.

### Python execution example test
```
pytest test_hw3.py
```
Success Screen
![](https://i.imgur.com/Wc1u2P6.png)

Failure Screen
![](https://i.imgur.com/1207NOe.png)


### Matlab execution example test

Success Screen
```
PASS: test op3
PASS: test op2
PASS: test op1
PASS: test rank
```
Failure Screen
```
Error using test_hw3 (line 25)
The row operation 2 get the wrong answer
```


## Other Notes
+ The index used in the calculation of the first row **starts from 0 in Python** and **from 1 in Matlab**.
+ Please submit the following files when you submit your python assignments：`my_solve.py`
+ Please submit the following files when you submit your matlab assignments：`row_op1.m`, `row_op2.m`, `row_op3.m`, `get_rank.m`,