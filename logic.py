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
	try:
		current = float(nums1)/nums2
		if current not in generated[0]:
			solfact = sols1+'/'+sols2
			generated[0].append(current)
			generated[1].append(solfact)
			applyFact(generated,current,solfact)
	except Exception as e:
		pass

	try:
		current = float(nums2)/nums1
		if current not in generated[0]:
			solfact = sols2+'/'+sols1
			generated[0].append(current)
			generated[1].append(solfact)
			applyFact(generated,current,solfact)
	except Exception as e:
		pass

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
		if '!' not in sols1 and '!' not in sols2: #cannot concatenate numbers if they are the result of a factorial
			current = nums1*10+nums2
			if current not in generated[0]:
				solfact = sols1+sols2
				generated[0].append(current)
				generated[1].append(solfact)
				applyFact(generated,current,solfact)
	if nums2 != 0:
		if '!' not in sols1 and '!' not in sols2:
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
			try: #division by zero
				current = float(nums1[i])/nums2[j]
				if int(current) == current and current > 0 and current <= 100:
					current = int(current)
					solfact = '('+sols1[i]+')/('+sols2[j]+')'
					results[current-1].append(solfact)
					finalApplyFact(results,current,solfact)
			except Exception as e:
				pass
			try:
				current = float(nums2[j])/nums1[i]
				if int(current) == current and current > 0 and current <= 100:
					current = int(current)
					solfact = '('+sols2[j]+')/('+sols1[i]+')'
					results[current-1].append(solfact)
					finalApplyFact(results,current,solfact)
			except Exception as e:
				pass

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

def doThree(results, l, finalNum):
	num1 = l[0]
	num2 = l[1]
	num3 = l[2]

	doneTwo = doTwo(num1,num2)
	doneTwoNowThree(results,doneTwo,num3,finalNum)
	if num2 != num3:
		doneTwo = doTwo(num1,num3)
		doneTwoNowThree(results,doneTwo,num2,finalNum)
	if num1 != num2:
		doneTwo = doTwo(num2,num3)
		doneTwoNowThree(results,doneTwo,num1,finalNum)

	#triple concatenation then operation, 6 for each permutation of concatenation
	#if finalNum is a duplicate of one of the other 3, there may be duplicates in 3x1s
	isFactorial = False # check if any of the numbers being concatenated are the result of a factorial
	for i in range(len(l)):
		if '!' in l[i][1]:
			isFactorial = True
	if not isFactorial:
		concat = [num1[0]*100+num2[0]*10+num3[0],num1[1]+num2[1]+num3[1]]
		doConcat(results,concat,finalNum)
		if num2[0] != num3[0]:
			concat = [num1[0]*100+num3[0]*10+num2[0],num1[1]+num3[1]+num2[1]]
			doConcat(results,concat,finalNum)
		if num1[0] != num2[0]:
			concat = [num2[0]*100+num1[0]*10+num3[0],num2[1]+num1[1]+num3[1]]
			doConcat(results,concat,finalNum)
			if num1[0] != num3[0]:
				concat = [num2[0]*100+num3[0]*10+num1[0],num2[1]+num3[1]+num1[1]]
				doConcat(results,concat,finalNum)
		if num3[0] != num1[0]:
			concat = [num3[0]*100+num1[0]*10+num2[0],num3[1]+num1[1]+num2[1]]
			doConcat(results,concat,finalNum)
			if num1[0] != num2[0]:
				concat = [num3[0]*100+num2[0]*10+num1[0],num3[1]+num2[1],num1[1]]
				doConcat(results,concat,finalNum)

def doneTwoNowThree(results, doneTwo, num3, finalNum):
	dtNums = doneTwo[0]
	dtSols = doneTwo[1]
	if finalNum[0] > 2 and int(finalNum[0]) == finalNum[0]:
		finalNumIterate = int(finalNum[0])
		finalSolIterate = finalNum[1]
		while finalNumIterate < 20:
			finalNumIterate = factorial[finalNumIterate]
			finalSolIterate = '('+finalSolIterate+')!'
			finalNum.append(finalNumIterate)
			finalNum.append(finalSolIterate)

	for i in range(len(dtNums)):

		#operation for finalNum is addition or subtraction, accounts for other last operations if there is overlap
		current = dtNums[i]*num3[0]
		solfact = '('+dtSols[i]+')*'+num3[1]
		if current > 2 and current <= 20: #whether it should consider a factorial
			applyFinalNum(results,current,solfact,finalNum,4)
		else:
			applyFinalNum(results,current,solfact,finalNum,0)
			applyFinalNum(results,current,solfact,finalNum,2)
			applyFinalNum(results,current,solfact,finalNum,3)
		
		try:
			current = dtNums[i]/num3[0]
			solfact = '('+dtSols[i]+')/'+num3[1]
			if current > 2 and current <= 20:
				applyFinalNum(results,current,solfact,finalNum,4)
			else:
				applyFinalNum(results,current,solfact,finalNum,0)
				applyFinalNum(results,current,solfact,finalNum,2)
				applyFinalNum(results,current,solfact,finalNum,3)
		except Exception as e:
			pass

		try:
			current = math.pow(dtNums[i],num3[0])
			solfact = '('+dtSols[i]+')^'+num3[1]
			if current > 2 and current <= 20:
				applyFinalNum(results,current,solfact,finalNum,4)
			else:
				applyFinalNum(results,current,solfact,finalNum,0)
				applyFinalNum(results,current,solfact,finalNum,1)
				applyFinalNum(results,current,solfact,finalNum,3)
		except Exception as e:
			pass

		try:
			current = math.pow(num3[0],dtNums[i])
			solfact = num3[1]+'^('+dtSols[i]+')'
			if current > 2 and current <= 20:
				applyFinalNum(results,current,solfact,finalNum,4)
			else:
				applyFinalNum(results,current,solfact,finalNum,0)
				applyFinalNum(results,current,solfact,finalNum,1)
				applyFinalNum(results,current,solfact,finalNum,3)
		except Exception as e:
			pass

		try:
			current = math.log(dtNums[i],num3[0])
			solfact = 'log_('+dtSols[i]+')('+num3[1]+')'
			if current > 2 and current <= 20:
				applyFinalNum(results,current,solfact,finalNum,4)
			else:
				applyFinalNum(results,current,solfact,finalNum,0)
				applyFinalNum(results,current,solfact,finalNum,1)
				applyFinalNum(results,current,solfact,finalNum,2)
		except Exception as e:
			pass

		try:
			current = math.log(num3[0],dtNums[i])
			solfact = 'log_'+num3[1]+'('+dtSols[i]+')'
			if current > 2 and current <= 20:
				applyFinalNum(results,current,solfact,finalNum,4)
			else:
				applyFinalNum(results,current,solfact,finalNum,0)
				applyFinalNum(results,current,solfact,finalNum,1)
				applyFinalNum(results,current,solfact,finalNum,2)
		except Exception as e:
			pass

		#operation for finalNum is multiplication or division
		current = dtNums[i]+num3[0]
		solfact = dtSols[i]+'+'+num3[1]
		if current > 2 and current <= 20:
			applyFinalNum(results,current,solfact,finalNum,4)
		else:
			applyFinalNum(results,current,solfact,finalNum,1)
			applyFinalNum(results,current,solfact,finalNum,2)
			applyFinalNum(results,current,solfact,finalNum,3)

		if dtNums[i] > num3[0]:
			current = dtNums[i]-num3[0]
			solfact = dtSols[i]+'-'+num3[1]
			if current > 2 and current <= 20:
				applyFinalNum(results,current,solfact,finalNum,4)
			else:
				applyFinalNum(results,current,solfact,finalNum,1)
				applyFinalNum(results,current,solfact,finalNum,2)
				applyFinalNum(results,current,solfact,finalNum,3)
		else:
			current = num3[0]-dtNums[i]
			solfact = num3[1]+'-('+dtSols[i]+')'
			if current > 2 and current <= 20:
				applyFinalNum(results,current,solfact,finalNum,4)
			else:
				applyFinalNum(results,current,solfact,finalNum,1)
				applyFinalNum(results,current,solfact,finalNum,2)
				applyFinalNum(results,current,solfact,finalNum,3)

def doConcat(results,concat,finalNum):
	current = concat[0]-finalNum[0]
	if current > 0 and current <= 100:
		results[current-1].append(concat[1]+'-'+finalNum[1])
	try:
		current = concat[0]/finalNum[0]
		if int(current) == current and current > 0 and current <= 100:
			current = int(current)
			results[current-1].append(concat[1]+'/'+finalNum[1])
	except Exception as e:
		pass
	try:
		current = math.log(concat[0],finalNum[0])
		if int(current) == current and current > 0 and current <= 100:
			current = int(current)
			results[current-1].append('log_'+finalNum[1]+'('+concat[1]+')')
	except Exception as e:
		pass

def applyFact(generated, current, solfact): #continuously adds to generated set of numbers by doing a factorial on the result under a certain threshold (20)
	if current > 2 and int(current) == current or current == 0:
		current = int(current)
		while current != 1 and current <= 20:
			solfact = '('+solfact+')!'
			if factorial[current] not in generated[0]:
				generated[0].append(factorial[current])
				generated[1].append(solfact)
			current = factorial[current]

def finalApplyFact(results, current, solfact):
	if current == 3 or current == 4:
		current = int(current)
		current = factorial[current]
		solfact = '('+solfact+')!'
		results[current-1].append(solfact)

def applyFinalNum(results, current, solfact, finalNum, operation): #value of operation is index in [+ and -, x and /, ^, log, !] to figure out the final operation to be made
	for i in range(len(finalNum)//2):
		if operation == 4:
			while int(current) == current and current > 2 and current <= 20:
				applyFinalNum(results,current,solfact,finalNum,0)
				applyFinalNum(results,current,solfact,finalNum,1)
				applyFinalNum(results,current,solfact,finalNum,2)
				applyFinalNum(results,current,solfact,finalNum,3)
				current = int(current)
				current = factorial[current]
				solfact = '('+solfact+')!'

		elif operation == 0:
			finalCurrent = current+finalNum[2*i]
			if int(finalCurrent) == finalCurrent and finalCurrent > 0 and finalCurrent <= 100:
				finalCurrent = int(finalCurrent)
				results[finalCurrent-1].append(solfact+'+'+finalNum[2*i+1])
			finalCurrent = current-finalNum[2*i]
			if int(finalCurrent) == finalCurrent and finalCurrent > 0 and finalCurrent <= 100:
				finalCurrent = int(finalCurrent)
				results[finalCurrent-1].append(solfact+'-'+finalNum[2*i+1])
			finalCurrent = finalNum[2*i]-current
			if int(finalCurrent) == finalCurrent and finalCurrent > 0 and finalCurrent <= 100:
				finalCurrent = int(finalCurrent)
				results[finalCurrent-1].append(finalNum[2*i+1]+'-('+solfact+')')

		elif operation == 1:
			finalCurrent = current*finalNum[2*i]
			if int(finalCurrent) == finalCurrent and finalCurrent > 0 and finalCurrent <= 100:
				finalCurrent = int(finalCurrent)
				results[finalCurrent-1].append('('+solfact+')*'+finalNum[2*i+1])
			try:
				finalCurrent = current/finalNum[2*i]
				if int(finalCurrent) == finalCurrent and finalCurrent > 0 and finalCurrent <= 100:
					finalCurrent = int(finalCurrent)
					results[finalCurrent-1].append('('+solfact+')/'+finalNum[2*i+1])
			except Exception as e:
				pass
			try:
				finalCurrent = finalNum[2*i]/current
				if int(finalCurrent) == finalCurrent and finalCurrent > 0 and finalCurrent <= 100:
					finalCurrent = int(finalCurrent)
					results[finalCurrent-1].append(finalNum[2*i+1]+'/('+solfact+')')
			except Exception as e:
				pass

		elif operation == 2:
			try:
				finalCurrent = math.pow(current,finalNum[2*i])
				if int(finalCurrent) == finalCurrent and finalCurrent > 0 and finalCurrent <= 100:
					finalCurrent = int(finalCurrent)
					results[finalCurrent-1].append('('+solfact+')^'+finalNum[2*i+1])
			except Exception as e:
				pass
			try:
				finalCurrent = math.pow(finalNum[2*i],current)
				if int(finalCurrent) == finalCurrent and finalCurrent > 0 and finalCurrent <= 100:
					finalCurrent = int(finalCurrent)
					results[finalCurrent-1].append(finalNum[2*i+1]+'^('+solfact+')')
			except Exception as e:
				pass

		elif operation == 3:
			try:
				finalCurrent = math.log(current,finalNum[2*i])
				if int(finalCurrent) == finalCurrent and finalCurrent > 0 and finalCurrent <= 100:
					finalCurrent = int(finalCurrent)
					results[finalCurrent-1].append('log_('+solfact+')('+finalNum[2*i+1]+')')
			except Exception as e:
				pass
			try:
				finalCurrent = math.log(finalNum[2*i],solfact)
				if int(finalCurrent) == finalCurrent and finalCurrent > 0 and finalCurrent <= 100:
					finalCurrent = int(finalCurrent)
					results[finalCurrent-1].append('log_'+finalNum[2*i+1]+'('+solfact+')')
			except Exception as e:
				pass
			
def findFactCombos(num):
	val = num[0]
	combos = [val]
	combosSol = [num[1]]
	if val > 2 or val == 0:
		while val != 1 and val < 20:
			val = factorial[val]
			combos.append(val)
			combosSol.append('('+combosSol[len(combosSol)-1]+')!')
	return [combos, combosSol]


factorial = [0]*21 #stores 0! to 20!
factorial[0] = 1
for i in range(1,21):
	factorial[i] = factorial[i-1]*i