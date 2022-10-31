from colorama import init, Fore
init()

# INPUT HANDLING

def boolInput(boolHandler={}) -> dict:
	handler = {}

	handler["request"] = ""
	handler["addedChars"] = " [Y/n]: "

	handler["errorColor"] = Fore.RED

	if boolHandler == {}:
		return handler

	handler.update(boolHandler)

	errorString = ""

	while True:
		try:
			handler["raw"] = input(errorString + handler["request"] + handler["addedChars"]).lower()
			
			if handler["raw"] in ["y", "t", ""]:
				handler["answer"] = True
				
			elif handler["raw"] in ["n", "f"]:
				handler["answer"] = False

			if "answer" in handler:
				return handler
			
			errorString = handler["errorColor"] + "SYNTAX ERROR " + Fore.RESET

		except(EOFError, KeyboardInterrupt):
			errorString = handler["errorColor"] + "\nKEYBOARD ERROR " + Fore.RESET
		
		except:
			errorString = handler["errorColor"] + "ERROR " + Fore.RESET
			
def stringInput(stringHandler={}) -> dict:
	handler = {}

	handler["request"] = ""
	handler["addedChars"] = ": "
	handler["allowedChars"] = []
	handler["allowedAnswers"] = []
	handler["blockedAnswers"] = []

	handler["errorColor"] = Fore.RED

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
			handler["answer"] = str(input(errorString + handler["request"] + handler["addedChars"])).lower()
			
			reloadFlag = False

			for char in blockedChars:
				if char in handler["answer"]:
					errorString = handler["errorColor"] + "CHARACTER ERROR " + Fore.RESET
					reloadFlag = True
					break

			if handler["answer"] in handler["blockedAnswers"]:
				errorString = handler["errorColor"] + "ANSWER ERROR " + Fore.RESET
				reloadFlag = True

			if reloadFlag:
				continue

			if handler["answer"] != "":
				if handler["allowedAnswers"] == [] or handler["answer"] in handler["allowedAnswers"]:
					return handler
			
			errorString = handler["errorColor"] + "SYNTAX ERROR " + Fore.RESET

		except(EOFError, KeyboardInterrupt):
			errorString = handler["errorColor"] + "\nKEYBOARD ERROR " + Fore.RESET
		
		except:
			errorString = handler["errorColor"] + "ERROR " + Fore.RESET
			
def numberInput(numberHandler={}) -> dict:
	# Automatically recognizes wether the input is a float or an integer.

	handler = {}

	handler["request"] = ""
	handler["addedChars"] = ": "
	handler["allowedRange"] = []

	handler["errorColor"] = Fore.RED

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
				rangeString = Fore.CYAN + "[" + str(handler["allowedRange"][0]) + ", " + str(handler["allowedRange"][1]) + "] " + Fore.RESET

	except(IndexError, TypeError):
		handler["allowedRange"] = []

	while True:
		try:
			handler["raw"] = input(errorString + rangeString + handler["request"] + handler["addedChars"])
			
			if handler["raw"] != "":
				handler["answer"] = float(handler["raw"])

				if len(handler["allowedRange"]) == 2:
					if handler["answer"] < handler["allowedRange"][0] or handler["answer"] > handler["allowedRange"][1]:
						errorString = handler["errorColor"] + "RANGE ERROR " + Fore.RESET
						continue
				
				if int(handler["answer"]) == handler["answer"]:
					handler["answer"] = int(handler["answer"])
				
				return handler
			
			errorString = handler["errorColor"] + "SYNTAX ERROR " + Fore.RESET
				
		except(ValueError):
			errorString = handler["errorColor"] + "VALUE ERROR " + Fore.RESET

		except(EOFError, KeyboardInterrupt):
			errorString = handler["errorColor"] + "\nKEYBOARD ERROR " + Fore.RESET

		except:
			errorString = handler["errorColor"] + "ERROR " + Fore.RESET

# LISTS HANDLING

def listChoice(listHandler={}) -> dict:
	handler = {}

	handler["list"] = []

	handler["errorColor"] = Fore.RED

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
			
		numberHandler = numberInput()
		numberHandler["request"] = "Choose from list"
		numberHandler["allowedRange"] = [0, len(handler["list"]) - 1]

		numberHandler = numberInput(numberHandler)
		
		handler["answer"] = handler["list"][numberHandler["answer"]]
			
	return handler