h=0.001;
epsilon=.1;
T=10;

sigma=10;
b=8/3;
r=28;

M = 9;

D=sqrt(b*(r-1)) - 1;
D0=sqrt(b*(r-1));
Z0 = (r-1);

N=T/h;
X = zeros(3,N);


hold off
plot(D0,D0,'bo');
hold on
plot(-D0,-D0,'bo');
plot([-D0, D0], [0.5*D0, -0.5*D0], '--');

for l=0:M
    for k=0:M
        X0 = [-D+k/M*2*D; -D+l/M*2*D; Z0];
        X(:,1) = X0;

        stop = 0;
        for j=2:N
            if stop == 0
                X(1,j) = X(1,j-1) + h * sigma * (-X(1,j-1) + X(2,j-1));
                X(2,j) = X(2,j-1) + h * (r * X(1,j-1) - X(2,j-1) - X(1,j-1)* ...
                                     X(3,j-1));
                X(3,j) = X(3,j-1) + h * (-b*X(3,j-1) + X(1,j-1)*X(2,j- ...
                                                              1));
                if X(3,j) - Z0 > 0 && X(3,j) - Z0 < epsilon && abs(X(1,j)) < D0 && ...
                        abs(X(2,j)) < D0
                    if (X(1,1)+2*X(2,1)) > 0
                        plot (X(1,j),X(2,j),'k.');
                    else
                        plot (X(1,j),X(2,j),'r.');
                    end
                    stop = 1;
                end
            end
        end
    end
end