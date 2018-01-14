import sys
from logic import *

if __name__ == "__main__":
	args = sorted([sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]])
	num1 = [int(args[0]),args[0]]
	num2 = [int(args[1]),args[1]]
	num3 = [int(args[2]),args[2]]
	num4 = [int(args[3]),args[3]]

def wgyn(num1, num2, num3, num4):
	results = [[] for i in range(100)] #array for solutions for each number

	num1 = findFactCombos(num1) #adds factorials to the set of original numbers
	num2 = findFactCombos(num2)
	num3 = findFactCombos(num3)
	num4 = findFactCombos(num4)

	for i in range(len(num1[0])): #iterates through all combinations of original numbers and factorials of original numbers
		for j in range(len(num2[0])):
			for k in range(len(num3[0])):
				for l in range(len(num4[0])):
					twoByTwo(results,
						[num1[0][i],num1[1][i]],
						[num2[0][j],num2[1][j]],
						[num3[0][k],num3[1][k]],
						[num4[0][l],num4[1][l]],)
	for i in range(len(num1[0])):
		for j in range(len(num2[0])):
			for k in range(len(num3[0])):
				for l in range(len(num4[0])):
					threeByOne(results,
						[num1[0][i],num1[1][i]],
						[num2[0][j],num2[1][j]],
						[num3[0][k],num3[1][k]],
						[num4[0][l],num4[1][l]],)
	return results


#obtain solutions by dividing the set of numbers into two sets of two, then combining numbers made from those sets
def twoByTwo(results, num1, num2, num3, num4):
	list1 = doTwo(num1,num2)
	list2 = doTwo(num3,num4)
	doListTwo(results,list1,list2)

	if num2[0] != num3[0]: #don't need to calculate again if there are duplicates
		list1 = doTwo(num1,num3)
		list2 = doTwo(num2,num4)
		doListTwo(results,list1,list2)

	if num2[0] != num4[0]:
		list1 = doTwo(num1,num4)
		list2 = doTwo(num2,num3)
		doListTwo(results,list1,list2)

#obtain solutions by dividing the set of numbers into a set of three and a set of one, then combining numbers made from those sets
def threeByOne(results, num1, num2, num3, num4):
	l = [num1,num2,num3]
	doThree(results,l,num4)

	if num1[0] != num4[0]:
		l = [num2,num3,num4]
		doThree(results,l,num1)

	if num2[0] != num4[0]:
		l = [num1,num3,num4]
		doThree(results,l,num2)

	if num3[0] != num4[0]:
		l = [num1,num2,num4]
		doThree(results,l,num3)

results = wgyn(num1,num2,num3,num4)
count = 0
for i in range(len(results)):
	print(str(i+1)+': ')
	print(results[i])
	print('-------------------------------------------------------------')
	if len(results[i]) != 0:
		count += 1
print('solved: '+str(count))