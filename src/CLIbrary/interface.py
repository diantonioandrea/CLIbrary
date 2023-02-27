from colorama import Fore, Back, Style
import json

from .settings import *
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
				output({"type": "verbose", "string": "VERBOSE, INPUT: " + rawAnswer})

			rawAnswer = " ".join(rawAnswer.split()).lower()

			instructions = rawAnswer.split(" ")

			# OPTIONS: SINGLE DASH [{(-)key1: value1}, ...] AND DOUBLE DASH [(--)key1, ...]

			sdOpts = {}
			ddOpts = []

			if "-" not in instructions[0]: # Checks the first word.
				answer["command"] = instructions[0]

			else:
				output({"type": "error", "string": "SYNTAX ERROR"})
				continue

			if answer["command"] not in handler["allowedCommands"] and rawAnswer != "": # Checks the commands list.
				output({"type": "error", "string": "UNKNOWN OR UNAVAILABLE COMMAND"})
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
			output({"type": "error", "string": "SYNTAX ERROR"})
			continue

		except(EOFError, KeyboardInterrupt): # Handles keyboard interruptions.
			output({"type": "error", "string": "KEYBOARD ERROR"})
			continue
			
		answer["sdOpts"] = sdOpts
		answer["ddOpts"] = ddOpts
		return answer

def helpPrint(handler={}) -> None:
	from .settings import style

	try:
		helpFile = open(handler["helpPath"], "r")
		helpJson = json.load(helpFile)
		helpFile.close()

		helpElements = []

		if style.setting_darkMode:
			font = Fore.BLACK
			back = Back.BLACK

		else:
			font = Fore.WHITE
			back = Back.WHITE

		for key in helpJson:
			helpString = ""

			if key not in handler["allowedCommands"]:
				helpString += Back.YELLOW + font + " UNAVAILABLE " + Style.RESET_ALL

			helpString += Back.GREEN + font + " " + key + " " + back + Fore.GREEN + " " + helpJson[key]["description"] + " " + Style.RESET_ALL
			
			if "options" in helpJson[key]:
				helpString += Back.GREEN + font + " " + str(len(helpJson[key]["options"])) + " option(s) " + Style.RESET_ALL

				for optionKey in helpJson[key]["options"]:
					if "#" in optionKey:
						helpString += "\n\t" + Back.RED + font + " " + optionKey.replace("#", "") + " "

						if "--" not in optionKey:
							helpString += back + Fore.RED + " " + helpJson[key]["options"][optionKey] + " "
					
					else:
						helpString += "\n\t" + Back.CYAN + font + " " + optionKey + " "

						if "--" not in optionKey:
							helpString += back + Fore.CYAN + " " + helpJson[key]["options"][optionKey] + " "
					
					helpString += Style.RESET_ALL
			
			helpElements.append(helpString)
		
		print("\n\n".join(helpElements)) if len(helpElements) else output({"type": "warning", "string": "NO HELP FOR CURRENTLY AVAILABLE COMMANDS", "before": "\n"})
		
	except(FileNotFoundError):
		output({"type": "error", "string": "HELP FILE ERROR"})
	
	except:
		output({"type": "error", "string": "HELP ERROR"})