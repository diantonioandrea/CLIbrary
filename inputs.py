from colorama import init, Fore, Back, Style
init()

# INPUT HANDLING

def strIn(stringHandler={}) -> str: # String input.
	handler = {}

	handler["request"] = "Insert a string"
	handler["addedChars"] = ": "
	handler["allowedChars"] = []

	handler["allowedAnswers"] = []
	handler["allowedStyle"] = Back.WHITE + Fore.CYAN
	handler["blockedAnswers"] = []
	handler["noSpace"] = False
	handler["fixedLength"] = 0

	handler["verification"] = False

	handler["errorStyle"] = Back.RED + Fore.WHITE

	handler["verbose"] = False
	handler["verboseStyle"] = Back.YELLOW

	handler["startingError"] = "" # For date input errors

	handler.update(stringHandler)

	errorString = handler["errorStyle"] + handler["startingError"] + Style.RESET_ALL + " "

	charactersRange = list(range(0, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 256))
	if not handler["noSpace"]:
		charactersRange.remove(32)
	blockedChars = [chr(char) for char in charactersRange]

	for char in handler["allowedChars"]:
		try:
			blockedChars.remove(char)
		except(ValueError):
			pass

	allowedString = ""

	if handler["allowedAnswers"] != []:
		try:
			allowedString = handler["allowedStyle"] + "[" + ", ".join(handler["allowedAnswers"]) + "]" + Style.RESET_ALL + " "
		except(TypeError):
			handler["allowedAnswers"] = []

	typeString = ""

	if handler["verbose"]:
		typeString = handler["verboseStyle"] + "STRING" + Style.RESET_ALL + " "
	
	lengthString = ""

	try:
		if handler["fixedLength"] > 0:
			lengthString = Back.GREEN + Fore.MAGENTA + "[" + str(handler["fixedLength"]) + "]" + Style.RESET_ALL + " "
	except:
		handler["fixedLength"] = 0

	while True:
		try:
			rawAnswer = str(input(errorString + typeString + allowedString + lengthString + handler["request"] + handler["addedChars"]))

			if handler["verbose"]:
				print(handler["verboseStyle"] + "VERBOSE, INPUT: " + rawAnswer + Style.RESET_ALL)

			answer = rawAnswer.lower()

			if handler["fixedLength"] != 0 and len(answer) != handler["fixedLength"]:
				errorString = handler["errorStyle"] + "LENGTH ERROR" + Style.RESET_ALL + " "
				continue

			reloadFlag = False
			for char in blockedChars:
				if char in answer:
					errorString = handler["errorStyle"] + "CHARACTER ERROR" + Style.RESET_ALL + " "
					reloadFlag = True
					break

			if reloadFlag:
				continue

			if answer in handler["blockedAnswers"]:
				errorString = handler["errorStyle"] + "ANSWER ERROR" + Style.RESET_ALL + " "
				continue

			if handler["allowedAnswers"] == [] or answer in handler["allowedAnswers"]:
				if not handler["verification"]:
					return answer

				else:
					verificationHandler = handler
					verificationHandler["verification"] = False
					verificationHandler["request"] = "Verification"
					
					if answer == strIn(verificationHandler):
						return answer
					
					else:
						errorString = handler["errorStyle"] + "VERIFICATION ERROR" + Style.RESET_ALL + " "
						continue
			
			errorString = handler["errorStyle"] + "SYNTAX ERROR" + Style.RESET_ALL + " "

		except(EOFError, KeyboardInterrupt):
			errorString = handler["errorStyle"] + "\nKEYBOARD ERROR" + Style.RESET_ALL + " "
		
		except:
			errorString = handler["errorStyle"] + "ERROR" + Style.RESET_ALL + " "

def dateIn(dateHandler={}) -> str: # Date input.
	handler = {}

	handler["request"] = "Insert a date"
	handler["addedChars"] = " [YYYY-MM-DD]: "

	handler["verbose"] = False
	handler["verboseStyle"] = Back.YELLOW

	handler.update(dateHandler)

	strHandler = {}
	strHandler["request"] = handler["request"]
	strHandler["addedChars"] = handler["addedChars"]
	strHandler["allowedChars"] = ["-"]
	strHandler["noSpace"] = True
	strHandler["fixedLength"] = 10

	while True:
		answer = strIn(strHandler)

		if handler["verbose"]:
			print(handler["verboseStyle"] + "VERBOSE, INPUT: " + answer + Style.RESET_ALL)

		splitDate = answer.split("-")

		if "-" in answer:
			if len(splitDate) == 3:
				if len(splitDate[0]) == 4 and len(splitDate[1]) == len(splitDate[2]) == 2:
					dateErrorFlag = False

					for dateElement in splitDate:
						try:
							if type(int(dateElement)) == int and int(dateElement) > 0:
								continue
								
							else:
								dateErrorFlag = True
						
						except:
							dateErrorFlag = True
							break
					
					if not dateErrorFlag:
						return answer
		
		strHandler["startingError"] = "DATE FORMAT ERROR"


def boolIn(boolHandler={}) -> bool: # Bool input.
	handler = {}

	handler["request"] = "Insert a boolean state"
	handler["addedChars"] = " [y/n]: "

	handler["verbose"] = False
	handler["verboseStyle"] = Back.YELLOW

	handler.update(boolHandler)

	strHandler = {}
	strHandler["request"] = handler["request"]
	strHandler["addedChars"] = handler["addedChars"]
	strHandler["allowedAnswers"] = ["y", "n"]
	strHandler["noSpace"] = True
	answer = strIn(strHandler)

	if handler["verbose"]:
		print(handler["verboseStyle"] + "VERBOSE, INPUT: " + answer + Style.RESET_ALL)
	
	if answer == "y":
		return True
		
	else:
		return False

def numIn(numberHandler={}): # Number input.
	# Automatically recognizes wether the input is a float or an integer.

	handler = {}

	handler["request"] = "Insert a number"
	handler["addedChars"] = ": "
	handler["allowedRange"] = []
	handler["allowedTypes"] = ["int", "float"]

	handler["errorStyle"] = Back.RED + Fore.WHITE

	handler["verbose"] = False
	handler["verboseStyle"] = Back.YELLOW

	handler.update(numberHandler)

	errorString = ""
	rangeString = ""

	try:
		if len(handler["allowedRange"]) == 2:
			if handler["allowedRange"][0] > handler["allowedRange"][1]:
				handler["allowedRange"] = []

			else:
				rangeString = Fore.GREEN + "[" + str(handler["allowedRange"][0]) + ", " + str(handler["allowedRange"][1]) + "] " + Style.RESET_ALL

	except(IndexError, TypeError):
		handler["allowedRange"] = []

	for types in handler["allowedTypes"]:
		if types not in ["int", "float"]:
			handler["allowedTypes"] = ["int", "float"]
			break
	
	if handler["allowedTypes"] == []:
		handler["allowedTypes"] = ["int", "float"]

	typeString = ""

	if handler["verbose"]:
		typeString = handler["verboseStyle"] + "NUMBER" + Style.RESET_ALL + " "

	while True:
		try:
			rawAnswer = str(input(errorString + typeString + rangeString + handler["request"] + handler["addedChars"]))

			if handler["verbose"]:
				print(handler["verboseStyle"] + "VERBOSE, INPUT: " + rawAnswer + Style.RESET_ALL)
			
			if rawAnswer != "":
				answer = float(rawAnswer)

				if len(handler["allowedRange"]) == 2:
					if answer < handler["allowedRange"][0] or answer > handler["allowedRange"][1]:
						errorString = handler["errorStyle"] + "RANGE ERROR" + Style.RESET_ALL + " "
						continue
				
				if int(answer) == answer and "int" in handler["allowedTypes"]:
					return int(answer)
				
				elif "float" in handler["allowedTypes"]:
					return answer
			
			errorString = handler["errorStyle"] + "SYNTAX ERROR" + Style.RESET_ALL + " "
				
		except(ValueError):
			errorString = handler["errorStyle"] + "VALUE ERROR" + Style.RESET_ALL + " "

		except(EOFError, KeyboardInterrupt):
			errorString = "\n" + handler["errorStyle"] + "KEYBOARD ERROR" + Style.RESET_ALL + " "

		except:
			errorString = handler["errorStyle"] + "ERROR" + Style.RESET_ALL + " "

# LISTS HANDLING

def listCh(listHandler={}): # List choice.
	handler = {}

	handler["list"] = []

	handler["errorStyle"] = Back.RED + Fore.WHITE

	handler.update(listHandler)

	if len(handler["list"]) == 0:
		answer = None
		
	elif len(handler["list"]) == 1:
		answer = handler["list"][0]
	
	else:
		for singleItem in handler["list"]:
			print(str(handler["list"].index(singleItem)) + ": " + str(singleItem))
			
		numberHandler = {}
		numberHandler["request"] = "Choose from list"
		numberHandler["allowedRange"] = [0, len(handler["list"]) - 1]
		numberHandler["allowedTypes"] = ["int"]
		
		answer = handler["list"][numIn(numberHandler)] # type: ignore
			
	return answer