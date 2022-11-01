from colorama import init, Fore, Back, Style
from pickle import load, dump
init()

# FILES HANDLING

def aLoad(fileHandler: dict): # Automatic loading.
	handler = {}

	handler["path"] = ""
	handler["type"] = "pickle"

	handler["errorStyle"] = Back.RED + Fore.WHITE

	handler["verbose"] = False
	handler["verboseStyle"] = Back.YELLOW

	handler.update(fileHandler)

	try:
		dataFile = open(handler["path"], "rb")
		data = load(dataFile)
		dataFile.close()
				
	except(FileNotFoundError):
		print(handler["errorStyle"] + "\'" + fileHandler["path"] + "\' NOT FOUND ERROR" + Style.RESET_ALL)
		data = None

	except:
		print(handler["errorStyle"] + "FILE ERROR" + Style.RESET_ALL)
		data = None

	return data
	
def aDump(fileHandler: dict) -> None: # Automatic dumping.
	handler = {}

	handler["path"] = ""
	handler["data"] = None
	handler["type"] = "pickle"

	handler["errorStyle"] = Back.RED + Fore.WHITE

	handler["verbose"] = False
	handler["verboseStyle"] = Back.YELLOW

	handler.update(fileHandler)

	try:
		dataFile = open(handler["path"], "wb")
		dump(handler["data"], dataFile)
		dataFile.close()
	
	except:
		print(handler["errorStyle"] + "FILE ERROR" + Style.RESET_ALL)