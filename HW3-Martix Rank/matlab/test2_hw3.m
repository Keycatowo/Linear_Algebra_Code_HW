%%
clear; clc;

A = [1 -2 1 5;
     2 0 3 -6;
     3 -1 2 -1
];


%% test matrix op 3
B = row_op3(A, 2, 3);
ans_B = [1 -2 1 5;
         3 -1 2 -1;
         2 0 3 -6
];

assert(max(max(abs(B - ans_B))) < 0.01, "The row operation 3 get the wrong answer")
disp("PASS: test op3")

%% test matrix op 2
B = row_op2(A, 3, -2);
ans_B = [1 -2 1 5;
         2 0 3 -6;
         -6 2 -4 2
];

assert(max(max(abs(B - ans_B))) < 0.01, "The row operation 2 get the wrong answer")
disp("PASS: test op2")

%% test matrix op 1
B = row_op1(A, 1, -2, 2);
B = row_op1(B, 1, -3, 3);
ans_B = [1 -2 1 5;
         0 4 1 -16;
         0 5 -1 -16
];

assert(max(max(abs(B - ans_B))) < 0.01, "The row operation 1 get the wrong answer")
disp("PASS: test op1")

%% test get rank
A = [
    1	 1	 1	0	1;
    0	 0	 0	0	0;
    1	 1	 1	0	0;
    1	 1	-1	0	0;
    1	-1	 1	1	0    
];

my_rank = get_rank(A)
ans_rank = rank(A)

assert(my_rank==ans_rank, "The rank is wrong.")
disp("PASS: test rank")

