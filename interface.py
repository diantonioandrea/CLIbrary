from colorama import init, Fore, Style
init()

# COMMANDS HANDLING

def getCommand(commandHandler={}) -> dict:
	handler = {}

	handler["string"] = ""
	handler["addedChars"] = ": "

	handler["style"] = ""
	handler["errorStyle"] = Fore.RED

	if commandHandler == {}:
		return handler

	handler.update(commandHandler)

	errorString = ""

	while True:
		try: 

			handler["raw"] = " ".join(input(errorString + handler["style"] + handler["string"] + Style.RESET_ALL).split()).lower()
			instructions = handler["raw"].split(" ")

			# OPTIONS: SINGLE DASH [[-key1, value1], ...] AND DOUBLE DASH [--key1, ...]

			handler["sdOpts"] = []
			handler["ddOpts"] = []

			if "_" not in instructions[0]:
				handler["command"] = instructions[0]

			else:
				errorString = handler["errorStyle"] + "\nSYNTAX ERROR " + Style.RESET_ALL
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
			errorString = handler["errorStyle"] + "\nSYNTAX ERROR " + Style.RESET_ALL
			continue

		except(EOFError, KeyboardInterrupt):
			errorString = handler["errorStyle"] + "\nKEYBOARD ERROR " + Style.RESET_ALL
			continue
			
		return handler