# COMMANDS HANDLING

def getCommand(commandString: str):
	while True:
		try: 

			command = " ".join(input(commandString).split()).lower()
			instructions = command.split(" ")

			# OPTIONS: SINGLE DASH [[-key1, value1], ...] AND DOUBLE DASH [--key1, ...]

			sdOpts = []
			ddOpts = []

			if "_" not in instructions[0]:
				command = instructions[0]

			for inst in instructions:
				if "--" in inst:
					ddOpts.append(inst)
				
				elif "-" in inst:
					try:
						if type(float(inst)) == float:
							pass

					except(ValueError):
						sdOpts.append([inst, instructions[instructions.index(inst) + 1]])
		
		except(IndexError, EOFError, KeyboardInterrupt):
			continue
			
		return command, sdOpts, ddOpts