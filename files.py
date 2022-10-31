from colorama import init, Fore
from pickle import load, dump
init()

# FILES HANDLING

def autoload(fileHandler: dict) -> dict:
	handler = {}

	handler["path"] = ""
	handler["type"] = "pickle"

	handler["errorColor"] = Fore.RED

	handler.update(fileHandler)

	if fileHandler == {}:
		return handler

	try:
		dataFile = open(handler["path"], "rb")
		data = load(dataFile)
		dataFile.close()
		
		handler["data"] = data
		
	except(FileNotFoundError):
		print(handler["errorColor"] + "fileHandler \'" + fileHandler["path"] + "\' NOT FOUND ERROR " + Fore.RESET)
		handler["data"] = None

	except:
		print(handler["errorColor"] + "ERROR " + Fore.RESET)
		handler["data"] = None

	return handler
	
def autodump(fileHandler: dict) -> dict:
	handler = {}

	handler["path"] = ""
	handler["data"] = None
	handler["type"] = "pickle"

	handler["errorColor"] = Fore.RED

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
		print(handler["errorColor"] + "ERROR " + Fore.RESET)

	return handler