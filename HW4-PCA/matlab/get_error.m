function [dis, x1, y1] = get_error(x0, y0, m)
% Get Distance and Location with Line y=ax and Point (x0,y0)
%   dis: The minimal distance bewteen (x0,y0) and y=ax.
%   (x1, y1): The point in y=ax with minimal distance.
    x1 = (y0*m + x0)/(m*m+1);
    y1 = x1*m;
    dis = (x0 - x1)^2 + (y0 - y1)^2;
end