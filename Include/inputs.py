from colorama import init, Fore
init()

# INPUTS HANDLING

def boolInput(request: str, addedChars=" [Y/n]: ") -> bool:
	errorString = ""

	while True:
		try:
			answer = input(errorString + request + addedChars).lower()
			
			if answer in ["y", "t", ""]:
				return True
				
			elif answer in ["n", "f"]:
				return False
			
			errorString = ""

		except(EOFError, KeyboardInterrupt):
			errorString = Fore.RED + "\nKEYBOARD ERROR " + Fore.RESET
			
def stringInput(request: str, addedChars=": ", allowedChars=[], blockedAnswers=[], allowedAnswers=[]) -> str:
	errorString = ""

	charactersRange = list(range(0, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 256))
	charactersRange.remove(32)
	blockedChars = [chr(char) for char in charactersRange]

	for char in allowedChars:
		blockedChars.remove(char)

	while True:
		try:
			answer = str(input(errorString + request + addedChars)).lower()
			
			reloadFlag = False

			for char in blockedChars:
				if char in answer:
					errorString = Fore.RED + "CHARACTER ERROR " + Fore.RESET
					reloadFlag = True
					break

			if answer in blockedAnswers:
				errorString = Fore.RED + "ANSWER ERROR " + Fore.RESET
				reloadFlag = True

			if reloadFlag:
				continue

			if answer != "":
				if allowedAnswers == [] or answer in allowedAnswers:
					return answer
			
			errorString = ""

		except(EOFError, KeyboardInterrupt):
			errorString = Fore.RED + "\nKEYBOARD ERROR " + Fore.RESET
		
		except:
			errorString = Fore.RED + "ERROR " + Fore.RESET
			
def numberInput(request: str, addedChars=": ", allowedRange=[]):
	# Automatically recognizes wether the input is a float or an integer.

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
			answer = input(errorString + rangeString + request + addedChars)
			
			if answer != "":
				number = float(answer)

				if len(allowedRange) == 2:
					if number < allowedRange[0] or number > allowedRange[1]:
						errorString = Fore.RED + "RANGE ERROR " + Fore.RESET
						continue
				
				if int(number) == number:
					return int(number)
				
				else:
					return number
				
		except(ValueError):
			errorString = Fore.RED + "VALUE ERROR " + Fore.RESET

		except(EOFError, KeyboardInterrupt):
			errorString = Fore.RED + "\nKEYBOARD ERROR " + Fore.RESET

		except:
			errorString = Fore.RED + "ERROR " + Fore.RESET

# LISTS HANDLING

def listChoice(choiceList: list):
	if len(choiceList) == 0:
		return None
		
	if len(choiceList) == 1:
		return choiceList[0]
	
	for singleItem in choiceList:
		print("\n" + str(choiceList.index(singleItem)) + ": " + str(singleItem))
		
	while True:
		choiceIndex = int(numberInput("\nChoose from list"))
		
		if choiceIndex in range(len(choiceList)):
			return choiceList[choiceIndex]