from colorama import init, Fore, Style
from pickle import load, dump
init()

# FILES HANDLING

def autoload(fileHandler: dict) -> dict:
	handler = {}

	handler["path"] = ""
	handler["type"] = "pickle"

	handler["errorStyle"] = Fore.RED

	handler.update(fileHandler)

	if fileHandler == {}:
		return handler

	try:
		dataFile = open(handler["path"], "rb")
		data = load(dataFile)
		dataFile.close()
		
		handler["data"] = data
		
	except(FileNotFoundError):
		print(handler["errorStyle"] + "fileHandler \'" + fileHandler["path"] + "\' NOT FOUND ERROR " + Style.RESET_ALL)
		handler["data"] = None

	except:
		print(handler["errorStyle"] + "ERROR " + Style.RESET_ALL)
		handler["data"] = None

	return handler
	
def autodump(fileHandler: dict) -> dict:
	handler = {}

	handler["path"] = ""
	handler["data"] = None
	handler["type"] = "pickle"

	handler["errorStyle"] = Fore.RED

	handler.update(fileHandler)

	if fileHandler == {}:
		return handler

	handler["success"] = False

	try:
		dataFile = open(handler["path"], "wb")
		dump(handler["data"], dataFile)
		dataFile.close()
		handler["success"] = True
	
	except:
		print(handler["errorStyle"] + "ERROR " + Style.RESET_ALL)

	return handler