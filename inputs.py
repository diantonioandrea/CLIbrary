from colorama import init, Fore
init()

# INPUTS HANDLING

def boolInput(request: str, addedChars=" [Y/n]: ") -> dict:
	output = {}
	errorString = ""

	while True:
		try:
			output["raw"] = input(errorString + request + addedChars).lower()
			
			if output["raw"] in ["y", "t", ""]:
				output["answer"] = True
				
			elif output["raw"] in ["n", "f"]:
				output["answer"] = False

			if "answer" in output:
				return output
			
			errorString = Fore.RED + "SYNTAX ERROR " + Fore.RESET

		except(EOFError, KeyboardInterrupt):
			errorString = Fore.RED + "\nKEYBOARD ERROR " + Fore.RESET
		
		except:
			errorString = Fore.RED + "ERROR " + Fore.RESET
			
def stringInput(request: str, addedChars=": ", allowedChars=[], blockedAnswers=[], allowedAnswers=[]) -> dict:
	output = {}
	errorString = ""

	charactersRange = list(range(0, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 256))
	charactersRange.remove(32)
	blockedChars = [chr(char) for char in charactersRange]

	for char in allowedChars:
		blockedChars.remove(char)

	while True:
		try:
			output["answer"] = str(input(errorString + request + addedChars)).lower()
			
			reloadFlag = False

			for char in blockedChars:
				if char in output["answer"]:
					errorString = Fore.RED + "CHARACTER ERROR " + Fore.RESET
					reloadFlag = True
					break

			if output["answer"] in blockedAnswers:
				errorString = Fore.RED + "ANSWER ERROR " + Fore.RESET
				reloadFlag = True

			if reloadFlag:
				continue

			if output["answer"] != "":
				if allowedAnswers == [] or output["answer"] in allowedAnswers:
					return output
			
			errorString = Fore.RED + "SYNTAX ERROR " + Fore.RESET

		except(EOFError, KeyboardInterrupt):
			errorString = Fore.RED + "\nKEYBOARD ERROR " + Fore.RESET
		
		except:
			errorString = Fore.RED + "ERROR " + Fore.RESET
			
def numberInput(request: str, addedChars=": ", allowedRange=[]) -> dict:
	# Automatically recognizes wether the input is a float or an integer.

	output = {}
	errorString = ""
	rangeString = ""

	try:
		if len(allowedRange) == 2:
			if allowedRange[0] > allowedRange[1]:
				allowedRange = []

			else:
				rangeString = Fore.CYAN + "[" + str(allowedRange[0]) + ", " + str(allowedRange[1]) + "] " + Fore.RESET

	except(IndexError, TypeError):
		allowedRange = []

	while True:
		try:
			output["raw"] = input(errorString + rangeString + request + addedChars)
			
			if output["raw"] != "":
				output["answer"] = float(output["raw"])

				if len(allowedRange) == 2:
					if output["answer"] < allowedRange[0] or output["answer"] > allowedRange[1]:
						errorString = Fore.RED + "RANGE ERROR " + Fore.RESET
						continue
				
				if int(output["answer"]) == output["answer"]:
					output["answer"] = int(output["answer"])
				
				return output
			
			errorString = Fore.RED + "SYNTAX ERROR " + Fore.RESET
				
		except(ValueError):
			errorString = Fore.RED + "VALUE ERROR " + Fore.RESET

		except(EOFError, KeyboardInterrupt):
			errorString = Fore.RED + "\nKEYBOARD ERROR " + Fore.RESET

		except:
			errorString = Fore.RED + "ERROR " + Fore.RESET

# LISTS HANDLING

def listChoice(choiceList: list) -> dict:
	output = {}
	output["list"] = choiceList

	if len(choiceList) == 0:
		output["answer"] = None
		
	elif len(choiceList) == 1:
		output["answer"] = choiceList[0]
	
	else:
		for singleItem in choiceList:
			print("\n" + str(choiceList.index(singleItem)) + ": " + str(singleItem))
			
		while True:
			choice = numberInput("\nChoose from list")
			
			if choice["answer"] in range(len(choiceList)):
				output["answer"] = choiceList[choice["answer"]]

	return output