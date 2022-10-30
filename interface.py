from colorama import init, Fore
init()

# COMMANDS HANDLING

def getCommand(commandHandler={}) -> dict:
	handler = {}

	handler["string"] = ""
	handler["addedChars"] = ": "

	if commandHandler == {}:
		return handler

	handler.update(commandHandler)

	errorString = ""

	while True:
		try: 

			handler["raw"] = " ".join(input(errorString + handler["string"]).split()).lower()
			instructions = handler["raw"].split(" ")

			# OPTIONS: SINGLE DASH [[-key1, value1], ...] AND DOUBLE DASH [--key1, ...]

			handler["sdOpts"] = []
			handler["ddOpts"] = []

			if "_" not in instructions[0]:
				handler["command"] = instructions[0]

			else:
				errorString = Fore.RED + "\nSYNTAX ERROR " + Fore.RESET
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
			errorString = Fore.RED + "\nSYNTAX ERROR " + Fore.RESET
			continue

		except(EOFError, KeyboardInterrupt):
			errorString = Fore.RED + "\nKEYBOARD ERROR " + Fore.RESET
			continue
			
		return handler