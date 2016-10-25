input_str = raw_input('Enter the numbers:')

nums = input_str.split(' ')

for i in range(len(nums)):
	nums[i] = int(nums[i])

A = nums

for j in range(len(nums)):
	key = A[j]
	i = j - 1

	while(i>=0 and A[i] > key):
		A[i+1] = A[i]
		i -= 1
		#print A

	A[i+1] = key

print "Sorted Array is:", A