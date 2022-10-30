from colorama import init, Fore
from pickle import load, dump
init()

# FILES HANDLING

def autoload(file: dict) -> dict:
	loadFile = {}

	loadFile["path"] = ""

	loadFile.update(file)

	if file == {}:
		return loadFile

	try:
		dataFile = open(loadFile["path"], "rb")
		data = load(dataFile)
		dataFile.close()
		
		loadFile["data"] = data
		
	except(FileNotFoundError):
		print(Fore.RED + "FILE \'" + file["path"] + "\' NOT FOUND ERROR " + Fore.RESET)
		loadFile["data"] = None

	except:
		print(Fore.RED + "ERROR " + Fore.RESET)
		loadFile["data"] = None

	return loadFile
	
def autodump(file: dict) -> dict:
	dumpFile = {}

	dumpFile["path"] = ""
	dumpFile["data"] = None

	dumpFile.update(file)

	if file == {}:
		return dumpFile

	dumpFile["success"] = False

	try:
		dataFile = open(dumpFile["path"], "wb")
		dump(dumpFile["data"], dataFile)
		dataFile.close()
		dumpFile["success"] = True
	
	except:
		print(Fore.RED + "ERROR " + Fore.RESET)

	return dumpFile