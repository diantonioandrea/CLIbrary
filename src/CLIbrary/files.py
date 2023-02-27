from pickle import load, dump

from .outputs import *

# FILES HANDLING

def aLoad(fileHandler: dict): # Automatic loading.
	handler = {}

	handler["path"] = ""
	handler["ignoreMissing"] = False
	handler["dark"] = False # Option for outputs.output.

	handler.update(fileHandler)
	errorHandler = {"type": "error"}

	try:
		dataFile = open(handler["path"], "rb")
		data = load(dataFile)
		dataFile.close()
				
	except(FileNotFoundError):
		if not handler["ignoreMissing"]:
			errorHandler["string"] = "\'" + fileHandler["path"] + "\' NOT FOUND ERROR"
			output(errorHandler)
		data = None

	except:
		errorHandler["string"] = "FILE ERROR"
		output(errorHandler)
		data = None

	return data
	
def aDump(fileHandler: dict) -> None: # Automatic dumping.
	handler = {}

	handler["path"] = ""
	handler["data"] = None
	handler["dark"] = False # Option for outputs.output.

	handler.update(fileHandler)
	errorHandler = {"type": "error"}

	try:
		dataFile = open(handler["path"], "wb")
		dump(handler["data"], dataFile)
		dataFile.close()
	
	except:
		errorHandler["string"] = "FILE ERROR"
		output(errorHandler)