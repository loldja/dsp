import numpy as np
from numpy import matrix

A = matrix([[1,2,3],[2,7,4]])
B = matrix([[1,-1],[0,1]])
C = matrix([[5,-1],[9,1],[6,0]])
D = matrix([[3,-2,-1],[1,2,3]])
u = matrix([[6,2,-3,5]])
v = matrix([[3,5,-1,4]])
w = matrix([[1],[8],[0],[5]])

all_matrices = {'A':A,'B':B,'C':C,'D':D, 'u':u, 'v':v, 'w':w}
element = 1

##DIMENSIONS##
for key, matrix in all_matrices.items():
	print "The dimension of matrix", key, "is", matrix.shape
	if element in matrix.shape:
		print key, "is a vector"

alpha = 6
u = np.array(u)
v = np.array(v)
w = np.array(w)

##VECTOR OPERATIONS##
print "These are the answers to the problems given: "
print "2.1)",u + v
print "2.2)", u - v
print "2.3)", alpha*u
print "2.4)", u*v 		#I am not getting the np.dot(u,v) function to work properly?
print "2.5)", np.linalg.norm(u)


def add_matrix(mat1,mat2):
	if mat1.shape != mat2.shape:
		return "Dimensions not equal. Cannot add/subtract these matrices"
	else:
		return mat1+mat2

def sub_matrix(mat1,mat2):
	if mat1.shape != mat2.shape:
		return "Dimensions not equal. Cannot add/subtract these matrices"
	else:
		return mat1-mat2

##MATRIX OPERATIONS##
print "3.1)", add_matrix(A,C)
print "3.2)", sub_matrix(A,C.transpose())
print "3.3)", add_matrix(C.transpose(),3*D)
print "3.4)", B*A
print "3.5)", "# Columns in B are not equal to # rows in A transpose"
print "3.6)", "# Columns in B are not equal to # rows in C"
print "3.7)", C*B
print "3.8)", B*B*B*B
print "3.9)", A*A.transpose()
print "3.10)", D.transpose()*D