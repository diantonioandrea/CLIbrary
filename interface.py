from colorama import init, Fore, Back, Style
import json
import outputs
init()

# COMMANDS HANDLING

def cmdIn(commandHandler={}) -> dict: # Command input.
	handler = {}
	answer = {}

	answer["output"] = ""

	handler["request"] = "command"
	handler["addedChars"] = ": "

	handler["style"] = ""

	handler["verbose"] = False

	handler["allowedCommands"] = []

	handler["helpPath"] = ""

	handler.update(commandHandler)

	if "exit" not in handler["allowedCommands"]:
		handler["allowedCommands"].append("exit")
	
	if "help" not in handler["allowedCommands"] and handler["helpPath"] != "":
		handler["allowedCommands"].append("help")

	while True:
		try:
			rawAnswer = str(input(handler["style"] + handler["request"] + Style.RESET_ALL + handler["addedChars"] + Style.RESET_ALL))
			
			if handler["verbose"]:
				outputs.output({"verbose": True, "string": "VERBOSE, INPUT: " + rawAnswer})

			rawAnswer = " ".join(rawAnswer.split()).lower() # type: ignore

			instructions = rawAnswer.split(" ")

			# OPTIONS: SINGLE DASH [[-key1, value1], ...] AND DOUBLE DASH [--key1, ...]

			sdOpts = {}
			ddOpts = []

			if "-" not in instructions[0]:
				answer["command"] = instructions[0]

			else:
				outputs.output({"error": True, "string": "SYNTAX ERROR"})
				continue

			if answer["command"] not in handler["allowedCommands"] and rawAnswer != "":
				outputs.output({"error": True, "string": "UNKNOWN COMMAND"})
				continue

			if answer["command"] == "help":
				helpDict = genHelp(handler)

				if helpDict["errorString"] != "":
					outputs.output({"error": True, "string": helpDict["errorString"]})
					continue
				
				answer["output"] = helpDict["helpString"]

			for inst in instructions:
				if "--" in inst:
					ddOpts.append(inst.replace("--", ""))
				
				elif inst[0] == "-":
					try:
						if type(float(inst)) == float:
							pass

					except(ValueError):
						sdOpts[inst.replace("-", "")] = instructions[instructions.index(inst) + 1]
		
		except(IndexError):
			outputs.output({"error": True, "string": "SYNTAX ERROR"})
			continue

		except(EOFError, KeyboardInterrupt):
			outputs.output({"error": True, "string": "KEYBOARD ERROR"})
			continue
			
		answer["sdOpts"] = sdOpts
		answer["ddOpts"] = ddOpts
		return answer

def genHelp(handler={}) -> dict:
	helpDict = {}

	helpDict["helpString"] = ""
	helpDict["errorString"] = ""

	try:
		helpFile = open(handler["helpPath"], "r")
		helpJson = json.load(helpFile)
		helpFile.close()

		helpElements = []

		for key in helpJson:
			helpString = handler["style"] + key + Style.RESET_ALL
			helpString += "\n\t" + helpJson[key]["description"]
			
			if "mandatoryOptions" in helpJson[key] or "options" in helpJson[key]:
				helpString += "\n\tOptions:" + "\n"

				if "mandatoryOptions" in helpJson[key]:
					helpString += "\t\t" + Fore.RED + helpJson[key]["mandatoryOptions"] + Style.RESET_ALL
					
				if "options" in helpJson[key]:
					helpString += "\t\t" + helpJson[key]["options"]
			
			helpElements.append(helpString)
		
		helpDict["helpString"] = "\n".join(helpElements)

	except(FileNotFoundError):
		helpDict["errorString"] = handler["errorStyle"] + "\nHELP FILE ERROR" + Style.RESET_ALL + " "
	
	except:
		helpDict["errorString"] = handler["errorStyle"] + "\nHELP ERROR" + Style.RESET_ALL + " "
	
	return helpDict