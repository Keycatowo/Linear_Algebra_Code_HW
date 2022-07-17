%%
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

assert(all(all(B == ans_B)), "The row operation 3 get the wrong answer")
disp("PASS: test op3")

%% test matrix op 2
B = row_op2(A, 2, 1/2);
ans_B = [1 -2 1 5;
         1 0 1.5 -3;
         3 -1 2 -1
];

assert(all(all(B == ans_B)), "The row operation 2 get the wrong answer")
disp("PASS: test op2")

%% test matrix op 1
B = row_op1(A, 1, -2, 2);
B = row_op1(A, 1, -3, 3);
ans_B = [1 -2 1 5;
         0 4 1 -16;
         0 5 -1 -16
];

assert(all(all(B == ans_B)), "The row operation 1 get the wrong answer")
disp("PASS: test op1")

%% test get rank
rank = get_rank(A)
ans_rank = 3;

assert(rank==ans_rank, "The rank is wrong.")
disp("PASS: test rank")

