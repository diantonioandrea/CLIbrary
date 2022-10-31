from colorama import init, Fore, Back, Style
init()

# COMMANDS HANDLING

def cmdIn(commandHandler={}) -> dict: # Command input.
	handler = {}
	answer = {}

	handler["request"] = "command"
	handler["addedChars"] = ": "

	handler["style"] = ""
	handler["errorStyle"] = Back.RED + Fore.WHITE

	handler["verbose"] = False
	handler["verboseStyle"] = Back.YELLOW

	if commandHandler == {}:
		return handler

	handler.update(commandHandler)

	errorString = ""

	while True:
		try: 

			rawAnswer = str(input(errorString + handler["style"] + handler["request"] + handler["addedChars"] + Style.RESET_ALL))
			
			if handler["verbose"]:
				print(handler["verboseStyle"] + "VERBOSE, INPUT: " + rawAnswer + Style.RESET_ALL)

			rawAnswer = " ".join(rawAnswer.split()).lower() # type: ignore

			instructions = rawAnswer.split(" ")

			# OPTIONS: SINGLE DASH [[-key1, value1], ...] AND DOUBLE DASH [--key1, ...]

			sdOpts = []
			ddOpts = []

			if "_" not in instructions[0]:
				answer["command"] = instructions[0]

			else:
				errorString = handler["errorStyle"] + "SYNTAX ERROR" + Style.RESET_ALL + " "
				continue

			for inst in instructions:
				if "--" in inst:
					ddOpts.append(inst)
				
				elif "-" in inst:
					try:
						if type(float(inst)) == float:
							pass

					except(ValueError):
						sdOpts.append([inst, instructions[instructions.index(inst) + 1]])
		
		except(IndexError):
			errorString = handler["errorStyle"] + "SYNTAX ERROR" + Style.RESET_ALL + " "
			continue

		except(EOFError, KeyboardInterrupt):
			errorString = handler["errorStyle"] + "\nKEYBOARD ERROR" + Style.RESET_ALL + " "
			continue
			
		answer["sdOpts"] = sdOpts
		answer["ddOpts"] = ddOpts
		return answer