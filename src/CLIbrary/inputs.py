from colorama import Fore, Back, Style
from datetime import datetime

from .outputs import *
from .settings import style

# INPUT HANDLING

def strIn(stringHandler={}) -> str: # String input.	
	handler = {}

	# Strings.
	handler["request"] = "String: " # The input request.
	handler["added"] = ": " # The set of added characters to the input request.

	# Lists.
	handler["allowedChars"] = [] # The list of allowed characters.
	handler["allowedAnswers"] = [] # The list of allowed answers.
	handler["blockedAnswers"] = [] # The list of blocked answers.

	# Bools.
	handler["space"] = True # Whether to allow the use of spaces.
	handler["empty"] = False # Whether to allow the input of empty strings.
	handler["verification"] = False # Whether to request verification.
	handler["verbose"] = False # Verbosity.

	# Integers.
	handler["fixedLength"] = 0

	# Updates the handler.
	handler.update(stringHandler)

	# Checks types and values.
	if not type(handler["request"]) == str:
		handler["request"] = "String"
	if not type(handler["added"]) == str:
		handler["added"] = ": "

	if not type(handler["allowedChars"]) == list:
		handler["allowedChars"] = []
	if not type(handler["allowedAnswers"]) == list:
		handler["allowedAnswers"] = []
	if not type(handler["blockedAnswers"]) == list:
		handler["blockedAnswers"] = []

	if not type(handler["space"]) == bool:
		handler["space"] = True
	if not type(handler["empty"]) == bool:
		handler["empty"] = False
	if not type(handler["verification"]) == bool:
		handler["verification"] = False
	if not type(handler["verbose"]) == bool:
		handler["verbose"] = False

	if not type(handler["fixedLength"]) == int:
		handler["fixedLength"] = 0
	if handler["fixedLength"] < 0:
		handler["fixedLength"] = 0

	# Stylings.
	allowedStyle = Fore.CYAN
	lengthStyle = Back.GREEN + Fore.MAGENTA

	if style.setting_plainMode:
		allowedStyle = ""
		lengthStyle = ""

	# Empty strings.
	if not handler["empty"]:
		handler["blockedAnswers"].append("")

	# Allowed and blocked characters
	charactersRange = list(range(0, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 256))

	if handler["space"]:
		charactersRange.remove(32)

	blockedChars = [chr(char) for char in charactersRange]

	for char in handler["allowedChars"]:
		try:
			blockedChars.remove(char)
		except:
			pass

	# Allowed answers.
	allowedString = ""
	if handler["allowedAnswers"] != []:
		allowedString = allowedStyle + "[" + ", ".join(handler["allowedAnswers"]) + "]" + Style.RESET_ALL + " "
		
	# Fixed length.
	lengthString = ""
	if handler["fixedLength"] > 0:
		lengthStyle + "[" + str(handler["fixedLength"]) + "]" + Style.RESET_ALL + " "

	# Input.
	while True:
		try:
			answer = str(input(allowedString + lengthString + handler["request"] + handler["added"]))

			if not style.setting_caseSensitive: # Case-sensitiveness.
				answer = answer.lower()

			if handler["verbose"]: # Verbosity.
				output({"type": "verbose", "string": "VERBOSE, INPUT: " + answer})

			if handler["fixedLength"] != 0 and len(answer) != handler["fixedLength"]: # Checks length.
				output({"type": "error", "string": "LENGTH ERROR"})
				continue
			
			if True in [bChar in [aChar for aChar in list(answer)] for bChar in blockedChars]: # Checks blocked characters.
				output({"type": "error", "string": "CHARACTER ERROR"})
				continue

			if answer in handler["blockedAnswers"]: # Checks blocked answers.
				output({"type": "error", "string": "ANSWER ERROR"})
				continue

			if handler["allowedAnswers"] == [] or answer in handler["allowedAnswers"]: # Checks allowed answers.
				if not handler["verification"]: # Checks verification.
					return answer

				else:
					verificationHandler = {key: handler[key] for key in handler}
					verificationHandler["request"] = "Verification"
					verificationHandler["verification"] = False # Disables verification on the verification handler to avoid looping.
					
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

	# Strings.
	handler["request"] = "Date"
	handler["added"] = " [YYYY-MM-DD]: "

	# Bools.
	handler["placeholders"] = False
	handler["verbose"] = False

	# Updates the handler.
	handler.update(dateHandler)

	# Checks types and values.
	if not type(handler["request"]) == str:
		handler["request"] = "Date"
	if not type(handler["added"]) == str:
		handler["added"] = " [YYYY-MM-DD]: "

	if not type(handler["placeholders"]) == bool:
		handler["placeholders"] = False
	if not type(handler["verbose"]) == bool:
		handler["verbose"] = False

	# String handler.
	strHandler = {}
	strHandler["request"] = handler["request"]
	strHandler["added"] = handler["added"]
	strHandler["allowedChars"] = ["-"]
	strHandler["space"] = False
	strHandler["fixedLength"] = 10

	while True:
		answer = strIn(strHandler)

		if handler["verbose"]:
			output({"type": "verbose", "string": "VERBOSE, INPUT: " + answer})

		try: # From an answer of Eduard Stepanov on https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
			if (answer.replace("x", "1") if handler["placeholders"] else answer) != datetime.strptime(answer.replace("x", "1") if handler["placeholders"] else answer, "%Y-%m-%d").strftime('%Y-%m-%d'):
				raise(ValueError)

			return answer
		
		except(ValueError):
			pass
		
		output({"type": "error", "string": "DATE FORMAT ERROR"})

def boolIn(boolHandler={}) -> bool: # Bool input.
	handler = {}

	# Strings.
	handler["request"] = "Bool"
	handler["added"] = " [y/n]: "

	# Bools.
	handler["verbose"] = False

	# Updates the handler.	
	handler.update(boolHandler)

	# Checks types and values.
	if not type(handler["request"]) == str:
		handler["request"] = "Bool"
	if not type(handler["added"]) == str:
		handler["added"] = " [y/n]: "

	if not type(handler["verbose"]) == bool:
		handler["verbose"] = False

	# String handler.
	strHandler = {}
	strHandler["request"] = handler["request"]
	strHandler["added"] = handler["added"]
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

	# Strings.
	handler["request"] = "Number"
	handler["added"] = ": "

	# Lists.
	handler["allowedRange"] = [] # The allowed range for return value. Must be a [a, b] interval where a < b.
	handler["allowedTypes"] = ["int", "float"] # Allowed types for return value.

	# Bools.
	handler["verbose"] = False

	# Integers.
	handler["round"] = -1 # Rounding number.

	# Updated the handler.
	handler.update(numberHandler)

	# Checks types and values.
	if not type(handler["request"]) == str:
		handler["request"] = "Number"
	if not type(handler["added"]) == str:
		handler["added"] = ": "

	if not type(handler["allowedRange"]) == list:
		handler["allowedRange"] = []
	if len(handler["allowedRange"]) != 2 or False in [type(number) not in [int, float] for number in handler["allowedRange"]]:
		handler["allowedRange"] = []
	elif handler["allowedRange"][0] > handler["allowedRange"][1]:
		handler["allowedRange"] = []
	if not type(handler["allowedTypes"]) == list:
		handler["allowedTypes"] = ["int", "float"]
	if len(handler["allowedTypes"]) not in [1, 2] or set(handler["allowedTypes"]).intersection({"int", "float"}) == set():
		handler["allowedTypes"] = ["int", "float"]

	if not type(handler["verbose"]) == bool:
		handler["verbose"] = False

	if not type(handler["round"]) == int:
		handler["round"] = -1

	# Stylings.
	rangeString = ""
	rangeStyle = Fore.GREEN

	if style.setting_plainMode:
		rangeStyle = ""

	if len(handler["allowedRange"]):
		rangeString = rangeStyle + "[" + str(handler["allowedRange"][0]) + ", " + str(handler["allowedRange"][1]) + "] " + Style.RESET_ALL

	while True:
		try:
			rawAnswer = str(input(rangeString + handler["request"] + handler["added"]))

			if handler["verbose"]:
				output({"type": "verbose", "string": "VERBOSE, INPUT: " + rawAnswer})
			
			if rawAnswer != "": # Checks empty strings.
				answer = float(rawAnswer)

				if len(handler["allowedRange"]) == 2: # Checks range.
					if answer <= handler["allowedRange"][0] or answer >= handler["allowedRange"][1]:
						output({"type": "error", "string": "RANGE ERROR"})
						continue
				
				if int(answer) == answer and "int" in handler["allowedTypes"]: # Integers.
					return int(answer)
				
				elif "float" in handler["allowedTypes"]: # Floats.
					return round(answer, int(handler["round"])) if handler["round"] > -1 else answer

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

	# Strings.
	handler["request"] = "List item"
	handler["added"] = ": "

	# Lists.
	handler["list"] = [] # The list from which to choose the output.

	# Updates the handler.
	handler.update(listHandler)

	# Number handler.
	numberHandler = {}
	numberHandler["request"] = handler["request"]
	numberHandler["added"] = handler["added"]
	numberHandler["allowedTypes"] = ["int"]


	# Checks types and values.
	if not type(handler["request"]) == str:
		handler["request"] = "List "
	if not type(handler["added"]) == str:
		handler["added"] = ": "

	if not type(handler["list"]) == list:
		handler["list"] = []

	if len(handler["list"]) == 0: # Returns None for an empty list.
		answer = None
		
	elif len(handler["list"]) == 1: # Returns the only item for a list that contains a single entry.
		answer = handler["list"][0]
	
	else:
		print("\n".join([str(handler["list"].index(item)) + ": " + str(item) for item in handler["list"]]))
		numberHandler["allowedRange"] = [0, len(handler["list"]) - 1]
		
		answer = handler["list"][numIn(numberHandler)]
			
	return answer