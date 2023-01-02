from colorama import Fore, Back, Style

def output(outputHandler: dict):
	handler = {}

	handler["error"] = False
	handler["verbose"] = False

	# Prints these style-unaffected strings before and after the main part
	handler["before"] = ""
	handler["after"] = ""

	handler["string"] = ""

	handler["errorStyle"] = Back.RED + Fore.WHITE + " \u25B2 " + Back.WHITE + Fore.RED + " "
	handler["verboseStyle"] = Back.YELLOW + Fore.WHITE + " \u25CF " + Back.WHITE + Fore.YELLOW + " "

	handler.update(outputHandler)

	if handler["error"]:
		outputStyle = handler["errorStyle"]

	elif handler["verbose"]:
		outputStyle = handler["verboseStyle"]

	print(handler["before"] + outputStyle + handler["string"] + " " + Style.RESET_ALL + handler["after"])