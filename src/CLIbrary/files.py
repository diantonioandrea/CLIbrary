from pickle import load, dump

from .outputs import *

# FILES HANDLING

def aLoad(fHandler: dict): # Automatic loading.
	from .settings import data

	handler = {}

	# Strings.
	handler["path"] = ""

	# Bools.
	handler["ignoreMissing"] = False

	# Updates the handler.
	handler.update(fHandler)

	# Checks types and values.
	if not type(handler["path"]) == str:
		handler["path"] = ""

	if not type(handler["ignoreMissing"]) == bool:
		handler["ignoreMissing"] = False

	try: # Tries to gather data from file.
		dataFile = open(handler["path"] + data.setting_fileExtension, "rb")
		data = load(dataFile)
		dataFile.close()
				
	except(FileNotFoundError):
		data = None
		if not handler["ignoreMissing"]:
			output({"type": "error", "string": "\'" + fHandler["path"] + data.setting_fileExtension + "\' NOT FOUND"})

	except:
		data = None
		output({"type": "error", "string": "FILE ERROR"})

	return data
	
def aDump(fHandler: dict) -> None: # Automatic dumping.
	from .settings import data
	
	handler = {}

	# Strings.
	handler["path"] = ""

	# Others.
	handler["data"] = None

	# Updates the handler.
	handler.update(fHandler)

	# Checks types and values.
	if not type(handler["path"]) == str:
		handler["path"] = ""

	try: # Try to write the file.
		dataFile = open(handler["path"] + data.setting_fileExtension, "wb")
		dump(handler["data"], dataFile)
		dataFile.close()
	
	except:
		output({"type": "error", "string": "FILE ERROR"})