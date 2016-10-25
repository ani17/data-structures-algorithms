from math import floor

def BinarySearch(A,start,end,key):
	while(start <= end):
		mid = int(floor((start + end)/2))

		if(key == A[mid]):
			return mid
		elif(key < A[mid]):
			end = mid - 1
			BinarySearch(A,start,end,key)
		else:
			start = mid + 1
			BinarySearch(A,start,end,key)

	return -1


input_str = raw_input('Enter the Sorted List:')
key = int(raw_input('Enter the Key:'))

nums = input_str.split(' ')

for i in range(len(nums)):
	nums[i] = int(nums[i])

A = nums

index = BinarySearch(A,0,len(A)-1,key)

print index