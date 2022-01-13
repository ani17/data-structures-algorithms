import math

def mergeSort(A):

	# If no more divison possible through mergeSort return to "merge" logic
	# for merging subarrays back into same array by repacing values
	# accordingly
	
	if len(A) < 2:
		return

	# Keep Dividing Array in to Left & Right Sub Arrays
	mid = int(math.floor(len(A) / 2))
	L = A[0 : mid]
	R = A[mid : ]

	mergeSort(L)
	mergeSort(R)
	merge(L,R,A)

	return A

def merge(L,R,A):
	# iterators for L, R and A
	i = 0
	l = 0
	r = 0

	# If iterators of both L & R have not reached the end
	#  compare values in both arrays and put the smaller value 
	#  back into the existing array
	while l < len(L) and r < len(R):
		if L[l] <= R[r]:
			A[i] = L[l]
			l += 1
		else:
			A[i] = R[r]
			r += 1
		i +=1

	# leftovers in L
	while l < len(L):
		A[i] = L[l]
		l += 1
		i += 1

	# leftovers in R
	while r < len(R):
		A[i] = R[r]
		r += 1
		i += 1

A = [5,4,3,2,1]
S = mergeSort(A)
print(S)
