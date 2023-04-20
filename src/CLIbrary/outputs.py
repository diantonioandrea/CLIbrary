from colorama import Fore, Back, Style

def output(outputHandler: dict) -> None:
	from .settings import style

	handler = {}

	# Strings.
	handler["string"] = "" # Output string.
	handler["type"] = "" # Output type.
	handler["before"] = "" # Prints this style-unaffected string before the main string.
	handler["after"] = "" # Prints this style-unaffected string after the main string.

	handler.update(outputHandler)

	# Checks types and values.
	if not type(handler["type"]) == str:
		handler["type"] = ""
	if not type(handler["before"]) == str:
		handler["before"] = ""
	if not type(handler["after"]) == str:
		handler["after"] = ""
	if not type(handler["string"]) == str:
		handler["string"] = ""

	# Checks global style
	if style.setting_darkMode:
		errorStyle = Back.RED + Fore.BLACK + " \u25A0 " + Back.BLACK + Fore.RED + " "
		warningStyle = Back.YELLOW + Fore.BLACK + " \u25B2 " + Back.BLACK + Fore.YELLOW + " "
		verboseStyle = Back.CYAN + Fore.BLACK + " \u25CF " + Back.BLACK + Fore.CYAN + " "
	
	else:
		errorStyle = Back.RED + Fore.WHITE + " \u25A0 " + Back.WHITE + Fore.RED + " "
		warningStyle = Back.YELLOW + Fore.WHITE + " \u25B2 " + Back.WHITE + Fore.YELLOW + " "
		verboseStyle = Back.CYAN + Fore.WHITE + " \u25CF " + Back.WHITE + Fore.CYAN + " "

	# Checks output type.
	if handler["type"] == "error":
		outputStyle = errorStyle
	
	elif handler["type"] == "warning":
		outputStyle = warningStyle

	elif handler["type"] == "verbose":
		outputStyle = verboseStyle

	elif handler["type"] == "":
		outputStyle = ""
	
	else:
		output({"type": "warning", "string": "OUTPUT MISCONFIGURED. PLEASE REFER TO THE DOCUMENTATION.", "before": "\n", "after": "\n"})
		outputStyle = ""

	if style.setting_plainMode: # Checks plain mode.
		if handler["type"] in ["error", "warning", "verbose"]:
			outputStyle = "[" + handler["type"].upper() + "] "

		else:
			outputStyle = ""

	print(handler["before"] + outputStyle + handler["string"] + " " + Style.RESET_ALL + handler["after"])