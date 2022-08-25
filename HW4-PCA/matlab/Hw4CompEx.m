% EECS2050 Linear Algebra
% Computer assignment for HW#4
% Principal value decomposition
% Due Aug 15, 2022
% Prof. Yi-Wen Liu


clear; close all
N = 50; % number of datapoints in 2D
rng(1);% random seed

% randomly create two correlated columns
A = randn(N,2);
B = [0.5 0.5; 0.6 -0.1];
X = A*B;

figure(1);
plot(X(:,1), X(:,2),'x');
grid on; pbaspect([1 1 1])

% Next, let us find a change of coordinates to diagonalize the covariance matrix.
mu = mean(X);
X_new = X - repmat(mu,N,1);

% >>>> TODO: Use diagonalization to get the pinciple axes.
% Q is the eigenvector"s"
% eg. Q(:,1) is the first eigenvector 
% D is diagonal matrix with eigenvalues

Sigma = 1/N* X_new' * X_new; % expected value of the covariance matrix
[Q,D] = eig(Sigma); % <----- This line is the key step for diagonalization.
prinAxes = Q*sqrt(D);

% <<< End of TODO

%%  Decorrelation by projecting onto principal components, and add the mean back.
Y = X_new*Q + repmat(mu,N,1);
figure(1); hold on;
plot(Y(:,1), Y(:,2),'.');

% Draw the principle axes
h1 = line(mu(1)+[0 prinAxes(1,1)],mu(2)+[0 prinAxes(2,1)],'color','k');
h2 = line(mu(1)+[0 prinAxes(1,2)],mu(2)+[0 prinAxes(2,2)],'color','k');
set(h1,'linewidth',2);
set(h2,'linewidth',2);

% set to aspect ratio to 1:1
set(gcf,'position',[400 300 500 500]); 
set(gca,'position',[0.1 0.1 0.8 0.8]);
set(gca,'xlim',[-3 3]);
set(gca,'ylim',[-3 3]);


%% Total Error with Principle components
% When we project the points on different axes, 
% we will get different errors.
% This part will show you the total errors 
% when we project the points on the two principle components.

m_axe1 = prinAxes(2,1) / prinAxes(1,1);
m_axe2 = prinAxes(2,2) / prinAxes(1,2);

figure(2);
% plot Errors with Axe1
subplot(121);
scatter(X(:,1), X(:,2),'x');
hold on; grid on; pbaspect([1 1 1]); 

line([-3 3],[-3*m_axe1 3*m_axe1],'color','#A2142F');
dis_sum = 0;
for kk = 1:N
    P = X(kk, 1:2);
    x0 = P(1); y0 = P(2);
    
    [dis, x1, y1] = get_error(x0, y0, m_axe1);
    scatter(x0,y0,"green");
    scatter(x1,y1,"green");
    dis_sum = dis_sum + dis;
    h1 = line([x0, x1], [y0, y1], "color", "#4DBEEE");
    set(h1,'linewidth',0.1);
%     pause;
end
title(["Total Error with PC_1", num2str(dis_sum)]);
xlim([-2, 2]);
ylim([-2, 2]);
pbaspect([1 1 1]);

% plot Errors with Axe2
subplot(122);
scatter(X(:,1), X(:,2),'x');
hold on; grid on; 

line([-3 3],[-3*m_axe2 3*m_axe2],'color','#A2142F');

% calculate the total errors
dis_sum = 0;
for kk = 1:N
    P = X(kk, 1:2);
    x0 = P(1); y0 = P(2);
    
    [dis, x1, y1] = get_error(x0, y0, m_axe2);
    scatter(x0,y0,"green");
    scatter(x1,y1,"green");
    dis_sum = dis_sum + dis;
    h1 = line([x0, x1], [y0, y1], "color", "#4DBEEE");
    set(h1,'linewidth',0.1);
%     pause;
end
title(["Total Error with PC_2", num2str(dis_sum)]);
xlim([-2, 2]);
ylim([-2, 2]);
pbaspect([1 1 1]);

%% Total Error with arbitary axes
% This part will show you how the total Error change 
% when we change the axes.
% NOTE: If you feel the process is too slow, 
%       you can reduce the size N or num_degrees.

num_degrees = 100; % how many graphs we calculate

thetas = linspace(0,2*pi, num_degrees);
figure(3);
for jj=1:length(thetas)
    hold off;
    scatter(X(:,1), X(:,2),'x');
    hold on; grid on;

    % Rotate the axes
    theta = thetas(jj);
    [a_x, a_y] = pol2cart(theta, 3);
    [b_x, b_y] = pol2cart(theta + pi, 3);
    m_k = a_y/ a_x;
    line([a_x, b_x], [a_y b_y],'color','#A2142F');
    
    % calculate the total errors
    dis_sum = 0;
    for kk = 1:N
        P = X(kk, 1:2);
        x0 = P(1); y0 = P(2);
        
        [dis, x1, y1] = get_error(x0, y0, m_k);
        scatter(x0,y0,"green");
        scatter(x1,y1,"green");
        dis_sum = dis_sum + dis;
        h1 = line([x0, x1], [y0, y1], "color", "#4DBEEE");
        set(h1,'linewidth',0.1);
    end
    title(["Total Error", num2str(dis_sum)]);
    
    xlim([-2, 2]);
    ylim([-2 2]);
%     pause;
    drawnow;
end


