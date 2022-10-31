from colorama import init, Fore, Back, Style
init()

# COMMANDS HANDLING

def cmdIn(commandHandler={}) -> dict: # Command input.
	handler = {}

	handler["request"] = ""
	handler["addedChars"] = ": "

	handler["style"] = ""
	handler["errorStyle"] = Back.RED + Fore.WHITE

	handler["verbose"] = False
	handler["verboseStyle"] = Fore.CYAN

	if commandHandler == {}:
		return handler

	handler.update(commandHandler)

	errorString = ""

	while True:
		try: 

			handler["raw"] = str(input(errorString + handler["style"] + handler["request"] + handler["addedChars"] + Style.RESET_ALL))
			
			if handler["verbose"]:
				print(handler["verboseStyle"] + "VERBOSE, INPUT: " + handler["raw"] + Style.RESET_ALL)

			handler["raw"] = " ".join(handler["raw"].split()).lower() # type: ignore

			instructions = handler["raw"].split(" ")

			# OPTIONS: SINGLE DASH [[-key1, value1], ...] AND DOUBLE DASH [--key1, ...]

			handler["sdOpts"] = []
			handler["ddOpts"] = []

			if "_" not in instructions[0]:
				handler["command"] = instructions[0]

			else:
				errorString = handler["errorStyle"] + "SYNTAX ERROR" + Style.RESET_ALL + " "
				continue

			for inst in instructions:
				if "--" in inst:
					handler["ddOpts"].append(inst)
				
				elif "-" in inst:
					try:
						if type(float(inst)) == float:
							pass

					except(ValueError):
						handler["sdOpts"].append([inst, instructions[instructions.index(inst) + 1]])
		
		except(IndexError):
			errorString = handler["errorStyle"] + "SYNTAX ERROR" + Style.RESET_ALL + " "
			continue

		except(EOFError, KeyboardInterrupt):
			errorString = handler["errorStyle"] + "\nKEYBOARD ERROR" + Style.RESET_ALL + " "
			continue
			
		return handler