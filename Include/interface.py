from colorama import init, Fore
init()

# COMMANDS HANDLING

def getCommand(commandString: str):
	errorString = ""

	while True:
		try: 

			commandString = " ".join(input(errorString + commandString).split()).lower()
			instructions = commandString.split(" ")

			# OPTIONS: SINGLE DASH [[-key1, value1], ...] AND DOUBLE DASH [--key1, ...]

			sdOpts = []
			ddOpts = []

			if "_" not in instructions[0]:
				command = instructions[0]

			else:
				errorString = Fore.RED + "\nSYNTAX ERROR " + Fore.RESET
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
			errorString = Fore.RED + "\nSYNTAX ERROR " + Fore.RESET
			continue

		except(EOFError, KeyboardInterrupt):
			errorString = Fore.RED + "\nKEYBOARD ERROR " + Fore.RESET
			continue
			
		return command, sdOpts, ddOpts