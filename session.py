# coding: utf-8
get_ipython().magic(u'run readdata.py')
a = read_WDBCdata();
a = read_WDBCdata('data.csv');
b = a.acquire_data()
b[0]
b[1]
cl1 = b[0][b[1]==9]
np.shape(cl1)
np.shape(b[0])
cl1 = b[0][b[1]==0]
np.shape(cl1)
np.shape(b[0])
cl2 = b[0][b[1]==1]
np.shape(cl2)
cl1 = np.hstack(-cl1,np.ones(cl1.shape[0],1))
cl21 = np.hstack(-cl1,np.ones(cl1.shape[0],1))
np.ones(cl1.shape[0],1)
cl21 = np.hstack(-cl1,np.ones((cl1.shape[0],1)))
cl1.shape
cl1.shape[0]
bg = np.ones((cl1.shape[0],1))
bg.shape
po = np.hstack(cl1,bg)
po = np.hstack((cl1,bg))
po
cla1 = np.hstack((-cl1,np.ones((cl1.shape[0],1))))
cla1 = np.hstack((-cl1,bg))
cla1 = np.hstack(-cl1,bg)
cla1 = np.hstack(-1*cl1,bg)
cle1 = -cl
cle1 = -cl1;
cle1 = 0-cl1
np.shape(cl1)
np.multiply(1,cl1);
np.multiply(*1,cl1);
np.multiply(-1,cl1);
cla1 = np.hstack((cl1.multiply(-1),np.ones((cl1.shape[0],1))))
cla1 = np.hstack((np.multiply(cl1,-1),np.ones((cl1.shape[0],1))))
negcl1 = np.multiply(cl1,-1);
clw1 = np.hstack((negcl1,np.ones((cl1.shape[0],1))))
negcl1.shape
cl1
np.shape(cl1)
clw1 = np.hstack((cl1,np.ones((cl1.shape[0],1))))
clw1 = np.hstack((cl1,-1*np.ones((cl1.shape[0],1))))
clw1
clw2 = np.hstack((cl2,-1*np.ones((cl1.shape[0],1))))
clw2 = np.hstack((cl2,-1*np.ones((cl2.shape[0],1))))
clw2
clw2 = clw2*-1
clw2  =np.multiply(clw2,-1)
clw2
clw2
clw2 = np.hstack((cl2,-1*np.ones((cl2.shape[0],1))))
clw2
0-clw2
np.zeros(clw2.shape)-clw2
import numpy
np.zeros(clw2.shape)-clw2
a = np.zeros(clw2.shape)
a-clw2
a.shape
clw2.shape
a-clw2
np.subtract(a,clw2)
get_ipython().magic(u'history ')
a = read_WDBCdata('data.csv');
a.write_data()
get_ipython().magic(u'run readdata.py')
a = read_WDBCdata('data.csv');
a = read_WDBCdata('data.csv');
get_ipython().magic(u'run readdata.py')
a = read_WDBCdata('data.csv');
get_ipython().magic(u'run readdata.py')
a = read_WDBCdata('data.csv');
get_ipython().magic(u'run readdata.py')
a = read_WDBCdata('data.csv');
b = a.acquire_data();
b
cl1 = b[0][b[1]==0]
cl2 = b[0][b[1]==1]
clw1 = np.hstack((cl1,-1*np.ones((cl1.shape[0],1))))
clw2 = np.hstack((cl2,-1*np.ones((cl2.shape[0],1))))
clw2 = -clw2
clw1
clw2
fin_dat = np.vstack(clw1,clw2)
fin_dat = np.vstack((clw1,clw2))
fin_dat.shape
fin_dat
fin_dat[:][30]
fin_dat[:,30]
A = fin_dat;
b = -np.ones(A.shape[0])
b
from cvxopt import matrix,solvers
A = matrix(A)
b = matrix(b)
A.shape()
A.shape
c = np.zeros(31);
c
c = matrix(c)
sol = solvers.lp(c,A,b)
print(sol['x'])
get_ipython().system(u'ls -F --color ')
get_ipython().magic(u'cd ..')
get_ipython().system(u'ls -F --color ')
get_ipython().magic(u'run linearseperabilitytest.py')
get_ipython().magic(u'run linearseperabilitytest.py')
po = LStest()
po = LStest(a,b)
po = LStest(a,b)
get_ipython().magic(u'run linearseperabilitytest.py')
po = LStest(a,b)
get_ipython().magic(u'hist ')
get_ipython().magic(u'hist > hist.txt')
get_ipython().system(u'ls -F --color ')
get_ipython().magic(u'hist ')
a = hist
a
get_ipython().magic(u'hist ')
get_ipython().magic(u'save session 1to123')
