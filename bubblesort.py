input_str = raw_input('Enter the numbers:')

nums = input_str.split(' ')

for i in range(len(nums)):
	nums[i] = int(nums[i])

A = nums

for i in range(len(A)):
	for j in range(len(A) - i - 1):
		if(A[j] > A[j+1]):
			A[j+1], A[j] = A[j], A[j+1]

print A