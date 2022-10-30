from colorama import init, Fore
init()

# COMMANDS HANDLING

def getCommand(commandString: str) -> dict:
	output = {}
	errorString = ""

	while True:
		try: 

			output["raw"] = " ".join(input(errorString + commandString).split()).lower()
			instructions = output["raw"].split(" ")

			# OPTIONS: SINGLE DASH [[-key1, value1], ...] AND DOUBLE DASH [--key1, ...]

			output["sdOpts"] = []
			output["ddOpts"] = []

			if "_" not in instructions[0]:
				output["command"] = instructions[0]

			else:
				errorString = Fore.RED + "\nSYNTAX ERROR " + Fore.RESET
				continue

			for inst in instructions:
				if "--" in inst:
					output["ddOpts"].append(inst)
				
				elif "-" in inst:
					try:
						if type(float(inst)) == float:
							pass

					except(ValueError):
						output["sdOpts"].append([inst, instructions[instructions.index(inst) + 1]])
		
		except(IndexError):
			errorString = Fore.RED + "\nSYNTAX ERROR " + Fore.RESET
			continue

		except(EOFError, KeyboardInterrupt):
			errorString = Fore.RED + "\nKEYBOARD ERROR " + Fore.RESET
			continue
			
		return output