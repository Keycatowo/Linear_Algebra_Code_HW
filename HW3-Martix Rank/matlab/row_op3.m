function matrix = row_op3(matrix, row_1, row_2)
% exchange two rows(row_1, row_2) in matrix
    tmp = matrix(row_1,:);
    matrix(row_1,:) = matrix(row_2, :);
    matrix(row_2, :) = tmp;
end