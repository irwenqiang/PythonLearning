# ref from http://en.wikipedia.org/wiki/Gradient_descent
# find a local minimum of the function f(x)=x4−3x3+2, with derivative f'(x)=4x3−9x2
# From calculation, we expect that the local minimum occurs at x=9/4
 
x_old = 0
x_new = 6 # The algorithm starts at x=6
eps = 0.01 # step size
precision = 0.00001
 
def f_prime(x):
    return 4 * x**3 - 9 * x**2
 
while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new = x_old - eps * f_prime(x_old)
print "Local minimum occurs at ", x_new
