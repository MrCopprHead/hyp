from scipy.stats import hypergeom, binom
import matplotlib.pyplot as plt
import numpy as np
import math

#n<N<M
#n = population of Type I
#N = sample size
#M = Total Population
#Would like to optimize N, the sample size, relative to M, the total population
#That gives us the smallest amount of error for the binom. approx.

accuracy = 0.01662        #target accuracy we would like to hit i.e 1%
again = True
keep = True
[M,n,N] = [1000,550,999]
typicals = []
while(again):
    keep = True
    if(N == 0):
        break
    p = (1.*N)/M
    hrv = hypergeom(M, n, N) #Hypergeometric random variable
    brv = binom(n,p)         #Binomial random variable
    x = np.arange(max(0,N-M+n),min(n,N))     #Support of random variables
    hpmf = hrv.pmf(x)
    bpmf = brv.pmf(x)
    for val in range(0,len(x)):
        if(hpmf[val] != 0):
            error = abs((hpmf[val] - bpmf[val]))
            if(error > accuracy):
                keep = False
                break
    if(keep):
        typicals.append(N)
    N = N - 1
print(len(typicals))
print((typicals[0],typicals[len(typicals) - 1]))

N = 500
p = (1.*N)/M
hrv = hypergeom(M, n, N)
brv = binom(n,p)
x = np.arange(max(0,N-M+n),min(n,N))     #Support of random variables
hpmf = hrv.pmf(x)
bpmf = brv.pmf(x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,hpmf, 'r.', label = 'Hypergeometric PDF')
ax.plot(x,bpmf, 'b.', label = 'Binomial PDF')
plt.show()
