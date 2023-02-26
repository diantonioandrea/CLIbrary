from colorama import Fore, Back, Style

def output(outputHandler: dict) -> None:
	handler = {}

	handler["type"] = ""

	# Prints these style-unaffected strings before and after the main part
	handler["before"] = ""
	handler["after"] = ""

	handler["string"] = ""

	handler["errorStyle"] = Back.RED + Fore.WHITE + " \u25A0 " + Back.WHITE + Fore.RED + " "
	handler["warningStyle"] = Back.YELLOW + Fore.WHITE + " \u25B2 " + Back.WHITE + Fore.YELLOW + " "
	handler["verboseStyle"] = Back.CYAN + Fore.WHITE + " \u25CF " + Back.WHITE + Fore.CYAN + " "

	handler.update(outputHandler)

	if handler["type"] == "error":
		outputStyle = handler["errorStyle"]
	
	elif handler["type"] == "warning":
		outputStyle = handler["warningStyle"]

	elif handler["type"] == "verbose":
		outputStyle = handler["verboseStyle"]

	else:
		output({"type": "warning", "string": "OUTPUT MISCONFIGURED. PLEASE REFER TO THE DOCUMENTATION.", "before": handler["before"], "after": handler["after"]})
		outputStyle = ""

	print(handler["before"] + outputStyle + handler["string"] + " " + Style.RESET_ALL + handler["after"])