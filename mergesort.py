from math import floor

def merge_sort(A):
	n = len(A)

	if(n < 2):
		return

	mid = int(floor(n/2))

	L = []
	R = []
	
	for i in range(0,mid):
		L.append(A[i])

	for i in range(mid,n):
		R.append(A[i])

	print "Left-->", L
	print "Right-->", R
	#exit(0)

	merge_sort(L)
	merge_sort(R)
	merge(A,L,R)



def merge(A,L,R):

	i = j = k = 0
	
	print "Inside Merge"
	print "Left-->", L
	print "Right-->", R
	#exit(0)

	while(i < len(L) and j < len(R)):
		
		if(L[i] < R[j]):
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
		k += 1

	while(i < len(L)):
		A[k] = L[i]
		i += 1
		k += 1

	while(j < len(R)):
		A[k] = R[j]
		j += 1
		k += 1

	print "After Merge:"
	print A


input_str = raw_input('Enter the numbers:')
nums = input_str.split(' ')

for i in range(len(nums)):
	nums[i] = int(nums[i])

A = nums

merge_sort(A)

print "Sorted Array is:", A