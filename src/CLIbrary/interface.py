from colorama import Fore, Back, Style
import json
from .outputs import *

# COMMANDS HANDLING

def cmdIn(commandHandler={}) -> dict: # Command input.
	handler = {}
	answer = {}

	handler["request"] = "enter a command"
	handler["addedChars"] = ": "

	handler["style"] = ""

	handler["verbose"] = False

	handler["allowedCommands"] = ["exit"]

	handler["helpPath"] = ""

	handler.update(commandHandler)

	if "exit" not in handler["allowedCommands"]: # "exit" must be in the allowed commands.
		handler["allowedCommands"].append("exit")
	
	if "help" not in handler["allowedCommands"] and handler["helpPath"] != "": # "help" is an embedded command.
		handler["allowedCommands"].append("help")

	if "help" in handler["allowedCommands"] and handler["helpPath"] == "":
		handler["allowedCommands"].remove("help")

	while True:
		try:
			rawAnswer = str(input(handler["style"] + handler["request"] + Style.RESET_ALL + handler["addedChars"] + Style.RESET_ALL))
			
			if handler["verbose"]:
				output({"verbose": True, "string": "VERBOSE, INPUT: " + rawAnswer})

			rawAnswer = " ".join(rawAnswer.split()).lower()

			instructions = rawAnswer.split(" ")

			# OPTIONS: SINGLE DASH [{(-)key1: value1}, ...] AND DOUBLE DASH [(--)key1, ...]

			sdOpts = {}
			ddOpts = []

			if "-" not in instructions[0]: # Checks the first word.
				answer["command"] = instructions[0]

			else:
				output({"error": True, "string": "SYNTAX ERROR"})
				continue

			if answer["command"] not in handler["allowedCommands"] and rawAnswer != "": # Checks the commands list.
				output({"error": True, "string": "UNKNOWN OR UNAVAILABLE COMMAND"})
				continue

			if answer["command"] == "help": # Prints the help.
				helpPrint(handler)
				continue

			for inst in instructions: # Parse the options.
				if "--" in inst:
					ddOpts.append(inst.replace("--", ""))
				
				elif inst[0] == "-":
					try:
						if type(float(inst)) == float:
							pass

					except(ValueError):
						sdOpts[inst.replace("-", "")] = instructions[instructions.index(inst) + 1]
		
		except(IndexError):
			output({"error": True, "string": "SYNTAX ERROR"})
			continue

		except(EOFError, KeyboardInterrupt): # Handles keyboard interruptions.
			output({"error": True, "string": "KEYBOARD ERROR"})
			continue
			
		answer["sdOpts"] = sdOpts
		answer["ddOpts"] = ddOpts
		return answer

def helpPrint(handler={}) -> None:
	try:
		helpFile = open(handler["helpPath"], "r")
		helpJson = json.load(helpFile)
		helpFile.close()

		helpElements = []

		for key in helpJson:
			helpString = ""

			if key not in handler["allowedCommands"]:
				helpString += Back.YELLOW + Fore.WHITE + " UNAVAILABLE " + Style.RESET_ALL

			helpString += Back.GREEN + Fore.WHITE + " " + key + " " + Back.WHITE + Fore.GREEN + " " + helpJson[key]["description"] + " " + Style.RESET_ALL
			
			if "options" in helpJson[key]:
				helpString += Back.GREEN + Fore.WHITE + " " + str(len(helpJson[key]["options"])) + " option(s) " + Style.RESET_ALL

				for optionKey in helpJson[key]["options"]:
					if "#" in optionKey:
						helpString += "\n\t" + Back.RED + Fore.WHITE + " " + optionKey.replace("#", "") + " "

						if "--" not in optionKey:
							helpString += Back.WHITE + Fore.RED + " " + helpJson[key]["options"][optionKey] + " "
					
					else:
						helpString += "\n\t" + Back.CYAN + Fore.WHITE + " " + optionKey + " "

						if "--" not in optionKey:
							helpString += Back.WHITE + Fore.CYAN + " " + helpJson[key]["options"][optionKey] + " "
					
					helpString += Style.RESET_ALL
			
			helpElements.append(helpString)
		
		print("\n\n".join(helpElements)) if len(helpElements) else output({"warning": True, "string": "NO HELP FOR CURRENTLY AVAILABLE COMMANDS", "before": "\n"})
		
	except(FileNotFoundError):
		output({"error": True, "string": "HELP FILE ERROR"})
	
	except:
		output({"error": True, "string": "HELP ERROR"})