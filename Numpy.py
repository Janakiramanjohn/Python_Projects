import numpy as np
import time
import sys

''' multi dimentional array'''
#size must be equal to get multi array
'''
a=np.array([(1,2,3,4),(4,5,6,7)])

print(type(a))
print(a)
'''

'''numpy faster than list in python'''

'''


s=range(100)
print(sys.getsizeof(1)*len(s))

d=np.arange(100) # same as range()
print(d.size*d.itemsize)
'''

#less memory and convenient
'''
size=100000

l=range(size)
l1=range(size)

start = time.time()

rs=[(x,y) for x,y in zip(l,l1)]
print((time.time()-start)*1000)
#print(rs)

a=np.arange(size)
a1=np.arange(size)

st=time.time()
rs=a+a1

print((time.time()-st)*1000)
'''
#numpy operations
#dimensions

'''
a=np.array([(1,4,8,8,9),(1,4,8,9,6)])

print(a.ndim) #number of dimensions

#size must be same for more dimensional arrays

print(a.itemsize) # number of bytes occupied by each elements


print(a.dtype)
'''


#numpy operations
'''
a=np.array([(1,2,4,5,7,8),(2,3,4,5,8,5)])

print(a.size) #total number of elements
print(a.shape) # shape of it (2X3) size must be same for columns
'''

'''
a=np.array([(1,2,3,4,5,6),(7,8,9,4,5,6)])

print(a)

#to change rows as column and columns as rows
a=a.reshape(6,2) # similar to a inverse

print(a)

'''


'''
a=np.array([(1,2,3,4,5,6),(7,8,9,4,5,6)])

print(a[0:2]) # print 0 to 2
print(a[0,2]) # print only 3 from first element

print(a[0:,3]) # print only third element from all the rows

a=np.array([(1,2,3,4,5,6),(7,8,9,4,5,6),(5,6,4,3,2,5)])


print(a[0:2,3]) # exclude element 3
'''



'''
a=np.linspace(1,3,10)

print(a)


'''

'''


a=np.array([12,45,89,56,78,23,56,48,76])


print(a)
print(min(a))
print(max(a))
print(sum(a))
print(round((sum(a)/a.size),2))

'''







'''

a=np.array([(12,45,89),(56,78,23),(56,48,76)])



print(a.sum(axis=1)) # sum

print(np.sqrt(a)) # square root

print(np.std(a)) # std deviation
'''


'''


a=np.array([(12,45,89),(56,78,23),(56,48,76)])


b=np.array([(12,45,89),(56,78,23),(56,48,76)])



print(a+b) #print array addition

print(a*b) # print array multiplication

print(a-b) # array subtraction

'''




'''
#concadination

print(np.vstack((a,b))) # vertical

print(np.hstack((a,b))) # horizantal

print(np.ravel(a))
'''








'''

import matplotlib.pyplot as plt





x=np.arange(0,3*np.pi,0.1)
print(x)


#y=np.sin(x)

#y=np.cos(x)

y=np.tan(x)

plt.plot(x,y)
plt.show()

'''




'''


a=np.array([1,2,3,4])

print(np.exp(a))

print(np.log(a))#natural log

print(np.log10(a)) # log base 10



'''



