from math import floor

def heapify(A,i,n):
	largest = i
	l = (2*i) + 1
	r = 2*i
	
	#if(l > n or r > n):
		#return

	if(l < n and A[l] > A[i]):
		largest = l

	if(r < n and A[r] > A[largest]):
		largest = r

	if(largest is not i):
		A[i], A[largest] = A[largest], A[i]
		print A
		heapify(A,largest,n)


input_str = raw_input('Enter the numbers:')
nums = input_str.split(' ')

n = len(nums)

for i in range(0,len(nums)):
	nums[i] = int(nums[i])

A = nums

non_leaf_node_start = int(floor(n/2)) - 1

#Heap creation starts from largest non-leaf node, 
#as leaf nodes (length 1) are already sorted

print "Build Heap Starts"
for i in range(non_leaf_node_start, -1, -1):
	heapify(A,i,n)
print "Build Heap Ends"

print "Heap Sort starts"
for i in range(n-1, -1, -1):
	A[i], A[0] = A[0], A[i]
	heapify(A,0,i)
print "Heap Sort Ends"

print "Sorted Numbers:", A