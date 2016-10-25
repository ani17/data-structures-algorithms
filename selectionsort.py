input_str = raw_input('Enter the numbers:')

nums = input_str.split(' ')

for i in range(len(nums)):
	nums[i] = int(nums[i])

A = nums

for i in range(len(A)):
	min_idx = i

	for j in range(i+1,len(A)):
		
		if(A[j] < A[min_idx]):
			min_idx = j
			print "min_idx = ", min_idx

	A[i], A[min_idx] = A[min_idx], A[i]
	print A

print A