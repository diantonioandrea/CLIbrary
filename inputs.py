from colorama import init, Fore, Back, Style
init()

# INPUT HANDLING

def boolIn(boolHandler={}) -> dict: # Bool input.
	handler = {}

	handler["request"] = ""
	handler["addedChars"] = " [Y/n]: "

	handler["errorStyle"] = Back.RED + Fore.WHITE

	handler["verbose"] = False
	handler["verboseStyle"] = Fore.CYAN

	if boolHandler == {}:
		return handler

	handler.update(boolHandler)

	errorString = ""

	while True:
		try:
			handler["raw"] = input(errorString + handler["request"] + handler["addedChars"])

			if handler["verbose"]:
				print(handler["verboseStyle"] + "VERBOSE, INPUT: " + handler["raw"] + Style.RESET_ALL)

			handler["raw"] = handler["raw"].lower()
			
			if handler["raw"] in ["y", "t", ""]:
				handler["answer"] = True
				
			elif handler["raw"] in ["n", "f"]:
				handler["answer"] = False

			if "answer" in handler:
				return handler
			
			errorString = handler["errorStyle"] + "SYNTAX ERROR" + Style.RESET_ALL + " "

		except(EOFError, KeyboardInterrupt):
			errorString = handler["errorStyle"] + "\nKEYBOARD ERROR" + Style.RESET_ALL + " "
		
		except:
			errorString = handler["errorStyle"] + "ERROR" + Style.RESET_ALL + " "
			
def strIn(stringHandler={}) -> dict: # String input.
	handler = {}

	handler["request"] = ""
	handler["addedChars"] = ": "
	handler["allowedChars"] = []
	handler["allowedAnswers"] = []
	handler["blockedAnswers"] = []

	handler["errorStyle"] = Back.RED + Fore.WHITE

	handler["verbose"] = False
	handler["verboseStyle"] = Fore.CYAN

	if stringHandler == {}:
		return handler

	handler.update(stringHandler)

	errorString = ""

	charactersRange = list(range(0, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 256))
	charactersRange.remove(32)
	blockedChars = [chr(char) for char in charactersRange]

	for char in handler["allowedChars"]:
		blockedChars.remove(char)

	while True:
		try:
			handler["raw"] = str(input(errorString + handler["request"] + handler["addedChars"]))

			if handler["verbose"]:
				print(handler["verboseStyle"] + "VERBOSE, INPUT: " + handler["raw"] + Style.RESET_ALL)

			handler["answer"] = handler["raw"].lower()
			
			reloadFlag = False

			for char in blockedChars:
				if char in handler["answer"]:
					errorString = handler["errorStyle"] + "CHARACTER ERROR" + Style.RESET_ALL + " "
					reloadFlag = True
					break

			if handler["answer"] in handler["blockedAnswers"]:
				errorString = handler["errorStyle"] + "ANSWER ERROR" + Style.RESET_ALL + " "
				reloadFlag = True

			if reloadFlag:
				continue

			if handler["answer"] != "":
				if handler["allowedAnswers"] == [] or handler["answer"] in handler["allowedAnswers"]:
					return handler
			
			errorString = handler["errorStyle"] + "SYNTAX ERROR" + Style.RESET_ALL + " "

		except(EOFError, KeyboardInterrupt):
			errorString = handler["errorStyle"] + "\nKEYBOARD ERROR" + Style.RESET_ALL + " "
		
		except:
			errorString = handler["errorStyle"] + "ERROR" + Style.RESET_ALL + " "
			
def numIn(numberHandler={}) -> dict: # Number input.
	# Automatically recognizes wether the input is a float or an integer.

	handler = {}

	handler["request"] = ""
	handler["addedChars"] = ": "
	handler["allowedRange"] = []

	handler["errorStyle"] = Back.RED + Fore.WHITE

	handler["verbose"] = False
	handler["verboseStyle"] = Fore.CYAN

	if numberHandler == {}:
		return handler

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

	while True:
		try:
			handler["raw"] = str(input(errorString + rangeString + handler["request"] + handler["addedChars"]))

			if handler["verbose"]:
				print(handler["verboseStyle"] + "VERBOSE, INPUT: " + handler["raw"] + Style.RESET_ALL)
			
			if handler["raw"] != "":
				handler["answer"] = float(handler["raw"])

				if len(handler["allowedRange"]) == 2:
					if handler["answer"] < handler["allowedRange"][0] or handler["answer"] > handler["allowedRange"][1]:
						errorString = handler["errorStyle"] + "RANGE ERROR" + Style.RESET_ALL + " "
						continue
				
				if int(handler["answer"]) == handler["answer"]:
					handler["answer"] = int(handler["answer"])
				
				return handler
			
			errorString = handler["errorStyle"] + "SYNTAX ERROR" + Style.RESET_ALL + " "
				
		except(ValueError):
			errorString = handler["errorStyle"] + "VALUE ERROR" + Style.RESET_ALL + " "

		except(EOFError, KeyboardInterrupt):
			errorString = handler["errorStyle"] + "\nKEYBOARD ERROR" + Style.RESET_ALL + " "

		except:
			errorString = handler["errorStyle"] + "ERROR" + Style.RESET_ALL + " "

# LISTS HANDLING

def listCh(listHandler={}) -> dict: # List choice.
	handler = {}

	handler["list"] = []

	handler["errorStyle"] = Back.RED + Fore.WHITE

	if listHandler == {}:
		return handler

	handler.update(listHandler)

	if len(handler["list"]) == 0:
		handler["answer"] = None
		
	elif len(handler["list"]) == 1:
		handler["answer"] = handler["list"][0]
	
	else:
		for singleItem in handler["list"]:
			print(str(handler["list"].index(singleItem)) + ": " + str(singleItem))
			
		numberHandler = numIn()
		numberHandler["request"] = "Choose from list"
		numberHandler["allowedRange"] = [0, len(handler["list"]) - 1]

		numberHandler = numIn(numberHandler)
		
		handler["answer"] = handler["list"][numberHandler["answer"]]
			
	return handler