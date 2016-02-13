#Name: Franz Joezepf C. Dinglasan
#Section: CMSC 128 AB-6L
#Student No: 2013-57046
#Date Written: February 13, 2016
#Program Description: Program consists of functions capable of
#converting numbers to words and vice versa. Also includes 
#delimiting of numbers.

#!/usr/bin/env python
import sys

#maps numbers to its corresponding words
def convertToWords(num):
	if(num == 0): sys.stdout.write("zero ")
	if(num == 1): sys.stdout.write("one ")		
	if(num == 2): sys.stdout.write("two ")
	if(num == 3): sys.stdout.write("three ")
	if(num == 4): sys.stdout.write("four ")
	if(num == 5): sys.stdout.write("five ")
	if(num == 6): sys.stdout.write("six ")
	if(num == 7): sys.stdout.write("seven ")
	if(num == 8): sys.stdout.write("eight ")
	if(num == 9): sys.stdout.write("nine ")
	if(num == 10): sys.stdout.write("ten ")
	if(num == 11): sys.stdout.write("eleven ")
	if(num == 12): sys.stdout.write("twelve ")
	if(num == 13): sys.stdout.write("thirteen ")
	if(num == 14): sys.stdout.write("fourteen ")
	if(num == 15): sys.stdout.write("fifteen ")
	if(num == 16): sys.stdout.write("sixteen ")
	if(num == 17): sys.stdout.write("seventeen ")
	if(num == 18): sys.stdout.write("eighteen ")
	if(num == 19): sys.stdout.write("nineteen ")
	if(num == 20): sys.stdout.write("twenty ")
	if(num == 30): sys.stdout.write("thirty ")
	if(num == 40): sys.stdout.write("forty ")
	if(num == 50): sys.stdout.write("fifty ")
	if(num == 60): sys.stdout.write("sixty ")
	if(num == 70): sys.stdout.write("seventy ")
	if(num == 80): sys.stdout.write("eighty ")
	if(num == 90): sys.stdout.write("ninety ")

#converts numbers into its word form 
def numToWords():
	zeroFlag = False
	num = int(input("\nInput number: "))

	if(num > 1000000):
		print("Number exceeds maximum value.\n")
		return

	if(num < 0):
		print("Number is below minimum value.\n")
		return

	sys.stdout.write("Output word: ")

	if(num == 0): zeroFlag = True
	#extract individual digits and print their value
	if(num >= 1000000):
		convertToWords(int(num/1000000))
		num = num - (int(num/1000000)*1000000)						
		sys.stdout.write("million ")

	if(num >= 1000):
		if(num < 1000000 and num >= 100000):
			convertToWords(int(num/100000))
			num = num - (int(num/100000)*100000)						
			sys.stdout.write("hundred ")

		if(num < 100000 and num >= 10000):
			if(num > 19000):
				convertToWords((int(num/10000)*10))
				num = num - (int(num/10000)*10000)
			else: 
				convertToWords(int(num/1000))
				num = num - (int(num/1000)*1000)

		if(num < 10000 and num >= 1000):
			convertToWords(int(num/1000))
			num = num - (int(num/1000)*1000)

		sys.stdout.write("thousand ")			

	if(num < 1000 and num >= 100):
		convertToWords(int(num/100))
		sys.stdout.write("hundred ")
		num = num - (int(num/100)*100)

	if(num < 100 and num >= 10):
		if(num > 19):
			convertToWords((int(num/10)*10))
			num = num - (int(num/10)*10)
		else: convertToWords(num)	

	if((num < 10 and num > 0) or zeroFlag):
		convertToWords(num)

	print("\n")

#maps words to its respective values
def convertToNum(word, num):
	if(word == "zero"): return 0
	if(word == "one"): return num + 1		
	if(word == "two"): return num + 2
	if(word == "three"): return num + 3
	if(word == "four"): return num + 4
	if(word == "five"): return num + 5
	if(word == "six"): return num + 6
	if(word == "seven"): return num + 7
	if(word == "eight"): return num + 8
	if(word == "nine"): return num + 9
	if(word == "ten"): return num + 10
	if(word == "eleven"): return num + 11
	if(word == "twelve"): return num + 12
	if(word == "thirteen"): return num + 13
	if(word == "fourteen"): return num + 14
	if(word == "fifteen"): return num + 15
	if(word == "sixteen"): return num + 16
	if(word == "seventeen"): return num + 17
	if(word == "eighteen"): return num + 18
	if(word == "nineteen"): return num + 19
	if(word == "twenty"): return num + 20
	if(word == "thirty"): return num + 30
	if(word == "forty"): return num + 40
	if(word == "fifty"): return num + 50
	if(word == "sixty"): return num + 60
	if(word == "seventy"): return num + 70
	if(word == "eighty"): return num + 80
	if(word == "ninety"): return num + 90
	if(word == "hundred"): return num * 100
	if(word == "thousand"): return num * 1000
	if(word == "million"): return num * 1000000

#gets the sum of the values extracted from the words
def getTotal(words):
	num = 0
	total = 0
	for text in words:
		num = convertToNum(text, num)
		if(num >= 1000): 
			total = total + num
			num = 0

	if(num < 1000): total = total + num	
	return total
	

#converts words to its number form
def wordsToNum():	
	word = input("\nInput word: ")	
	words = word.split()
	total = getTotal(words)

	if(total > 1000000):
		print("Number exceeds maximum value.\n")
		return

	sys.stdout.write("Output number: ")	
	print(str(total)+"\n")

#checks if input currency is allowed
def allowedCurrency(cur):
	if(cur == "PHP"): return True
	if(cur == "JPY"): return True
	if(cur == "USD"): return True
	return False

#converts words to its number form with currency
def wordsToCurrency():
	word = input("\nInput word: ")
	cur = input("Input Currency: ")	

	if(not allowedCurrency(cur)):
		print("Invalid currency.\n")
		return

	words = word.split()	
	total = getTotal(words)

	if(total > 1000000):
		print("Number exceeds maximum value.\n")
		return

	sys.stdout.write("Output Currency: ")
	sys.stdout.write(cur)
	print(str(total)+"\n")

#adds a delimiter on a number
def numberDelimited():
	foo = 0
	num = int(input("\nInput number: "))

	if(num > 1000000):
		print("Number exceeds maximum value.\n")
		return

	if(num < 0):
		print("Number is below minimum value.\n")
		return	

	deli = input("Input delimiter: ")
	jmp = int(input("Input no of jump: "))	
	asd = ""
	lst = asd.split()		

	if(jmp != 0): i = 0
	else: i = 1
	#inserts individual digit to a list
	if(num >= 1000000):
		foo = foo + 1
		lst.insert(i,int(num/1000000))
		if(jmp != i+1): i = i+1
		else: i = i+2
		num = num - (int(num/1000000)*1000000)

	if(num < 1000000 and num >= 100000):
		foo = foo + 1
		lst.insert(i,int(num/100000))
		if(jmp != i+1): i = i+1
		else: i = i+2
		num = num - (int(num/100000)*100000)

	if(num < 100000 and num >= 10000):
		foo = foo + 1
		lst.insert(i,int(num/10000))
		if(jmp != i+1): i = i+1
		else: i = i+2
		num = num - (int(num/10000)*10000)	

	if(num < 10000 and num >= 1000):
		foo = foo + 1
		lst.insert(i,int(num/1000))
		if(jmp != i+1): i = i+1
		else: i = i+2
		num = num - (int(num/1000)*1000)

	if(num < 1000 and num >= 100):
		foo = foo + 1
		lst.insert(i,int(num/100))
		if(jmp != i+1): i = i+1
		else: i = i+2
		num = num - (int(num/100)*100)

	if(num < 100 and num >= 10):
		foo = foo + 1
		lst.insert(i,int(num/10))
		if(jmp != i+1): i = i+1
		else: i = i+2
		num = num - (int(num/10)*10)

	if(num < 10):
		foo = foo + 1
		lst.insert(i,num)
	#insert the delimiter to its proper place
	jmp = foo - jmp
	lst.insert(jmp, deli);	
	sys.stdout.write("Output Delimited: ")

	for ele in lst:
		sys.stdout.write(str(ele))

	print("\n")	

#shows the menu in the terminal
def main():	
	ch = 0
	while(ch != 5):
		print("----------------------")
		print("[1] Num to Words")
		print("[2] Words to Num")
		print("[3] Words to Currency")
		print("[4] Number Delimited")
		print("[5] Exit")
		print("----------------------")
		ch = int(input("Choice: "))

		if(ch == 1): numToWords()
		if(ch == 2): wordsToNum()
		if(ch == 3): wordsToCurrency()
		if(ch == 4): numberDelimited()

main()		