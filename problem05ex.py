#!user/nin/env python
# kiki 2018/09/22
# python problem05ex.py

def A2toA1(A1,A2):
	left = 0
	while left < len(A1) and len(A2) > 0:
		if A2[0] < A1[left]:
			A1.insert(left,A2[0])
			print (A1)
			del A2[0]
		left += 1
	A1.extend(A2)
	return A1

if __name__ == "__main__":
	A1 = [1,2,3]
	A2 = [4,5,6]
	A3 = [1,2,3]
	A4 = [1,9,18]
	A5 = [2,10,20]
	print (A2toA1(A3,A4))
