import math

def binarySearch(A, v, start, end):
	
	while start <= end:
		# print(f"start={start} & end={end}")
		mid = int(math.floor((start+end)/2))

		if A[mid] == v:
			return mid
		elif v < A[mid]:
			end = mid - 1
			return binarySearch(A,v,start,end)
		else:
			start = mid + 1
			return binarySearch(A,v,start,end)

	return -1


A = [int(i) for i in range(1,101)]
print(A)
find = 2
idx = binarySearch(A,find,0,len(A)-1)
print(f"{find} is located at index {idx}")