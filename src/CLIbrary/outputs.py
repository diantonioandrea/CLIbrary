from colorama import Fore, Back, Style

def output(outputHandler: dict) -> None:
	from .settings import style

	handler = {}

	# Output type.
	handler["type"] = ""

	# Prints these style-unaffected strings before and after the main part.
	handler["before"] = ""
	handler["after"] = ""

	# Output string.
	handler["string"] = ""

	handler.update(outputHandler)

	if style.setting_darkMode:
		errorStyle = Back.RED + Fore.BLACK + " \u25A0 " + Back.BLACK + Fore.RED + " "
		warningStyle = Back.YELLOW + Fore.BLACK + " \u25B2 " + Back.BLACK + Fore.YELLOW + " "
		verboseStyle = Back.CYAN + Fore.BLACK + " \u25CF " + Back.BLACK + Fore.CYAN + " "
	
	else:
		errorStyle = Back.RED + Fore.WHITE + " \u25A0 " + Back.WHITE + Fore.RED + " "
		warningStyle = Back.YELLOW + Fore.WHITE + " \u25B2 " + Back.WHITE + Fore.YELLOW + " "
		verboseStyle = Back.CYAN + Fore.WHITE + " \u25CF " + Back.WHITE + Fore.CYAN + " "

	customStyle = ""

	if handler["type"] == "error":
		outputStyle = errorStyle
	
	elif handler["type"] == "warning":
		outputStyle = warningStyle

	elif handler["type"] == "verbose":
		outputStyle = verboseStyle

	elif handler["type"] == "custom":
		outputStyle = customStyle
	
	else:
		output({"type": "warning", "string": "OUTPUT MISCONFIGURED. PLEASE REFER TO THE DOCUMENTATION.", "before": handler["before"], "after": handler["after"]})
		outputStyle = ""

	print(handler["before"] + outputStyle + handler["string"] + " " + Style.RESET_ALL + handler["after"])