from pickle import load, dump

from .outputs import *
from .settings import data

# FILES HANDLING

def aLoad(fileHandler: dict): # Automatic loading.
	handler = {}

	handler["path"] = ""
	handler["ignoreMissing"] = False

	handler.update(fileHandler)

	try:
		dataFile = open(handler["path"] + data.setting_fileExtension, "rb")
		data = load(dataFile)
		dataFile.close()
				
	except(FileNotFoundError):
		data = None
		if not handler["ignoreMissing"]:
			output({"type": "error", "string": "\'" + fileHandler["path"] + data.setting_fileExtension + "\' NOT FOUND"})

	except:
		data = None
		output({"type": "error", "string": "FILE ERROR"})

	return data
	
def aDump(fileHandler: dict) -> None: # Automatic dumping.
	handler = {}

	handler["path"] = ""
	handler["data"] = None

	handler.update(fileHandler)

	try:
		dataFile = open(handler["path"] + data.setting_fileExtension, "wb")
		dump(handler["data"], dataFile)
		dataFile.close()
	
	except:
		output({"type": "error", "string": "FILE ERROR"})