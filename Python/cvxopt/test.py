from cvxopt import matrix, solvers, glpk
from numpy import array, dot



#actual numbers: primal
G = matrix([ [1., 0., 0., 1., 0.,  -1., 0., 0., -1., 0.,  -1., 0., 0., 0., 0., 0.],
             [1., 0., 0., 0., 1.,  -1., 0., 0., 0., -1.,  0., -1., 0., 0., 0., 0.],
             [0., 1., 0., 1., 0.,  0., -1., 0., -1., 0.,  0., 0., -1., 0., 0., 0.],
             [0., 1., 0., 0., 1.,  0., -1., 0., 0., -1.,  0., 0., 0., -1., 0., 0.],
             [0., 0., 1., 1., 0.,  0., 0., -1., -1., 0.,  0., 0., 0., 0., -1., 0.],
             [0., 0., 1., 0., 1.,  0., 0., -1., 0., -1.,  0., 0., 0., 0., 0., -1.] ])


h = matrix([7., 2., 4., 5., 8.,  -7., -2., -4., -5., -8.,  0., 0., 0., 0., 0., 0.,])
o = matrix([4., 7., 6., 8., 8., 9])

G = matrix([ [-1., 0., 0., -1., 0.,  -1., 0., 0., 0., 0., 0.],
             [-1., 0., 0., 0., -1.,  0., -1., 0., 0., 0., 0.],
             [0., -1., 0., -1., 0.,  0., 0., -1., 0., 0., 0.],
             [0., -1., 0., 0., -1.,  0., 0., 0., -1., 0., 0.],
             [0., 0., -1., -1., 0.,  0., 0., 0., 0., -1., 0.],
             [0., 0., -1., 0., -1.,  0., 0., 0., 0., 0., -1.] ])


h = matrix([-7., -2., -4., -5., -8.,  0., 0., 0., 0., 0., 0.,])
o = matrix([4., 7., 6., 8., 8., 9])


sol = solvers.lp(o,G,h)
print sol['x']
print sol['primal objective']
sol = glpk.ilp(o,G,h)
print sol[1]
##print sol[1]
##print sol[1][0]*4 + sol[1][1]*7 + sol[1][2]*6 + sol[1][3]*8 + sol[1][4]*8\
##      + sol[1][5]*9


G = matrix([ [-1., 0., 0., 0., 0., 0.],
             [0., -1., 0., 0., 0., 0.],
             [0., 0., -1., 0., 0., 0.],
             [0., 0., 0., -1., 0., 0.],
             [0., 0., 0., 0., -1., 0.],
             [0., 0., 0., 0., 0., -1.] ])

h = matrix([ 0., 0., 0., 0., 0., 0.,])
o = matrix([4., 7., 6., 8., 8., 9])

A = matrix([ [1., 0., 0., 1., 0.],
             [1., 0., 0., 0., 1.],
             [0., 1., 0., 1., 0.],
             [0., 1., 0., 0., 1.],
             [0., 0., 1., 1., 0.],
             [0., 0., 1., 0., 1.] ])
b = matrix([7., 2., 4., 5., 8])
##sol = solvers.lp(o,G,h,A,b)
##print sol['x']
##print sol['primal objective']

##print "answer", sol['x'][0]*4 + sol['x'][1]*7 + sol['x'][2]*6 + sol['x'][3]*8\
##      + sol['x'][4]*8 + sol['x'][5]*9
##print sol
sol = glpk.ilp(o,G,h,A,b)
print sol[1]
##print sol[1][0]*4 + sol[1][1]*7 + sol[1][2]*6 + sol[1][3]*8 + sol[1][4]*8\
##      + sol[1][5]*9