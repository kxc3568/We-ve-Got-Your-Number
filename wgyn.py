import sys
from . import logic

if __name__ == "__main__":
	args = sorted([sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]])
	num1 = args[0]
	num2 = args[1]
	num3 = args[2]
	num4 = args[3]

def wgyn(num1, num2, num3, num4):
	results = [[] for i in range(100)] #array for solutions for each number
	twoByTwo(results,num1,num2,num3,num4)
	threeByOne(results,num1,num2,num3,num4)
	return results


#obtain solutions by dividing the set of numbers into two sets of two, then combining numbers made from those sets
def twoByTwo(results, num1, num2, num3, num4):
	list1 = doTwo(num1,num2)
	list2 = doTwo(num3,num4)
	doListTwo(results,list1,list2)

	if num2 != num3: #don't need to calculate again if there are duplicates
		list1 = doTwo(num1,num3)
		list2 = doTwo(num2,num4)
		doListTwo(results,list1,list2)

	if num2 != num4:
		list1 = doTwo(num1,num4)
		list2 = doTwo(num2,num3)
		doListTwo(results,list1,list2)

#obtain solutions by dividing the set of numbers into a set of three and a set of one, then combining numbers made from those sets
def threeByOne(results, num1, num2, num3, num4):
	l = doThree(num1,num2,num3)
	doListThree(results,l,num4)

	if num1 != num4:
		l = doThree(num2,num3,num4)
		doListThree(results,l,num1)

	if num2 != num4:
		l = doThree(num1,num3,num4)
		doListThree(results,l,num2)

	if num3 != num4:
		l = doThree(num1,num2,num4)
		doListThree(results,l,num3)

print(wgyn(num1,num2,num3,num4))