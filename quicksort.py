def quick_sort(A,start,end):
	if(start < end):
		pidx = partition(A,start,end)
		quick_sort(A,start,pidx-1)
		quick_sort(A,pidx+1,end)

def partition(A,start,end):
	pivot = A[end]
	i = start - 1 #saves the position of elements less than pivot

	for j in range(start,end):
		if(A[j] <= pivot):
			i += 1
			A[i], A[j] = A[j], A[i]

	A[i+1], A[end] = A[end], A[i+1] #When u reach the end Swap Pivot with i+1 position
	return i + 1					#as numbers upto i are all less than pivot(but not necessarily sorted)

input_str = raw_input('Enter the numbers:')
nums = input_str.split(' ')

for i in range(len(nums)):
	nums[i] = int(nums[i])

A = nums

quick_sort(A,0,len(A)-1)

print 'Sorted Array is', A