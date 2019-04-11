#第一种方法
from numpy import*
x0=100
p=5
N=4
index_set=range(N+1)
x=zeros(len(index_set))
x[0]=x0
for e in index_set[1:]:
    i=e-1
    x[i+1]=x[i]+(p/100)*x[i]
print(x)
plt.plot(index_set,x,"-")
plt.xlabel('years')
plt.ylabel('amount')
plt.show()
#第二种方法
from numpy import*
x0=100
p=5
N=4
index_set=range(N+1)
index_set1=range(N+2)
x=zeros(len(index_set)+1)
x[0]=x0
for i in index_set:
    x[i+1]=x[i]+(p/100)*x[i]
print(x)
plt.plot(index_set1,x,"-")
plt.xlabel('years')
plt.ylabel('amount')
plt.show()