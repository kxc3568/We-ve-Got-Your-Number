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

	for i in range(len(nums1)):
		for j in range(len(nums2)):

			#addition
			current = nums1[i]+nums2[j]
			if int(current) == current and current > 0 and current <= 100:
				current = int(current)
				solfact = sols1[i]+'+'+sols2[j]
				results[current-1].append(solfact)
				finalApplyFact(results,current,solfact)

			#subtraction
			if int(nums1[i]) == nums1[i] and int(nums2[j]) == nums2[j]:
				current = int(math.fabs(nums1[i]-nums2[j]))
				if current > 0 and current <= 100:
					if nums2[j] > nums1[i]:
						solfact = sols2[j]+'-('+sols1[i]+')'
					else:
						solfact = sols1[i]+'-('+sols2[j]+')'
					results[current-1].append(solfact)
					finalApplyFact(results,current,solfact)

			#multiplication
			current = nums1[i]*nums2[j]
			if int(current) == current and current > 0 and current <= 100:
				current = int(current)
				solfact = '('+sols1[i]+')x('+sols2[j]+')'
				results[current-1].append(solfact)
				finalApplyFact(results,current,solfact)

			#division
			current = float(nums1[i])/nums2[j]
			if int(current) == current and current > 0 and current <= 100:
				current = int(current)
				solfact = '('+sols1[i]+')/('+sols2[j]+')'
				results[current-1].append(solfact)
				finalApplyFact(results,current,solfact)
			current = float(nums2[j])/nums1[i]
			if int(current) == current and current > 0 and current <= 100:
				current = int(current)
				solfact = '('+sols2[j]+')/('+sols1[i]+')'
				results[current-1].append(solfact)
				finalApplyFact(results,current,solfact)

			#exponentiation
			try: #math overflow error
				current = math.pow(nums1[i],nums2[j])
				if int(current) == current and current > 0 and current <= 100:
					current = int(current)
					solfact = '('+sols1[i]+')^('+sols2[j]+')'
					results[current-1].append(solfact)
					finalApplyFact(results,current,solfact)
			except Exception as e:
				pass
			try: #math overflow error
				current = math.pow(nums2[j],nums1[i])
				if int(current) == current and current > 0 and current <= 100:
					current = int(current)
					solfact = '('+sols2[j]+')^('+sols1[i]+')'
					results[current-1].append(solfact)
					finalApplyFact(results,current,solfact)
			except Exception as e:
				pass
			
			#logarithm
			try: #division by zero error
				current = math.log(nums1[i],nums2[j])
				if int(current) == current and current > 0 and current <= 100:
					current = int(current)
					solfact = 'log_('+sols1[i]+')('+sols2[j]+')'
					results[current-1].append(solfact)
					finalApplyFact(results,current,solfact)
			except Exception as e:
				pass
			try:
				current = math.log(nums2[j],nums1[i])
				if int(current) == current and current > 0 and current <= 100:
					current = int(current)
					solfact = 'log_('+sols2[j]+')('+sols1[i]+')'
					results[current-1].append(solfact)
					finalApplyFact(results,current,solfact)
			except Exception as e:
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

def applyFact(generated, current, solfact): #continuously adds to generated set of numbers by doing a factorial on the result under a certain threshold (20)
	if current > 2 and int(current) == current:
		while current <= 20:
			solfact = '('+solfact+')!'
			if factorial[current] not in generated[0]:
				generated[0].append(factorial[current])
				generated[1].append(solfact)
			current = factorial[current]

def finalApplyFact(results, current, solfact):
	if current == 3 or current == 4:
		current = factorial[current]
		solfact = '('+solfact+')!'
		results[current-1].append(solfact)


factorial = [0]*21 #stores 0! to 99!
factorial[0] = 1
for i in range(1,21):
	factorial[i] = factorial[i-1]*i

l1 = [4,'4']
l2 = [5,'5']
l3 = [6,'6']
l4 = [7,'7']
results = [[] for i in range(100)]

first = doTwo(l1,l2)
second = doTwo(l3,l4)
doListTwo(results,first,second)
count = 0
for i in range(100):
	print(str(i+1)+':')
	print(results[i])
	if len(results[i]) != 0:
		count += 1
print('count: ' + str(count))