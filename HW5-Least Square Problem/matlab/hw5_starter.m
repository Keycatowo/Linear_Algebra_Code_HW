%% HW 
% For given points (1,6), (2,5), (3,7), (4,10)
% Please use least square method to find the cloest sol Ax=b, 
% and we name the sol beta. 
% It's ok to use inverse matrix operation in with A^(-1).
% It not allow to use lsqr.
x = [1;2;3;4];
y = [6;5;7;10];
% >>>>> Start of todo
b = ...
A = ...
beta = ...
% <<<<< End of todo
y_pred = A * beta;
disp(sprintf("y = %.3fx + %.3f", beta(1), beta(2)));
check = lsqr(A,y);
assert(max(abs(check-beta))<0.0001, "Wrong beta output");
figure(1);
scatter(x,y); hold on;
plot(x,y_pred);
xlim([0.5,4.5]); ylim([4,11]);
legend(["True Point", sprintf("y = %.3fx + %.3f", beta(1), beta(2))]);
%% Demo 1 
% It's a demo for realtion between bmi and diabetes target.
% We can plot it and see the equation.
T = readtable('../diabetes.csv');
x = table2array(T(:, 3));
y = table2array(T(:, 11));

figure(2);
mdl = fitlm(x,y);

plotAdded(mdl);

%% Demo 2
% It's a demo for 10 features, and 
% we use linear regration to find the equation.
T = readtable('../diabetes.csv');
X = table2array(T(:, 1:10));
y = table2array(T(:, 11));
coef = lsqr(X,y);
mdl = fitlm(X,y);
col_name = T.Properties.VariableNames;

disp("target=");
for kk = 1:length(coef)
    if coef(kk)>0
        disp(sprintf("\t+%.3f x %s", coef(kk), col_name{1,kk}));
    else
        disp(sprintf("\t%.3f x %s", coef(kk), col_name{1,kk}));
    end


end


