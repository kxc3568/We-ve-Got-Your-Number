#considered operations include - 
#addition (a+b), subtraction (a-b), multiplication (axb), division (a/b), exponentiation (a^b), 
#logarithms (log_a(b)), concatenation (ab), factorials (a!)


def doTwo(num1, num2): #return two lists - one for numbers, one for solutions to those numbers
	nums1 = num1[0]
	nums2 = num2[0]
	sols1 = num1[1]
	sols2 = num2[1]

	pass

def doListTwo(results,list1,list2):
	nums1 = list1[0]
	nums2 = list2[0]
	sols1 = list1[1]
	sols2 = list2[1]

	pass

def doThree(num1, num2, num3): #return two lists - one for numbers, one for solutions to those numbers
	nums1 = num1[0]
	nums2 = num2[0]
	nums3 = num3[0]
	sols1 = num1[1]
	sols2 = num2[1]
	sols3 = num3[1]

	pass

def doListThree(results, l, num):
	nums1 = l[0]
	nums2 = num[0]
	sols1 = l[1]
	sols2 = num[1]

	pass

factorial = [0]*100
factorial[0] = 1
for i in range(1,100):
	factorial[i] = factorial[i-1]*i