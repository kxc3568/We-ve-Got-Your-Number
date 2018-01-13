#considered operations include - 
#addition (a+b), subtraction (a-b), multiplication (axb), division (a/b), 
#exponentiation (a^b), logarithms (log_a(b)), concatenation (ab), factorials (a!)

#factorals are not applied in the same way the others are as it is a unary operator
#considers every factorial up to 20! to account for solutions such as 12!/(5!*8!), but accounts for solutions such as 31!/30! by checking for a difference of 1

import math

def doTwo(num1, num2): #return two lists - one for numbers, one for solutions to those numbers
	nums1 = num1[0]
	nums2 = num2[0]
	sols1 = num1[1]
	sols2 = num2[1]
	generated = [[],[]]

	#addition
	current = nums1+nums2
	solfact = sols1+'+'+sols2
	generated[0].append(current)
	generated[1].append(solfact)
	applyFact(generated,current,solfact)

	#subtraction
	current = int(math.fabs(nums2-nums1))
	if current not in generated[0]:
		if nums2 > nums1:
			solfact = sols2+'-'+sols1
			generated[0].append(current)
			generated[1].append(solfact)
		else:
			solfact = sols1+'-'+sols2
			generated[0].append(current)
			generated[1].append(solfact)
		applyFact(generated,current,solfact)

	#multiplication
	current = nums1*nums2
	if current not in generated[0]:
		solfact = sols1+'x'+sols2
		generated[0].append(current)
		generated[1].append(solfact)
		applyFact(generated,current,solfact)

	#division, not sure how precision works
	current = float(nums1)/nums2
	if current not in generated[0]:
		solfact = sols1+'/'+sols2
		generated[0].append(current)
		generated[1].append(solfact)
		applyFact(generated,current,solfact)

	current = float(nums2)/nums1
	if current not in generated[0]:
		solfact = sols2+'/'+sols1
		generated[0].append(current)
		generated[1].append(solfact)
		applyFact(generated,current,solfact)

	#exponentiation
	try:
		current = int(math.pow(nums1,nums2))
		if current not in generated[0]:
			solfact = sols1+'^'+sols2
			generated[0].append(current)
			generated[1].append(solfact)
			applyFact(generated,current,solfact)
	except Exception as e:
		pass

	try:
		current = int(math.pow(nums2,nums1))
		if current not in generated[0]:
			solfact = sols2+'^'+sols1
			generated[0].append(current)
			generated[1].append(solfact)
			applyFact(generated,current,solfact)
	except Exception as e:
		pass
	
	#logarithm, not sure how precision works
	try:
		current = math.log(nums1,nums2)
		if current not in generated[0]:
			solfact = 'log_'+sols1+'('+sols2+')'
			generated[0].append(current)
			generated[1].append(solfact)
			applyFact(generated,current,solfact)
	except Exception as e:
		pass
	try:
		current = math.log(nums2,nums1)
		if current not in generated[0]:
			solfact = 'log_'+sols2+'('+sols1+')'
			generated[0].append(current)
			generated[1].append(solfact)
			applyFact(generated,current,solfact)
	except Exception as e:
		pass
	
	#concatenation
	if nums1 != 0:
		current = nums1*10+nums2
		if current not in generated[0]:
			solfact = sols1+sols2
			generated[0].append(current)
			generated[1].append(solfact)
			applyFact(generated,current,solfact)
	if nums2 != 0:
		current = nums2*10+nums1
		if current not in generated[0]:
			solfact = sols2+sols1
			generated[0].append(current)
			generated[1].append(solfact)
			applyFact(generated,current,solfact)

	return generated

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

def applyFact(generated, current, solfact):
	if current > 2 and int(current) == current:
		while current <= 20:
			solfact = '('+solfact+')!'
			if factorial[current] not in generated[0]:
				generated[0].append(factorial[current])
				generated[1].append(solfact)
			current = factorial[current]



factorial = [0]*21 #stores 0! to 99!
factorial[0] = 1
for i in range(1,21):
	factorial[i] = factorial[i-1]*i

l1 = [4,'4']
l2 = [5,'5']
print(doTwo(l1,l2))