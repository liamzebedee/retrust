import sys
import math
import string
import operator
from optparse import OptionParser
from functools import reduce

def load_data(filename):
	# This procedure loads relevant data into table T.
	# Table[i][1] denotes source of evidence
	# Table[i][2] denotes subject of evidence
	# Table[i][3] denotes (signed) amount of evidence. (positive amount means positive evidence and negative amount means negative evidence.)
	T = []
	separator = " "
	
	file = open(filename, "r")
	file.readline()
	# Assumed is that data set consists of 5 entries each row, where first and last entries are irrelevant. 
	for line in file:
		tmp = line.split(separator)
		T.append( [int(i) for i in tmp[1:-1] ])
	return T

def get_max(data):
    print(data)
    return [max(i) for i in data]

def get_theta(data):
	return max([data[i][2] for i in range(len(data))])

def get_evidence(data):
	# This procedure computes amount of positive and negative evidences only
	print("get evidence...")
	y = get_max([[data[i][j] for i in range(len(data))] for j in range(2)])
	Flow = [[[0,0] for i in range(y[0]+1)] for j in range(y[1]+1)]

	for row in data:
		val = row[-1]
		if val >= 0:
			Flow[row[0]][row[1]][0] += val
		else:
			Flow[row[0]][row[1]][1] += -1*val
	
	print("finished")
	return Flow

def get_opinion(data, constant):
	# first extract evidences from dataset 
	print("get evidence...")
	y = get_max([[data[i][j] for i in range(len(data))] for j in range(2)])
	Flow = [[[0,0,constant] for i in range(y[0]+1)] for j in range(y[1]+1)]

	for row in data:
		val = row[-1]
		if val >= 0:
			# add positive evidence
			Flow[row[0]][row[1]][0] += val
		else:
			# add negative evidence
			Flow[row[0]][row[1]][1] += -1*val
	
	print("finished")

	# Given evidence compute Evidence Based Opinions using uncertainty constant
	print("extract opinions...")	
	for i in range(len(Flow)):
		for j in range(len(Flow)):
			el = Flow[i][j]
			ev_sum_el = el[0]+el[1]+el[2]
			Flow[i][j][0] = float(el[0])/ev_sum_el
			Flow[i][j][1] = float(el[1])/ev_sum_el
			Flow[i][j][2] = float(el[2])/ev_sum_el
	print("finished")
	return Flow
		
def test_flow(flow):
	# Test for entries in flow, that have both positiev and negative evidence
	print("test for both neg and pos evidence")
	for row in flow:
		for el in row:
			if (el[0]!=0) and (el[1]!=0):
				print(el)
	print("test finished")

def otimes(ox, oy):
	# compute SL opinion x otimes opinion y
	return [ox[0]*oy[0], ox[0]*oy[1], ox[1]+ox[2]+ox[0]*oy[2]]

def oplus(ox, oy):
	# compute SL opinion x oplus opinion y
	div = ox[2]+oy[2]-ox[2]*oy[2]
	return [x/div for x in [ox[2]*oy[0]+oy[2]*ox[0], ox[2]*oy[1]+oy[2]*ox[1], ox[2]*oy[2]]]

def scalartimes(scalar, ox):
	# comput scalar mul
	div = scalar*(ox[0]+ox[1])+ox[2]
	return [x/div for x in [scalar*ox[0], scalar*ox[1], ox[2]]]

def boxtimes(ox, oy, func):
	#compute opinion x boxtimes opinion y given g(x) = func 
	scalar = func(ox)
	return scalartimes(scalar, oy)

def odot(ox, oy, theta, constant):
	scalar = (float(constant)/theta) * (ox[0]/ox[2])
	return scalartimes(scalar, oy)
	
def matrixtimes(A, B, plus=operator.add, times=operator.mul):
	# compute A.B using own functions for plus and mul
	# Default plus = +
	# Default mul = *
	return [[reduce(plus, list(map(times, A[i], [B[k][j] for k in range(len(B[0]))]))) for j in range(len(B))] for i in range(len(A))]
	
def matrixsquare(A, plus=operator.add, times=operator.mul):
	# compute A^2 using own functions for plus and mul
	# Default plus = +
	# Default mul = *
	return [[reduce(plus, list(map(times, A[i], [A[j][k] for k in range(len(A))]))) for i in range(len(A))] for j in range(len(A))]
	
def matrixplus(A, B, plus=operator.add):
	return [list(map(plus, A[i],B[i])) for i in range(len(A))]

def matrixgeo(A, pow, plus=operator.add, times=operator.mul):
	# compute A^pow using own functions for plus and mul
	# Default plus = +
	# Default mul = *
	R = A
	for i in range(pow-1):
		R = matrixplus(A, matrixtimes(R,A, plus, times), plus)
	return R

def matrixgeonew(A, pow, plus=operator.add, times=operator.mul):
	# compute A^pow using own functions for plus and mul
	# Default plus = +
	# Default mul = *
	# Set diagonal to zero.
	R = A
	for i in range(pow-1):
		R = matrixplus(A, matrixtimes(R,A, plus, times), plus)
		for j in range(len(R)):
			R[j][j] = [0.0, 0.0, 1.0]
	return R

	
def matrixpow(A, pow, plus=operator.add, times=operator.mul):
	# compute A^pow using own functions for plus and mul
	# Default plus = +
	# Default mul = *
	R = A
	for i in range(pow-1):
		R = matrixtimes(R,A, plus, times)
	return R

def matrixpownew(A, pow, plus=operator.add, times=operator.mul):
	# compute A^pow using own functions for plus and mul
	# Default plus = +
	# Default mul = *
	R = A
	for i in range(pow-1):
		R = matrixtimes(R,A, plus, times)
		for j in range(len(R)):
			R[j][j] = [0.0, 0.0, 1.0]
	return R

def func_belief(ox):
	# This function takes g(x) = x_b
	return ox[0]

def func_belief_sqrt(ox):
	# This function takes g(x) = sqrt(x_b)
	return math.sqrt(ox[0])

def distance(m1, m2):
	res = 0.0
	for i in range(len(m1)):
		for j in range(len(m1)):
			for k in range(3):
				res += abs(m1[i][j][k] - m2[i][j][k])
	return res

def matrixgeoconvtest(A, threshold, plus=operator.add, times=operator.mul):
	# Default plus = +
	# Default mul = *
	# Set diagonal to zero.
	t = threshold + 1.0
	R = A
	count = 0
	while (t > threshold and count < 100):
		count = count + 1
		Y = R
		R = matrixplus(A, matrixtimes(R,A, plus, times), plus)
		for j in range(len(R)):
			R[j][j] = [0.0, 0.0, 1.0]
		t = distance(Y , R)
	return R, count, t

# def finalfunctrust_converge(T, R, threshold, plus=operator.add, times=operator.mul):
# 	# Default plus = +
# 	# Default mul = *
# 	# Set diagonal to zero.
# 	t = threshold + 1.0
	
#     F = T
# 	count = 0
# 	while (t > threshold and count < 100):
# 		count = count + 1
		
#         # Y = R
        
#         # R = A + fixedpoint(R * A)
        
#         # F = T + fixedpoint(R * T)

# 		F = matrixplus(A, matrixtimes(R, A, plus, times), plus)
# 		for j in range(len(R)):
# 			R[j][j] = [0.0, 0.0, 1.0]
# 		t = distance(Y , R)
# 	return R, count, t

def extract_evidence(M, constant):
	return [[[constant*(M[i][j][0]/M[i][j][2]), constant*(M[i][j][1]/M[i][j][2])] for j in range(len(M[i]))] for i in range(len(M))]

def write_to_file(M, openfile):
	openfile.write("{")
	for i in range(len(M)):
		openfile.write("{")
		for j in range(len(M[i])):
			openfile.write("{")
			for k in range(len(M[i][j])-1):
				openfile.write(str(M[i][j][k]))
				openfile.write(",")
			openfile.write(str(M[i][j][-1]))
			openfile.write("},")
		openfile.write("},\n")
	openfile.write("}")