h=0.01;
T=50;

sigma=10;
b=8/3;
r=28;

X0 = [0; 0.1; 10];


N=T/h;

X = zeros(3,N);
X(:,1) = X0;

for j=2:N
    X(1,j) = X(1,j-1) + h * sigma * (-X(1,j-1) + X(2,j-1));
    X(2,j) = X(2,j-1) + h * (r * X(1,j-1) - X(2,j-1) - X(1,j-1)* ...
                             X(3,j-1));
    X(3,j) = X(3,j-1) + h * (-b*X(3,j-1) + X(1,j-1)*X(2,j-1));
end


hold off

plot3(X(1,:), X(2,:), X(3,:), 'k-.');

hold on

plot3(0,0,0,'bo');
plot3(sqrt(b*(r-1)), sqrt(b*(r-1)), r-1, 'bo');
plot3(-sqrt(b*(r-1)), -sqrt(b*(r-1)), r-1, 'bo');
