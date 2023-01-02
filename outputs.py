from colorama import Fore, Back, Style

def output(outputHandler: dict):
	handler = {}

	handler["error"] = False
	handler["verbose"] = False

	handler["string"] = ""

	handler["errorStyle"] = Back.RED + Fore.WHITE + " ! " + Back.WHITE + Fore.RED + " "
	handler["verboseStyle"] = Back.YELLOW + " ? " + Back.WHITE + Fore.YELLOW + " "

	handler.update(outputHandler)

	if handler["error"]:
		print(handler["errorStyle"] + handler["string"] + " " + Style.RESET_ALL)

	elif handler["verbose"]:
		print(handler["verboseStyle"] + handler["string"] + " " + Style.RESET_ALL)