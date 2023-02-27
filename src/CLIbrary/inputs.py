from colorama import Fore, Back, Style
from datetime import datetime

from .outputs import *

# INPUT HANDLING

def strIn(stringHandler={}) -> str: # String input.
	handler = {}

	handler["request"] = "Insert a string"
	handler["addedChars"] = ": "
	handler["allowedChars"] = []

	handler["allowedAnswers"] = []
	handler["allowedStyle"] = Fore.CYAN
	handler["blockedAnswers"] = []
	handler["noSpace"] = False
	handler["fixedLength"] = 0

	handler["verification"] = False

	handler["verbose"] = False

	handler.update(stringHandler)

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

	lengthString = ""

	try:
		if handler["fixedLength"] > 0:
			lengthString = Back.GREEN + Fore.MAGENTA + "[" + str(handler["fixedLength"]) + "]" + Style.RESET_ALL + " "
	except:
		handler["fixedLength"] = 0

	while True:
		try:
			rawAnswer = str(input(allowedString + lengthString + handler["request"] + handler["addedChars"]))

			if handler["verbose"]:
				output({"type": "verbose", "string": "VERBOSE, INPUT: " + rawAnswer})

			answer = rawAnswer.lower()

			if handler["fixedLength"] != 0 and len(answer) != handler["fixedLength"]:
				output({"type": "error", "string": "LENGTH ERROR"})
				continue

			reloadFlag = False
			for char in blockedChars:
				if char in answer:
					output({"type": "error", "string": "CHARACTER ERROR"})
					reloadFlag = True
					break

			if reloadFlag:
				continue

			if answer in handler["blockedAnswers"]:
				output({"type": "error", "string": "ANSWER ERROR"})
				continue

			if handler["allowedAnswers"] == [] or answer in handler["allowedAnswers"]:
				if not handler["verification"]:
					return answer

				else:
					verificationHandler = {}

					for key in handler:
						verificationHandler[key] = handler[key]

					verificationHandler["verification"] = False
					verificationHandler["request"] = "Verification"
					
					if answer == strIn(verificationHandler):
						return answer
					
					else:
						output({"type": "error", "string": "VERIFICATION ERROR"})
						continue
			
			output({"type": "error", "string": "SYNTAX ERROR"})

		except(EOFError, KeyboardInterrupt):
			output({"type": "error", "string": "KEYBOARD ERROR"})
		
		except:
			output({"type": "error", "string": "ERROR"})

def dateIn(dateHandler={}) -> str: # Date input.
	handler = {}

	handler["request"] = "Insert a date"
	handler["addedChars"] = " [YYYY-MM-DD]: "

	handler["verbose"] = False

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
			output({"type": "verbose", "string": "VERBOSE, INPUT: " + answer})

		try: # From an answer of Eduard Stepanov on https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
			if answer != datetime.strptime(answer, "%Y-%m-%d").strftime('%Y-%m-%d'):
				raise(ValueError)

			return answer
		
		except(ValueError):
			pass
		
		output({"type": "error", "string": "DATE FORMAT ERROR"})

def boolIn(boolHandler={}) -> bool: # Bool input.
	handler = {}

	handler["request"] = "Insert a boolean state"
	handler["addedChars"] = " [y/n]: "

	handler["verbose"] = False

	handler.update(boolHandler)

	strHandler = {}
	strHandler["request"] = handler["request"]
	strHandler["addedChars"] = handler["addedChars"]
	strHandler["allowedAnswers"] = ["y", "n"]
	strHandler["noSpace"] = True
	answer = strIn(strHandler)

	if handler["verbose"]:
		output({"type": "verbose", "string": "VERBOSE, INPUT: " + answer})
	
	if answer == "y":
		return True
		
	else:
		return False

def numIn(numberHandler={}) -> "int, float": # Number input.
	# Automatically recognizes wether the input is a float or an integer.

	handler = {}

	handler["request"] = "Insert a number"
	handler["addedChars"] = ": "
	handler["allowedRange"] = []
	handler["allowedTypes"] = ["int", "float"]
	handler["round"] = -1

	handler["verbose"] = False

	handler.update(numberHandler)

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
			rawAnswer = str(input(rangeString + handler["request"] + handler["addedChars"]))

			if handler["verbose"]:
				output({"type": "verbose", "string": "VERBOSE, INPUT: " + rawAnswer})
			
			if rawAnswer != "":
				answer = float(rawAnswer)

				if len(handler["allowedRange"]) == 2:
					if answer < handler["allowedRange"][0] or answer > handler["allowedRange"][1]:
						output({"type": "error", "string": "RANGE ERROR"})
						continue
				
				if int(answer) == answer and "int" in handler["allowedTypes"]:
					return int(answer)
				
				elif "float" in handler["allowedTypes"]:
					try:
						if handler["round"] > -1:
							return round(answer, int(handler["round"]))
					
					except:
						pass

					return answer

			output({"type": "error", "string": "SYNTAX ERROR"})
				
		except(ValueError):
			output({"type": "error", "string": "VALUE ERROR"})

		except(EOFError, KeyboardInterrupt):
			output({"type": "error", "string": "KEYBOARD ERROR"})

		except:
			output({"type": "error", "string": "ERROR"})

# LISTS HANDLING

def listCh(listHandler={}): # List choice.
	handler = {}

	handler["list"] = []
	handler["request"] = "Choose from list"
	
	handler.update(listHandler)

	if len(handler["list"]) == 0:
		answer = None
		
	elif len(handler["list"]) == 1:
		answer = handler["list"][0]
	
	else:
		for singleItem in handler["list"]:
			print(str(handler["list"].index(singleItem)) + ": " + str(singleItem))
			
		numberHandler = {}
		numberHandler["request"] = handler["request"]
		numberHandler["allowedRange"] = [0, len(handler["list"]) - 1]
		numberHandler["allowedTypes"] = ["int"]
		
		answer = handler["list"][numIn(numberHandler)] # type: ignore
			
	return answer