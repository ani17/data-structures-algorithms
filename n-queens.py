def display(m):
	for i in range(0,N):
		print m[i]

def isAttacked(i,j):
	for itr in range(0,N):
		if 1 == matrix[i][itr] and itr is not j: # if position is same row
			return True
		if 1 == matrix[itr][j] and itr is not i: # if position is same row
			return True

	for x in range(0,N):
		for y in range(0,N):
			if x is not i and y is not j:
				if x+y == i+j and matrix[x][y] == 1: # if position is diagonal 1
					return True
				if x-y == i-j and matrix[x][y] == 1: # if position is diagonal 2
					return True

def Algo(m,row):
	if row == N:
		return True

	# row-wise check every column for safe position
	for col in range(0,N):
		if not isAttacked(row,col):
			m[row][col] = 1
			# print "========="
			# display(matrix)
			# print "========="
			if Algo(m,row+1):
				return True
			m[row][col] = 0 # if algo return false, backtrack | make previous marked queen = 0

	return False


N = int(raw_input('Enter the value of N:'))

matrix = []

# create N x N matrix
for i in range(0,N):
	row = [0 for x in range(0,N)]
	matrix.append(row)

print "Start-->"
display(matrix)

Algo(matrix,0)

print "Solution-->"
display(matrix)