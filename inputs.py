from colorama import init, Fore, Back, Style
init()

# INPUT HANDLING
						
def strIn(stringHandler={}) -> str: # String input.
	handler = {}

	handler["request"] = "Insert a string"
	handler["addedChars"] = ": "
	handler["allowedChars"] = []
	handler["allowedAnswers"] = []
	handler["blockedAnswers"] = []

	handler["errorStyle"] = Back.RED + Fore.WHITE

	handler["verbose"] = False
	handler["verboseStyle"] = Fore.CYAN

	handler.update(stringHandler)

	errorString = ""

	charactersRange = list(range(0, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 256))
	charactersRange.remove(32)
	blockedChars = [chr(char) for char in charactersRange]

	for char in handler["allowedChars"]:
		blockedChars.remove(char)

	while True:
		try:
			rawAnswer = str(input(errorString + handler["request"] + handler["addedChars"]))

			if handler["verbose"]:
				print(handler["verboseStyle"] + "VERBOSE, INPUT: " + rawAnswer + Style.RESET_ALL)

			answer = rawAnswer.lower()
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
				return answer
			
			errorString = handler["errorStyle"] + "SYNTAX ERROR" + Style.RESET_ALL + " "

		except(EOFError, KeyboardInterrupt):
			errorString = handler["errorStyle"] + "\nKEYBOARD ERROR" + Style.RESET_ALL + " "
		
		except:
			errorString = handler["errorStyle"] + "ERROR" + Style.RESET_ALL + " "
			
def boolIn(boolHandler={}) -> bool: # Bool input.
	handler = {}

	handler["request"] = "Insert a boolean state"
	handler["addedChars"] = " [Y/n]: "

	handler["verbose"] = False
	handler["verboseStyle"] = Fore.CYAN

	handler.update(boolHandler)

	strHandler = {}
	strHandler["request"] = handler["request"]
	strHandler["addedChars"] = handler["addedChars"]
	strHandler["allowedAnswers"] = ["y", "t", "n", "f", ""]
	answer = strIn(strHandler)

	if handler["verbose"]:
		print(handler["verboseStyle"] + "VERBOSE, INPUT: " + answer + Style.RESET_ALL)
	
	if answer in ["y", "t", ""]:
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
	handler["verboseStyle"] = Fore.CYAN

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

	while True:
		try:
			rawAnswer = str(input(errorString + rangeString + handler["request"] + handler["addedChars"]))

			if handler["verbose"]:
				print(handler["verboseStyle"] + "VERBOSE, INPUT: " + rawAnswer + Style.RESET_ALL)
			
			if rawAnswer != "":
				answer = float(handler["raw"])

				if len(handler["allowedRange"]) == 2:
					if answer < handler["allowedRange"][0] or answer > handler["allowedRange"][1]:
						errorString = handler["errorStyle"] + "RANGE ERROR" + Style.RESET_ALL + " "
						continue
				
				if int(answer) == answer and "int" in handler["allowedTypes"]:
					return int(answer)
				
				if "float" in handler["allowedTypes"]:
					return answer
			
			errorString = handler["errorStyle"] + "SYNTAX ERROR" + Style.RESET_ALL + " "
				
		except(ValueError):
			errorString = handler["errorStyle"] + "VALUE ERROR" + Style.RESET_ALL + " "

		except(EOFError, KeyboardInterrupt):
			errorString = handler["errorStyle"] + "\nKEYBOARD ERROR" + Style.RESET_ALL + " "

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