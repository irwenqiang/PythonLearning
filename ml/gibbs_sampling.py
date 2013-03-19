from scipy import*
from pylab import plot, show, figure, axis,step
from scipy import stats

#Task 1
# Generating 3000 samples using the Gibbs sampling method.
n = 3000
# set the mean and covariance parameters
mu = [0,0]
cov = [[4,1],[1,4]]

#define functions to return the mean of the full conditional distributions
def sam1(x):
   x1 = mu[0] + cov[0][1]/cov[1][1]*(x-mu[1])
   return x1
def sam2(x):
   x2 = mu[1] + cov[1][0]/cov[0][0]*(x-mu[0])
   return x2

#compute the covariance of the full conditional distributions
val1 = sqrt(cov[0][0]-cov[0][1]**2/cov[1][1])
val2 = sqrt(cov[1][1]-cov[1][0]**2/cov[0][0])
print val1, val2

X1 = zeros(n)
X2 = zeros(n)

#set the starting value of the Gibbs sampling algorithm
X1[0]=0
X2[0]=0

#run the Gibbs sampling algorithm for n steps
for i in xrange(1,n):
   X1[i]=random.normal(sam1(X2[i-1]), val1)
   X2[i]=random.normal(sam2(X1[i]), val2)

#Task 2
figure(0)
plot(X1[2900:],X2[2900:])
figure(1)
plot(X1,'b')
figure(2)
plot(X2,'r')
show()

#Task 3
#estimate the probability
prob = zeros(n)
prob[0]= (X1[0]>=0 and X2[0]>=0)

for i in xrange(1,n):
   prob[i]= prob[i-1]+(X1[i]>=0 and X2[i]>=0)
Prob = prob/xrange(1,n+1)

print(Prob)

figure(3)
plot(Prob)
axis([-200,n+200,0.2,0.6])
show()

#Task 4
#set the new covariance parameter, and repeat steps above
cov = [[4,2.8],[2.8,4]]



